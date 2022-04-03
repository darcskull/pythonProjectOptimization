def fibonacci_iterative(n):
    arr = []
    arr.insert(0, 1)
    arr.insert(1, 1)
    for x in range(2, n+1):
        arr.insert(x, arr[x - 2] + arr[x - 1])

    return arr
