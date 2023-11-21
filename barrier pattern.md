# the barrier pattern

one of my favorite patterns is chunking the work, running as many workers as you have cores and then waiting for each worker to finish based on the [barrier pattern](<https://en.m.wikipedia.org/wiki/Barrier_(computer_science)>): "a barrier for a group of threads or processes in the source code means any thread/process must stop at this point and cannot proceed until all other threads/processes reach this barrier."

it's a straightforward method to execute multiple tasks simultaneously and await their completion. this pattern is highly adaptable and the best part is: you can leverage the language's runtime or the operating system for scheduling, eliminating the need to create a separate [executor instance](https://stackoverflow.com/questions/32621990/what-are-workers-executors-cores-in-spark-standalone-cluster) or write your own task scheduler.

here's a little collection of implementations in different languages that also serves as a nice comparison between them.

<br><br>

## jvm languages

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

here's the kotlin implementation:

```kotlin
package code

import kotlinx.coroutines.*
import java.util.stream.IntStream
import kotlin.random.Random

fun main() = runBlocking {
    val asyncTask: suspend () -> String = {
        val timeout = Random.nextInt(5)
        delay((timeout * 1000).toLong())

        val threadName = Thread.currentThread().name
        val msg = String.format("%s returned result after %ds", threadName, timeout)
        msg
    }

    val numCores = Runtime.getRuntime().availableProcessors()
    val promises = IntStream
        .range(0, numCores)
        .mapToObj { i ->
            async(Dispatchers.Default) {
                try {
                    asyncTask()
                } catch (t: Throwable) {
                    println(t.message)
                    null
                }
            }
        }
        .toList()

    promises.forEach { promise ->
        println(promise.await())
    }

    println("all done")
}
```

and in case you were wondering, here's what the it would look like in java, if we would leverage the akka-framework:

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

and here's a much more concise akka-version in scala:

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

<br><br>

## python

because of python's [gil](https://wiki.python.org/moin/GlobalInterpreterLock), concurrent programming isn't as fun as it could be – but i'm really looking forward [for this to change](https://peps.python.org/pep-0703/).

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

<br><br>

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

<br><br>

## go

i find both javascript and golang to have the most straightforward solutions – although the one in golang is a lot more performant.

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

<br><br>

## beam languages

finally, let's look at the most popular beam languages.

i personally think the actor-paradigm is much better than the csp-paradigm as implemented in golang – i'd love to get better at programming in erlang at some point.

_erlang:_

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

_elixir:_

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

_gleam:_

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

<br><br>

## rust

```rust
use std::thread;
use std::time::Duration;
use rand::Rng;

fn main() {
    let num_cores = num_cpus::get();

    let mut handles = vec![];

    for i in 0..num_cores {
        let handle = thread::spawn(move || {
            let timeout = rand::thread_rng().gen_range(0..5);
            thread::sleep(Duration::from_secs(timeout));

            println!("thread {} returned result after {}s", i, timeout);
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("all done");
}
```

<br><br>

## c/c++

_c:_

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

void* worker(void *arg) {
    int i = *((int *) arg);
    int timeout = rand() % 5;
    sleep(timeout);
    printf("Thread %d returned result after %d seconds\n", i, timeout);
    return NULL;
}

int main() {
    srand(time(NULL)); // seed for random number generation

    int numCores = sysconf(_SC_NPROCESSORS_ONLN); // get number of cores

    pthread_t threads[numCores];
    int thread_args[numCores];

    // create threads
    for (int i = 0; i < numCores; i++) {
        thread_args[i] = i;
        pthread_create(&threads[i], NULL, worker, &thread_args[i]);
    }

    // wait for all threads to finish
    for (int i = 0; i < numCores; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("all done\n");

    return 0;
}
```

_cpp:_

the interesting thing about the cpp implementation below is how it is more complicated and verbose than the c version although it has so many abstractions for convenience.

```cpp
#include <iostream>
#include <thread>
#include <vector>
#include <chrono>
#include <random>

int main() {
    unsigned int numCores = std::thread::hardware_concurrency();
    std::vector<std::thread> threads(numCores);

    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(0, 4);

    for (unsigned int i = 0; i < numCores; ++i) {
        threads[i] = std::thread(i, &mt, &dist {
            int timeout = dist(mt);
            std::this_thread::sleep_for(std::chrono::seconds(timeout));
            std::cout << "Thread " << i << " returned result after " << timeout << " seconds\n";
        });
    }

    for (auto& th : threads) {
        th.join();
    }

    std::cout << "all done\n";

    return 0;
}
```
