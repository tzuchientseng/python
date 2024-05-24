list = {'滷肉飯': 40,
     '爌肉飯': 65,
     '大滷麵': 45,
     "餛飩麵": 70
    }

print('滷肉飯一碗', list['滷肉飯'], '元')
print('爌肉飯一碗', list['爌肉飯'], '元')
print('大滷麵一碗', list['大滷麵'], '元')
print('餛飩麵一碗', list['餛飩麵'], '元')

list["牛肉麵"] = 120

del list['大滷麵']
list.pop('爌肉飯')
_tuple = list.popitem()
print(_tuple)
print(list)
print

print("-"*7, 'demo', "-"*7)
x = {'滷肉飯':40, '爌肉飯':65}
y = {'大滷麵':45, "餛飩麵":70, '爌肉飯':90}
z = {**x, **y}
print(z)


print("-"*7, 'demo', "-"*7)
x = {'滷肉飯':40, '爌肉飯':65, '大滷麵':45}

y = sorted(x.items(), key=lambda item:item[1])
print(y)

print("-"*7, 'demo', "-"*7)
武力 = {'關羽':98, '張遼':96, '周瑜':72, '數學':31, '郭嘉':42}
智力 = {'關羽':85, '張遼':83, '周瑜':99, '數學':97, '郭嘉':98}

_武力 = sorted(武力.items(), key=lambda item:item[1])
_智力 = sorted(智力.items(), key=lambda item:item[1])

print("武將排名依武力由低到高:")
for i,j in _武力:
    print(i,j)

print("武將排名依智力由低到高:")
for i,j in _智力:
    print(i,j)
"""
from operator import itemgetter

def print_sorted(items, title, attribute):
    print(f"武將排名依{attribute}由低到高:")
    for name, value in sorted(items, key=itemgetter(1)):
        print(name, value)

武力 = {'關羽': 98, '張遼': 96, '周瑜': 72, '數學': 31, '郭嘉': 42}
智力 = {'關羽': 85, '張遼': 83, '周瑜': 99, '數學': 97, '郭嘉': 98}

print_sorted(武力.items(), "武將", "武力")
print_sorted(智力.items(), "武將", "智力")
"""

print("-"*7, 'demo', "-"*7)
# Define the inventory with quantities and prices
inventory_details = {'Pen': [12, 50, 600], 'CorrectionTape': [35, 60, 2100]}

# Loop through the items in the inventory to display their details
for item, details in inventory_details.items():
    print(item, 'details (type, quantity, amount) in order:')
    for detail in details:
        print(detail)

print('---------------------------------')

# Define the inventory with a detailed structure
detailed_inventory = {
    'Pen': {'UnitPrice': 12, 'Stock': 50, 'Amount': 600},
    'CorrectionTape': {'UnitPrice': 35, 'Stock': 60, 'Amount': 2100}
}

# Loop through the items in the detailed inventory to display their properties
for category, properties in detailed_inventory.items():
    print("Category", category, 'details as follows:')
    for property_name, value in properties.items():
        print(property_name, value)
