import time


def Countdown():
    n = int(input("Please, enter an integer : "))
    m = n
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(0.2)
    for i in range(m + 1):
        print(m - i)
        time.sleep(0.2)
Countdown()