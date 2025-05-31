import random

def generate_random_number():
    random_number = random.randint(0,100)
    return random_number

ans = generate_random_number()

while(True): 
    num = int(input("Select the number between 1 to 100: \n"))
    if num>ans:
        print("Too big!")
    elif num<ans:
        print("Too small!")
    else:
        break
print("Congratulation!! The number is", num)
