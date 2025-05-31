import random

print("-"*40, 'SORT', "-"*40)
list = [random.randint(1,100) for _ in range(10)]
print(f"Original list:{list}")

sorted_list = sorted(list, reverse=False)
print(f"Sorted:{sorted_list}")

list.sort(reverse=False)
print(f"Sort:{list}")

print("-"*40, 'REVERSE', "-"*40)
print("--Immutable--")
list2 = [random.randint(1,100) for _ in range(10)]
reversed_list = list2[::-1]
print(f"Before:{list}.\nReverse after:{reversed_list}")

print("--Mutable--")
list3 = [random.randint(1,100) for _ in range(10)]
print(f"Before:{list3}")
list3.reverse()
print(f"After:{list3}")
