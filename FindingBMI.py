height=float(input("Enter your height: "))
weight=float(input("Enter your weight: ")) #it is in meter
BMI=weight/(height**2)

if(BMI<18.5):
    print("You are thin")
elif(18.<BMI<25):
    print("You are normal")
elif(25<BMI<30):
    print("You are fat")
elif(BMI>30):
    print("You are obese")
