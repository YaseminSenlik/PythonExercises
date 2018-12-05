a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))

if(a>b):
    if(a>c):
        print("Max number is {}".format(a))
    else:print("Max number is {}".format(c))
else:
    if(b>c):
        print("Max number is {}".format(b))
    else:print("Max number is {}".format(c))
