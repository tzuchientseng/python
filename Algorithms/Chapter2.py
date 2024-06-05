print("----------------------------------------", 'demo-array', "-"*40)
from array import*
x = array('i', [5,15,25,35,45])
for data in x:
    print(data, end=" ")
print()
print('x[3]:', x[3])

print("----------------------------------------", 'demo-insert(i, x)', "-"*40)
from array import*
x = array('i', [5,15,25,35,45])
x.insert(2, 100)
print(x) #ouput: array('i', [5, 15, 100, 25, 35, 45])

print("----------------------------------------", 'demo-append(x) (append at last)', "-"*40)
x.append(100)
print(x)

print("----------------------------------------", 'demo-remove(value)', "-"*40)
x.remove(x[5])
print(x)

print("----------------------------------------", 'demo-pop(index)|default: i=-1', "-"*40)
print(x)
_pop = x.pop()
print("Pop out: ", _pop)
print(x)
_pop2 = x.pop(4)
print("Pop out: ", _pop2)
print(x)

print("----------------------------------------", 'demo-index(value)to find value', "-"*40)
i = x.index(x[1])
print("x[1]=", i)

print("========================================", 'Practice', "="*40)
from array import*
_array = array('f', [1,2,5,6,7])
print(_array)
index = int(input('Pop the index of [1,2,5,6,7]:\n'))
if index > 0 and index < len(_array):
    _array.pop(index)
else:
    print("Out of range!.") 
print(_array)

index = int(input('Insert the index of [1,2,5,6,7]:\n'))
if index > 0 and index < len(_array):
    value = int(input('Enter the value:\n'))
    _array.insert(index, value)
else:
    print("Out of range!.") 
print(_array)
