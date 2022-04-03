from Function import function


def dichotomy(a, b, m_it, tau, f_par_a, f_par_b, f_par_c):
    xc = (a + b) / 2
    dx = (b - a) / 4
    xi = [a, xc - dx, xc, xc + dx, b]
    fi = [1, 1, 1, 1, 1]
    for i in range(5):
        fi[i] = function(xi[i], f_par_a, f_par_b, f_par_c)

    c = 5
    fa = fi[0]
    fb = fi[4]
    fc = fi[2]
    fm = min(fi)
    index = fi.index(fm)
    xm = xi[index]
    iterator = 0
    iterate = 1

    while iterate > tau and iterator < m_it:
        iterator = iterator + 1
        if index == 0:
            b = a + dx
            xc = (a+b)/2
            fb = fi[1]
            fc = function(xc, f_par_a, f_par_b, f_par_c)
            c = c+1
        else:
            if index == 4:
                a = b - dx
                xc = (a + b) / 2
                fa = fi[3]
                fc = function(xc, f_par_a, f_par_b, f_par_c)
                c = c+1
            else:
                a = xm - dx
                b = xm + dx
                xc = xm
                fa = fi[index-1]
                fb = fi[index+1]
                fc = fi[index]

        dx = (b-a)/4
        xi = [a, xc - dx, xc, xc + dx, b]
        fi = [fa, function(xi[1], f_par_a, f_par_b, f_par_c), fc, function(xi[3], f_par_a, f_par_b, f_par_c), fb]
        c = c+2
        fm = min(fi)
        index = fi.index(fm)
        xm = xi[index]
        iterate = dx

    print("Xm = " + str(xm) + " Fm = " + str(fm) + " Iterator = " + str(iterator) +
          " Tau = " + str(tau) + " C = " + str(c))

