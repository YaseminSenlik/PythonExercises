midterm1=float(input("Enter your first midterm: "))
midterm2=float(input("Enter your second midterm: "))
final=float(input("Enter your final exam: "))

grade=(midterm1*0.3)+(midterm2*0.3)+(final*0.4)

if(grade>=90):
    print("AA")
elif(grade>=85):
    print("BA")
elif(grade>=75):
    print("BB")
elif(grade>=65):
    print("CB")
elif(grade>=55):
    print("CC")
elif(grade>=45):
    print("DC")
else:
    print("Failed!")