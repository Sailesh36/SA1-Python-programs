# WAP to take input of year and check if it is a leap year

yr = int(input("Enter the year:"))

# leap years occur every four years so obviously lead year is divisible by 4 so i used this
if yr % 4 == 0:
    print("It is a leap year")

else:
    print("It is not a leap year")
