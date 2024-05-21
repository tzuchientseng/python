_list = [23, 56, 71, 80, 63, 62, 19, 88, 92, 49, 35]

area1 = 0 #From 0 ~ 30
area2 = 0 #From 31 ~ 60
area3 = 0 #From 61 ~ 99

for i in _list:
    try:
        if i <= 30:
            area1 += 1
        elif i <= 60 and i > 30:
            area2 += 1
        elif i <= 99:
            area3 += 1
        else:
            raise ValueError("Number out of range")
    except ValueError as e:
        print("Warning:", e)
    finally: 
        pass
print("00 ~ 30:", area1)
print("31 ~ 60:", area2)
print("61 ~ 99:", area3)

_list = [23, 56, 71, 80, 63, 62, 19, 88, 92, 49, 35]

# Count occurrences in each range
area1 = sum(1 for i in _list if i <= 30)
area2 = sum(1 for i in _list if 31 <= i <= 60)
area3 = sum(1 for i in _list if 61 <= i <= 99)

# Alternatively, you can use set operations
area1_set = sum(1 for i in set(_list) & set(range(0, 31)))
area2_set = sum(1 for i in set(_list) & set(range(31, 61)))
area3_set = sum(1 for i in set(_list) & set(range(61, 100)))

print("00 ~ 30:", area1)
print("31 ~ 60:", area2)
print("61 ~ 99:", area3)

print("00 ~ 30 (set):", area1_set)
print("31 ~ 60 (set):", area2_set)
print("61 ~ 99 (set):", area3_set)

word = 'deepmind'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
alphabetCount = {alphabet: word.count(alphabet) for alphabet in set(word)} #較快
print(alphabetCount)