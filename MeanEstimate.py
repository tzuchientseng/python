import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append('my_project_module')
# from scipy import stats

from my_project_module.statistic import * 

print("-----------------descriptive statistics (estimate \u03bc)-----------------")
data = [470, 493, 289, 482, 355, 467, 447, 399, 502, 368]
plt.plot(data, '-o', label="price", lw=7)
plt.title("statistic")
plt.xlabel("x")
plt.ylabel("y")
plt.axis([0, len(data), 0, max(data)+100])
plt.grid()
plt.legend(loc="best")
plt.show()

object = DesData(data)
confidence_level = 95

lower, upper = object.bound(90)
print(f"the mean (\u03bc) estimate (\u03c3 unknown): [{lower:.2f}, {upper:.2f}]")

print("-----------------end-----------------")
print("----------------------------------------", 'demo', "-"*40)
