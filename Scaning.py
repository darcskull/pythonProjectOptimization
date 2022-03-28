from Function import function


def scan(a, b, m_it, tau, f_par_a, f_par_b, f_par_c):
    iterator = 0
    xm = a
    fm = function(a, f_par_a, f_par_b, f_par_c)
    c = int((b - a) / tau) + 1
    x = a + tau
    iterate = 1
    while iterate < b and iterator < m_it:
        iterator = iterator + 1
        f = function(x, f_par_a, f_par_b, f_par_c)
        if f < fm:
            xm = x
            fm = f
        x = x + tau
        iterate = x

    print("Xm = " + str(xm) + " Fm = " + str(fm) + " Iterator = " + str(iterator) +
          " Tau = " + str(tau) + " C = " + str(c))
