shape=input("Please enter that you want to know: ")

if(shape=="Triangular"):
    a=float(input("Enter first edge: "))
    b=float(input("Enter second edge: "))
    c=float(input("Enter third edge: "))
    if(abs(a+b)>c and abs(a+c)>b and abs(b+c)>a):
        if(a==b and b==c):
            print("This is an equilateral triangle ")
        elif((a==b and b!=c) or (a==c and a!=b) or (b==c and a!=b)):
            print("This is an isosceles triangle ")
        else:print("This is only triangular")
    else:print("it is not triangular")
elif(shape=="Tetragonal"):
    x = float(input("Enter first edge: "))
    y = float(input("Enter second edge: "))
    z = float(input("Enter third edge: "))
    t = float(input("Enter third edge: "))
    if(x==y and x==z and x==t):
        print("This is square")
    elif(x==y and z==t):
        print("This is rectangle")
    else:print("It is only tetragonal")
else:print("Please enter a valid shape")