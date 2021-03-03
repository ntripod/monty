income = float(input("Enter the annual income: "))

#
# Put your code here.
if income <= 85528:
    tax = income * .18
    tax = tax - 556.02
else:
    tax = 14839.02
    surplus = income - 85528
    tax = tax + surplus * .32

#    tax = 14839.02
#    surplus = income - 85528
#    surplustax = surplus * .32
#    tax = tax + surplustax

if tax < 0:
    print("Tax is zero psile")

#if tax < 0
#   tax = 0
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")




