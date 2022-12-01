def Fact():
    n = int(input("Please, enter a integer : "))
    if input("Do you want to see for or while?  : ") == "for":
        s = 1
        for i in range(2, n + 1):
            s *= i
            print(s)
        print("The Factorial is", s, "with for")
    else:
        s = 1
        while n > 1:
            s *= n
            print(s)
            n -= 1
        print("The Factorial is", s, "with for")
Fact()