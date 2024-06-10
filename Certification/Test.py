print("----------------------------------------", 'Test1', "-"*40)
# a, b, c, d = map(float, input("Input four Number space to seperat: \n").split(" "))
# a, b, c, d = input().split(" ")
a, b, c, d = 23.12, 395.3, 100.4617, 564.329

print(f"|{a:7.2f} {b:7.2f}|")
print(f"|{c:7.2f} {d:7.2f}|")
print(f"|{a:<7.2f} {b:<7.2f}|")
print(f"|{c:<7.2f} {d:<7.2f}|")

print("|{:7.2f} {:7.2f}|".format(a, b))
print("|{:7.2f} {:7.2f}|".format(c, d))
print("|{:<7.2f} {:<7.2f}|".format(a, b))
print("|{:<7.2f} {:<7.2f}|".format(c, d))

print("|%7.2f %7.2f|" % (a, b))
print("|%7.2f %7.2f|" % (c, d))
print("|%-7.2f %-7.2f|" % (a, b))
print("|%-7.2f %-7.2f|" % (c, d))

print("----------------------------------------", 'Test2', "-"*40)
x = 345345333424243*15
if x % 15 == 0:
    print("x is multuple of 3 and 5")
elif x % 3 == 0:
    print("x is multuple of 3")
elif  x % 5 == 0:
    print("x is multuple of 5")
else:
    print("x is not multuple of 3 or 5")

print("----------------------------------------", 'Test3', "-"*40)
# a, b = map(int, input("Input two Number(a>b) space to seperat: \n").split(" "))
a, b = 14, 1144

#Method 1
sum_ = sum(n for n in range(a, b+1) if n % 2 == 0)

#Method 2
sum_ = 0
for _ in range(a, b+1):
    sum_ += _ if _ % 2 == 0 else 0

print("Sum:", sum_)

print("----------------------------------------", 'Test4', "-"*40)
list_ = []
while True:
    num = int(input("Enter 9999 to stop loop:\n"))
    list_.append(num)
    if num == 9999:
        print("The minimum number: ", min(list_))
        break

"""
list_ = []
while True:
    try:
        num = int(input("Enter 9999 to stop loop:\n"))
        if num == 9999:
            if list_:  # 確保列表中有數據
                print("The minimum number: ", min(list_))
            else:
                print("No numbers were entered.")
            break
        else:
            list_.append(num)
    except ValueError:
        print("Please enter a valid integer.")
"""

print("----------------------------------------", 'Test5', "-"*40)
def compute(x, y):
    return x * y
a, b = map(int, input("Enter two number, use space to seperate.\n").split(" "))
print(f"{a}*{b} = {compute(a,b)}")

print("----------------------------------------", 'Test6', "-"*40)
list_ = list(map(str, input("Select five cards of deck(num), use space to seperate.\n").split(" ")))


"""
list_ = list(map(str, input("Select five cards of deck(num), use space to seperate.\n").split(" ")))
valid_cards = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'J', 'j', 'Q', 'q', 'K', 'k'}
if not all(card in valid_cards for card in list_):
    print("Invalid input")
"""
