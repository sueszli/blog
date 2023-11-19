# the barrier pattern

one of my favorite patterns is chunking the work, running as many workers as you have cores and then waiting for each worker to finish based on the [barrier pattern](https://en.m.wikipedia.org/wiki/Barrier_(computer_science)): "a barrier for a group of threads or processes in the source code means any thread/process must stop at this point and cannot proceed until all other threads/processes reach this barrier."

it's a straightforward method to execute multiple tasks simultaneously and await their completion. this pattern is highly adaptable and the best part is: you can leverage the language's runtime or the operating system for scheduling, eliminating the need to create a separate [executor instance](https://stackoverflow.com/questions/32621990/what-are-workers-executors-cores-in-spark-standalone-cluster) or write your own task scheduler.

here's a little collection of implementations in different languages that also serves as a nice comparison between them.

<br>

## java

here's one possible java implementation:

```java
package code;

import java.util.concurrent.CompletableFuture;
import java.util.function.Consumer;
import java.util.function.Supplier;
import java.util.stream.IntStream;

public class ParallelPromisePattern {

    public static void main(String[] args) {
        Supplier<String> asyncTask = () -> {
            var timeout = (int) (Math.random() * 5);
            try {
                Thread.sleep(timeout * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            var threadName = Thread.currentThread().getName();
            var msg = String.format("%s returned result after %ds", threadName, timeout);
            return msg;
        };

        // @formatter:off
        var numCores = Runtime.getRuntime().availableProcessors();
        var promises = IntStream
            .range(0, numCores)
            .mapToObj(i ->
                CompletableFuture.supplyAsync(asyncTask)
                    .thenAcceptAsync((Consumer<String>) (String t) -> System.out.println(t)) // .then()
                    .exceptionally((Throwable t) -> { // .catch()
                        System.err.println(t.getMessage());
                        return null;
                    })
            )
            .toArray(CompletableFuture[]::new);

        CompletableFuture.allOf(promises).join(); // promise.all()
        // @formatter:on

        System.out.println("all done");
    }
}
```

the most concise way to program this pattern out in java is to use lambdas. but using lambdas in java is pretty unintuitive. you either have to definte your own types with `@FunctionalInterface` or know these expressions by heart:

```txt
Supplier       ()    -> x
Consumer       x     -> ()
BiConsumer     x, y  -> ()
Callable       ()    -> x throws ex
Runnable       ()    -> ()
Function       x     -> y
BiFunction     x,y   -> z
Predicate      x     -> boolean
UnaryOperator  x1    -> x2
BinaryOperator x1,x2 -> x3
```

but fortunately, once you do, coding in java becomes a lot more fun.

and in case you were wondering, here's what the implementation would look like, if we would leverage the akka-framework:

```java
package code;

import akka.actor.*;
import akka.pattern.Patterns;
import scala.concurrent.Future;

import java.util.stream.IntStream;

public class ParallelAkkaPattern {

    static class AsyncTask extends AbstractActor {
        @Override
        public Receive createReceive() {
            return receiveBuilder()
                    .match(Integer.class, i -> {
                        var timeout = (int) (Math.random() * 5);
                        Thread.sleep(timeout * 1000);
                        var msg = String.format("%s returned result after %ds", Thread.currentThread().getName(), timeout);
                        getSender().tell(msg, getSelf());
                    })
                    .build();
        }
    }

    public static void main(String[] args) {
        final var system = ActorSystem.create("system");
        final var asyncTaskActor = system.actorOf(Props.create(AsyncTask.class), "asyncTaskActor");

        IntStream.range(0, Runtime.getRuntime().availableProcessors())
                .mapToObj(i -> Patterns.ask(asyncTaskActor, i, 5000))
                .forEach(future -> future.onComplete(result -> System.out.println(result.get()), system.dispatcher()));

        System.out.println("all done");
    }
}
```

and here's a much more concise implementation that's leveraging the akka-framework in scala: 

```scala
import akka.actor.ActorSystem
import akka.dispatch.{ExecutionContexts, Future}
import scala.concurrent.duration._
import scala.util.Random

object ParallelPromisePattern extends App {
  implicit val system: ActorSystem = ActorSystem("ParallelPromisePattern")
  implicit val ec = ExecutionContexts.global()

  val asyncTask = () => {
    val timeout = Random.nextInt(5)
    Thread.sleep(timeout * 1000)
    val threadName = Thread.currentThread().getName
    val msg = s"$threadName returned result after $timeout s"
    msg
  }

  val numCores = Runtime.getRuntime.availableProcessors
  val futures = for (_ <- 0 until numCores) yield Future(asyncTask())

  Future.sequence(futures).onComplete { _ =>
    println("all done")
    system.terminate()
  }
}
```

<br>

## python

```python
import asyncio
import random
from concurrent.futures import ThreadPoolExecutor

def async_task():
    timeout = random.randint(0, 5)
    asyncio.sleep(timeout)
    return f"{threading.current_thread().name} returned result after {timeout}s"

async def main():
    num_cores = multiprocessing.cpu_count()
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                async_task
            )
            for _ in range(num_cores)
        ]
        for response in await asyncio.gather(*futures):
            print(response)
    print("all done")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

<br>

## javascript

```js
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function asyncTask() {
  const timeout = Math.floor(Math.random() * 5);
  await sleep(timeout * 1000);
  const threadName = `Thread ${Math.floor(Math.random() * 1000)}`;
  const msg = `${threadName} returned result after ${timeout}s`;
  return msg;
}

const numCores = navigator.hardwareConcurrency; // num of cores
const promises = Array.from({ length: numCores }, () =>
  asyncTask()
    .then((t) => console.log(t))
    .catch((err) => console.error(err.message))
);

Promise.all(promises)
  .then(() => console.log("all done"))
  .catch((err) => console.error(err.message));
```

<br>

## go

```go
package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

func main() {
	numCores := runtime.NumCPU()

	var wg sync.WaitGroup
	wg.Add(numCores)

	for i := 0; i < numCores; i++ {
		go func(i int) {
			defer wg.Done()

			timeout := time.Duration(rand.Intn(5)) * time.Second
			time.Sleep(timeout)

			msg := fmt.Sprintf("goroutine %d returned result after %s", i, timeout)
			fmt.Println(msg)
		}(i)
	}

	wg.Wait()

	fmt.Println("all done")
}
```

<br>

## erlang

```erlang
-module(main).
-export([start/0, worker/1]).

start() ->
  NumWorkers = 4,  %% unable to read num of cores during runtime
  lists:foreach(
    fun(I) ->
      spawn(fun() -> worker(I) end)
    end,
    lists:seq(1, NumWorkers)),
  wait_for_workers(NumWorkers).

worker(I) ->
  Timeout = rand:uniform(5000),
  timer:sleep(Timeout),
  io:format("process ~p returned result after ~p milliseconds~n", [I, Timeout]),
  main ! done.

wait_for_workers(0) ->
  io:format("all done~n");
wait_for_workers(N) ->
  receive
    done -> wait_for_workers(N - 1)
  end.
```

<br>

## elixir

```elixir
Enum.each(1..System.schedulers_online(), fn i ->
  Task.start(fn ->
    timeout = :rand.uniform(5) * 1000
    :timer.sleep(timeout)
    IO.puts "Task ##{i} returned result after ##{timeout} ms"
  end)
end)
|> Enum.each(&Task.await/1)

IO.puts("all done")
```

<br>

## gleam

```gleam
import gleam/number
import gleam/io
import gleam/list.{each, map}
import gleam/task.{sleep, start_link}
import gleam/random.{int}

let num_tasks = 4 // Replace with the number of schedulers

let tasks =
  list.range(1, num_tasks)
  |> map(fn(i) {
    let timeout = int(1, 5) * 1000
    start_link(fn() {
      sleep(timeout)
      io.println("Task " ++ number.to_string(i) ++ " returned result after " ++ number.to_string(timeout) ++ " ms")
    })
  })

each(tasks, fn(task) { task.await() })

io.println("all done")
```
