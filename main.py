from FibonacciRecursion import fibonacci
import time


def print_fibonacci():
    print("Въведете номер на член от редицата на Фибоначи")
    input1 = int(input())
    start_time = time.time()
    print(fibonacci(input1))
    end_time = time.time()
    print(end_time-start_time)


if __name__ == '__main__':
    print_fibonacci()

