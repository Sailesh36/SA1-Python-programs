# WAP to find compound interest
#this is also a bit complicated but not out of topic so im doing this
# if u dont understand follow this link: https://www.geeksforgeeks.org/python-program-for-compound-interest/

p = int(input("Enter principle amount:"))
t = float(input("Enter time period:"))
r = float(input("Enter rate of interest:"))

a = p*(1+(r/100))**t
ci = a-p

print("Compound Interst is:", ci)
print("Total amount:", a)