from math import sqrt

from Function import function


def golden_section(a, b, m_it, tau, f_par_a, f_par_b, f_par_c):
    t1 = (3 - sqrt(5)) / 2
    t2 = (-1 + sqrt(5)) / 2
    iterator = 0
    x1 = a
    x2 = a + t1 * (b - a)
    x3 = a + t2 * (b - a)
    x4 = b
    c = 4
    f1 = function(x1, f_par_a, f_par_b, f_par_c)
    f2 = function(x2, f_par_a, f_par_b, f_par_c)
    f3 = function(x3, f_par_a, f_par_b, f_par_c)
    f4 = function(x4, f_par_a, f_par_b, f_par_c)
    iterate = 1
    while iterate > tau and iterator < m_it:
        iterator = iterator + 1
        if f2 < f3:
            xm = x2
            b = x3
            x3 = x2
            x2 = a + t1 * (b - a)
            fm = f2
            f4 = f3
            f3 = f2
            f2 = function(x2, f_par_a, f_par_b, f_par_c)
            c = c + 1
        else:
            if f3 < f2:
                xm = x3
                b = x2
                x2 = x3
                x3 = a + t2 * (b - a)
                fm = f3
                f1 = f2
                f2 = f3
                f3 = function(x3, f_par_a, f_par_b, f_par_c)
                c = c + 1
            else:
                xm = x2
                fm = f2
                tau = (b - a)
                a = x2
                b = x3
                x2 = a + t1 * (b - a)
                x3 = a + t2 * (b - a)
                f1 = f2
                f4 = f3
                f2 = function(x2, f_par_a, f_par_b, f_par_c)
                f3 = function(x3, f_par_a, f_par_b, f_par_c)
                c = c + 2

        iterate = t2 * (b - a)

    print("Xm = " + str(xm) + " Fm = " + str(fm) + " Iterator = " + str(iterator) +
          " Tau = " + str(tau) + " C = " + str(c))
