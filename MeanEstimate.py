import sys
import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats

# Append the project module path
sys.path.append('my_project_module')
from my_project_module.statistic import DesData

print("-----------------descriptive statistics (estimate \u03bc)-----------------")
data = [470, 493, 289, 482, 355, 467, 447, 399, 502, 368]
day = [ _ for _ in range(1, len(data) + 1)]

# Create DesData object and calculate confidence interval
object = DesData(data)
confidence_level = 95
lower, upper = object.bound(90)
text_str = f"the mean (\u03bc) estimate (\u03c3 unknown): [{lower:.2f}, {upper:.2f}]"
print(text_str)

# Plotting data
plt.figure(figsize=(12, 6))
plt.plot(day, data, 'r-o', lw=2, label="price")

# Add legend
plt.legend(loc="best")

# Add titles and labels
plt.title("Statistics Over Time", fontsize=18)
plt.xlabel("Day", fontsize=14)
plt.ylabel("Price", fontsize=14)

# Customize ticks
plt.xticks(day, fontsize=12)
plt.yticks(fontsize=12)
plt.tick_params(axis='both', colors='black')

# Adjust axis limits dynamically
plt.axis([0, max(day) + 1, 0, max(data) + 100])

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Add annotation text
plt.text(0.5, 0.1, text_str, transform=plt.gca().transAxes, fontsize=12, 
         verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Show the plot
plt.show()

print("-----------------end-----------------")
print("----------------------------------------", 'demo', "-"*40)
