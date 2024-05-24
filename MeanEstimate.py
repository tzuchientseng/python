import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append('my_project_module')
# from scipy import stats

from my_project_module.statistic import * 

print("-----------------descriptive statistics (estimate \u03bc)-----------------")
data = [470, 493, 289, 482, 355, 467, 447, 399, 502, 368]

object = DesData(data)
confidence_level = 95

lower, upper = object.bound(90)
text_str = f"the mean (\u03bc) estimate (\u03c3 unknown): [{lower:.2f}, {upper:.2f}]"
print(text_str)

plt.plot(data, 'r-o', label="price", lw=7)
plt.legend(loc="best")

plt.title("statistic")
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.axis([0, len(data), 0, max(data)+100])
plt.grid()
plt.text(0.5, 0.1, text_str, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

plt.show()
print("-----------------end-----------------")
print("----------------------------------------", 'demo', "-"*40)

