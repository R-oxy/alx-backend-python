# 0x01. Python - Async

## Resources
Read or watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements
- A `README.md` file at the root of the project is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- All files must be executable
- The length of all files will be tested using `wc`
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules should have documentation (using `python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (using `python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method

## Tasks

### 0. The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer argument (`max_delay`, with a default value of 10) and waits for a random delay between 0 and `max_delay` (inclusive) seconds and eventually returns it. Use the `random` module.

```python
#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### 1. Let's execute multiple coroutines at the same time with async
Import `wait_random` from the previous python file and write an async routine `wait_n` that takes two int arguments (`n` and `max_delay`). You will spawn `wait_random` `n` times with the specified `max_delay`. `wait_n` should return the list of all the delays (float values) in ascending order without using `sort()`.

```python
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### 2. Measure the runtime
Import `wait_n` into `2-measure_runtime.py`. Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`. Your function should return a float. Use the `time` module to measure the approximate elapsed time.

```python
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### 3. Tasks
Import `wait_random` from `0-basic_async_syntax`. Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

```python
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4. Tasks
Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

```python
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```