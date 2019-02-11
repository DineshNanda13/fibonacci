def fibonacci(n):
    a = 0
    b = 1

    counter = 0
    while counter < n:
        tmp = a + b
        a = b
        b = tmp
        counter += 1
    return a

print(fibonacci(7))
