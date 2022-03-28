def fibonacci_optimization(n):
    arr = []
    arr.insert(0, 0)
    arr.insert(1, 1)
    for x in range(n-1):
        temp = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = temp

    return arr
