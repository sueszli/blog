the asynchronous `promise.all` pattern from javascript is one of my absolute favorite:

i have to rewrite the java code in java 21

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

```js
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function asyncTask() {
    const timeout = Math.floor(Math.random() * 5);
    await sleep(timeout * 1000);
    const threadName = `Thread ${Math.floor(Math.random() * 1000)}`; // Simulate thread name
    const msg = `${threadName} returned result after ${timeout}s`;
    return msg;
}

const numCores = navigator.hardwareConcurrency; // Get the number of logical processor cores
const promises = Array.from({length: numCores}, () =>
    asyncTask()
        .then(t => console.log(t))
        .catch(err => console.error(err.message))
);

Promise.all(promises)
    .then(() => console.log('all done'))
    .catch(err => console.error(err.message));
```

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

# WORK IN PROGRESS.....