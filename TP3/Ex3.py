import random


def Guess():
    i = 1
    b = 0
    n = random.randint(0, 100)
    searching = True
    while searching:
        a = int(input("your guess : "))
        b += 1
        if a == n:
            print("Good Job ! in ", b, "attempt(s)")
            return i
        if a > n:
            print("less")
        else:
            print("more")
        i += 1
Guess()