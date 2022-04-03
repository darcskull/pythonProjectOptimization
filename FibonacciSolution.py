from Function import function


def fibonacci(a, b, m_it, tau, c, f, f_par_a, f_par_b, f_par_c):
    tau_l = (b - a) / f[c + 1]
    fm = function(a, f_par_a, f_par_b, f_par_c)
    xm = a
    flag = 0
    i = 0
    iterate = 1
    while iterate:
        if i > c - 2:
            iterate = 0
            continue
        if i > m_it:
            iterate = 0
            tau_l = tau_l * f[c - i]
            c = i + 1
            continue

        i = i + 1
        x = xm + tau_l * f[c - i]
        func = function(x, f_par_a, f_par_b, f_par_c)
        if flag == 0:
            if func <= fm:
                fm = func
                xm = x
                flag = 1
            else:
                c = c - 1
        else:
            if flag == 1:
                if func <= fm:
                    fm = func
                    xm = x
                else:
                    tau_l = - tau_l

    print("Xm = " + str(xm) + " Fm = " + str(fm) + " Tau = " + str(tau) + " C = " + str(c) +
          " Fibonacci " + str(f))
