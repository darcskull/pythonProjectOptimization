from Function import function


def golden_section(a, b):
    d = b-a
    eps = 0.2
    print("а = " + str(a) + " b = " + str(b))
    print("Грешка: " + str(eps))
    while b-a > eps:
        d = d*0.618
        x1 = b-d
        x2 = a+d
        if function(x1) <= function(x2):
            b = x2
        else:
            a = x1

        print("а = " + str(a) + " b = " + str(b))

