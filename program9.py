# WAP to check if a no is odd or even. If it is even display its square else display its cube

num = int(input("Enter a number:"))

if (num % 2) == 0:
    print("It is even number")
    print(num**2)

else:
    print("It is odd number")
    print(num**3)