radius = float(input("Enter the radius of the circle(cm):\n"))

circumference = radius*2*3.14
area = radius**2*3.14

print("Circumference is %.2fcm" %(circumference), end=" ")
print("Area is %.2fcm^2"%(area))

print("----next----")

Celsius = float(input("Enter Celsius\n"))
Fahrenheit = Celsius*9/5 +32

print("Celsius:{0:.2f}; Fahrenheit:{1:.2f}".format(Celsius,Fahrenheit))
print(f"Celsius:{Celsius:.2f}; Fahrenheit:{Fahrenheit: .2f}")