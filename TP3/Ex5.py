def checkdata(start, end):
    if start<0 or start>24 or end<0 or end>24:
        print("The hours must be between 0 and 24 ! ")
        return False
    if start==end:
        print("Attention! The end time is identical to the start time.")
        return False
    if start>end:
        print("Attention! The beginning of the rent is after the end ...")
        return False
    return True

def velo():
    start = int(input("Give the start time of the rental (an integer): "))
    end = int(input("Give the end time of the rental (an integer): "))
    while not checkdata(start, end):
        start = int(input("Enter the start time of the rental (a whole number) : "))
        end = int(input("Give the end time of the rental (an integer) : "))

    high=0
    low=0

    if end<7:
        low = end - start
    else:
        if start<7:
            low = 7 - start
            start = 7

        if end<17:
            high=2*(end-start)
        else:
            if start<17:
                high=2*(17-start)
                start=17
            low+=end-start

    print("You have rented your bike for")
    if low>0:
        print(low, "hour(s) at the hourly rate of 1.0 euro(s)")
    if high>0:
        print(high//2, "hour(s) at the hourly rate of 2.0 euro(s)")
    print("The total amount to pay is", float(high+low), "euro(s).")

velo()