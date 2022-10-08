# WAP to display simple interest

p = int(input("Enter principle amount:"))
t = float(input("Enter time period:"))
r = float(input("Enter rate of interest:"))

si = p*t*r/100

print("Simple Interest:", si)
print("Total amount:", p+si)
