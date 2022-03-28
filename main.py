import sys

from Function import function
from Scaning import scan


def print_fibonacci():
    a = -10
    b = 45
    tau = 0.01
    max_iteration = sys.maxsize
    par_a = 2
    par_b = -12
    par_c = 20
    x_opt = -b/2*a
    f_opt = function(x_opt, par_a, par_b, par_c)
    scan(a, b, max_iteration, tau, par_a, par_b, par_c)



if __name__ == '__main__':
    print_fibonacci()
