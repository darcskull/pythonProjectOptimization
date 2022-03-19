from FibonacciRecursion import fibonacci
from Function import function


def fibonacci_function(a, b):
    eps = 0.2
    n = 1
    fn = fibonacci(n)
    while fn < (b-a)/eps:
        n = n+1
        fn = fibonacci(n)

    print("Число на Фибоначи : " + str(fn) + " n = " + str(n))
    print("Грешка: " + str(eps))
    print("а = " + str(a) + " b = " + str(b))
    d = b - a
    for k in range(1, n):
        d = (d*fibonacci(n-k))/fibonacci(n-k+1)
        x1 = b-d
        x2 = a+d
        if function(x1) <= function(x2):
            b = x2
        else:
            a = x1

        print("а = " + str(a) + " b = " + str(b))


