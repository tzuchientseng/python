a, b, c, d, e = eval(input("Enter five Number:\n"))
list = [a, b, c, d, e]
print(f"The list is {list}\n")

Tsorted = sorted(list, reverse=True)
print(Tsorted)

Fsorted = sorted(list, reverse=False)
print(Fsorted)

print("The maximum score:", max(Tsorted))
print("The minimum score:", min(Tsorted))
print("The sum:", sum(Tsorted))
print("Average:", sum(Tsorted)/len(Tsorted))

list = [6, 7, 7, 8, 98]
print([_ + 3 for _ in list])