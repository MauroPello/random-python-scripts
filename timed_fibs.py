import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.10f} secs")
        return value
    return wrapper_timer


# nth number in the fib sequence
def fib_2_variables(n):
    if n == 0: return 0
    last_2 = 1
    last_1 = 1
    for i in range(2, n):
        tmp = last_1 + last_2
        last_2 = last_1
        last_1 = tmp
    return last_1


def fib_1_variable(n):
    if n == 0: return 0
    last_num = 1
    for i in range(2, n):
        last_num = round(last_num + (last_num/1.618033988749895))
    return last_num


def fib_recursive(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@timer
def timed_fib(fib_type, n):
    return fib_type(n)


def main():
    # middle ground
    print([timed_fib(fib_1_variable, num) for num in range(10)])

    # fastest and most variables used
    print([timed_fib(fib_2_variables, num) for num in range(10)])

    # slowest and least variables used but consumes a lot of memory
    print([timed_fib(fib_recursive, num) for num in range(10)])


if __name__ == "__main__":
    main()
