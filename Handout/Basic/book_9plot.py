"""
pip install matplotlib
"""
print("----------------------------------------", 'Test-matplotlib.pyplot', "-"*40)
print("----------------------------------------", 'Test-plot()', "-"*40)
"""
plot(x, y, lw=x, ls='x', label='xxx', color) #line width and line style
"""
import matplotlib.pyplot as plt
x = [x for x in range(9)]
squares = [y**2 for y in range(9)]
plt.plot(x, squares)
plt.show()

print("----------------------------------------", 'Test-axis()', "-"*40)
import matplotlib.pyplot as plt
squares = [n**2 for n in range(7)]
plt.plot(squares)
plt.axis(0, 8, 0, 70) #[xmin, xmax, ymin, ymax]
plt.show()
print("----------------------------------------", 'Test-grid()', "-"*40)
plt.grid(True)
print("----------------------------------------", 'Test-title(), xlabel(), ylabel()', "-"*40)
plt.title('name', fontsize=24)
plt.xlabel('name', fontsize=17)
plt.ylabel('name', fontsize=17)

print("----------------------------------------", 'Test-tick_params()', "-"*40)
plt.tick_params(axis='both', labelsize=12, color='red')

print("----------------------------------------", 'Test-mutiple data', "-"*40)
print("----------------------------------------", 'Test-legend()', "-"*40)
import matplotlib.pyplot as plt
data1 = [n*n for n in range(50)]
data2 = [25*n for n in range(50)]
seq = [n for n in range(50)]
# plt.plot(seq, data1, seq, data2)
# plt.plot(seq, data1, seq, data2, label='data1', label='data2') #不能和再一起寫
plt.plot(seq, data1, label='data1')
plt.plot(seq, data2, label='data2')
plt.legend(loc='best')
plt.title('Test chart', fontsize=24)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tick_params(axis='both', which='both', labelsize=12, color='red')
plt.show()

print("----------------------------------------", 'Test-savefig()', "-"*40)
"""
plt.savefig('fileName.jpg')
"""

print("----------------------------------------", 'Test-imread()', "-"*40)
import matplotlib.pyplot as plt
import matplotlib.image as img
fig = img.imread('XXX.jpg')
plt.imshow('fig')

print("----------------------------------------", 'Test-scatter()', "-"*40)
import matplotlib.pyplot as plt
xpt = list(range(1,101))
ypt = [x**2 for x in xpt]
plt.scatter(xpt, ypt, color='y')
plt.show()

print("----------------------------------------", 'Test', "-"*40)
