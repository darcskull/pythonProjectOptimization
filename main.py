import sys

from Dichotomy import dichotomy
from FibonacciIterative import fibonacci_iterative
from FibonacciSolution import fibonacci
from Function import function
from GoldenSection import golden_section
from Scaning import scan


def print_fibonacci():
    a = -10
    b = 45
    tau = 0.01
    cd = 19
    max_iteration = sys.maxsize
    par_a = 2
    par_b = -12
    par_c = 20
    x_opt = -b/2*a
    f_opt = function(x_opt, par_a, par_b, par_c)
    print("Scan")
    scan(a, b, max_iteration, tau, par_a, par_b, par_c)
    print("Golden Section")
    golden_section(a, b, max_iteration, tau, par_a, par_b, par_c)
    print("Dichotomy")
    dichotomy(a, b, max_iteration, tau, par_a, par_b, par_c)
    print("Fibonacci")
    f_fibonacci = fibonacci_iterative(cd+1)
    fibonacci(a, b, max_iteration, tau, cd, f_fibonacci, par_a, par_b, par_c)



if __name__ == '__main__':
    print_fibonacci()
