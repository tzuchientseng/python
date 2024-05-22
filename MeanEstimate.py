import numpy as np
import sys
sys.path.append('my_project_module')
# from scipy import stats


from my_project_module.statistic import * 

print("-----------------Descriptive Statistics (Estimate \u03BC)-----------------")
data = [470, 493, 289, 482, 355, 467, 447, 399, 502, 368]
object = DesData(data)
confidence_level = 95

lower, upper = object.bound(90)
print(f"The mean (\u03BC) estimate (\u03C3 unknown): [{lower:.2f}, {upper:.2f}]")

print("-----------------END-----------------")