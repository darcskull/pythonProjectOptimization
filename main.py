import sys

from Dichotomy import dichotomy
from FibonacciIterative import fibonacci_iterative
from FibonacciSolution import fibonacci
from GoldenSection import golden_section
from Scaning import scan


def main():
    interval_min = -10
    interval_max = 45
    tau = 0.01
    fib_count = 19
    max_iteration = sys.maxsize
    par_a = 2
    par_b = -12
    par_c = 20

    print("Scan")
    scan(interval_min, interval_max, max_iteration, tau, par_a, par_b, par_c)

    print("Golden Section")
    golden_section(interval_min, interval_max, max_iteration, tau, par_a, par_b, par_c)

    print("Dichotomy")
    dichotomy(interval_min, interval_max, max_iteration, tau, par_a, par_b, par_c)

    print("Fibonacci")
    fib_array = fibonacci_iterative(fib_count + 1)
    fibonacci(interval_min, interval_max, max_iteration, tau, fib_count, fib_array, par_a, par_b, par_c)


if __name__ == '__main__':
    main()
