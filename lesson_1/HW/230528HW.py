print("----------------------------------------", 'demo-HW', "-"*40)
import matplotlib.pyplot as plt
data = [60,10,40,80,80,30,60,90,50,60,\
        70,20,40,40,70,80,90,20,30,30,\
        60,50,80,10,40,20,80,80,80,20,\
        60,70,20,30,80,90,90,80,70,80]
A, B, C = [], [], []

for i in data:
    if i <= 59:
        A.append(i) 
    elif i >= 60 and i <=79:
        B.append(i)
    else:
        C.append(i)
area = ['A', 'B', 'C']  
rate = [len(A)/len(data), len(B)/len(data), len(C)/len(data)]
plt.pie(rate, labels=area, autopct='%1.1f%%')
plt.show()

print("----------------------------------------", 'demo-HW', "-"*40)
import numpy as np
# (number & 1) == 0
def medi(list):
    if len(list) & 1 == 0: #even
        temp = sorted(list, reverse=False) 
        n1 = int(len(temp)/2)
        n2 = int(len(temp)/2 - 1)
        return (temp[n1] + temp[n2])/2
    else:
        temp = sorted(list, reverse=False) 
        n = int(len(temp)/2)
        return temp[n]
list = [4, 5, 2, 7]
print(medi(list))
print(np.median(list))
