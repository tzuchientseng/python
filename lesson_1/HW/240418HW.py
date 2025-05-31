while(True):
    price = 100.0
    ages = int(input("Enter your ages:"))
    if ages>=80 or ages<=6:
        print("The price = ", price*0.5)
    elif ages>=60 or ages<=12:
        print("The price = ", price*0.8)
    else:
        print("The price", price)