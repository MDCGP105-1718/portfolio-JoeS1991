def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#print(fib(8))

for i in range (0, 20):
    print(fib(i))
