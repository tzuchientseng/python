print("HI~ Today is the second lesson of the Python!")


# x = input() #Return String
# y = int(x)

y = int(input("Enter the Grade:"))

if y>=80 and y<=100:
    print("Excellent")
elif y>=60 and y<80:
    print("Pass")
else:
    print("Fail")

# 可以這樣寫
if y>=80:
    print("Excellent")
elif y>=60:
    print("Pass")
else:
    print("Faild")