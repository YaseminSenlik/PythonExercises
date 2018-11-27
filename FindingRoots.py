#our equations with two unknown is ax^2+bx+c

a=int(input("Please enter a number: "))
b=int(input("Please enter a number: "))
c=int(input("Please enter a number: "))

delta=(b**2)-(4*a*c)
root1=(-b-(delta**0.5))/(2*a)
root2=(-b+(delta**0.5))/(2*a)

print("Root1 is {}\nRoot2 is {}\n ".format(root1,root2))