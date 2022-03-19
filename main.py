from FibonacciFunction import fibonacci_function
from GoldenSection import golden_section
from FibonacciRecursion import fibonacci
from FibonacciIterative import fibonacci_iterative
from FibonacciOptimization import fibonacci_optimization
import time


def print_fibonacci():
    print("Въведете числова граница:")
    input_first = int(input())
    input_second = int(input())
    print("Golden Section: ")
    golden_section(input_first, input_second)
    print("Fibonacci: ")
    fibonacci_function(input_first, input_second)


# print("Въведете номер на член от редицата на Фибоначи")
# input1 = int(input())
# start_time = time.time_ns()
# print(fibonacci(input1))
# end_time = time.time_ns()
# print(end_time-start_time)
# print("")

# startI_time = time.time_ns()
# print(fibonacci_iterative(input1))
# endI_time = time.time_ns()
# print(endI_time-startI_time)
# print("")

# startO_time = time.time_ns()
# print(fibonacci_optimization(input1))
# endO_time = time.time_ns()
# print(endO_time-startO_time)
# print("")


if __name__ == '__main__':
    print_fibonacci()
