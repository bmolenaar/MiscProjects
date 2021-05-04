import time

fib1 = 0
fib2 = 1

while True:
    start = fib1 + fib2
    fib1 = fib2
    fib2 = start
    print(start)
    time.sleep(1)