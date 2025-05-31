"""
第一題
"""
_list = ["蘋果", "芭樂", "香蕉", "西瓜"]
for i, j in enumerate(_list, 1):
    print(f"{i}:{j}")
"""
第二題
"""
# Define column titles and an empty table
column_titles = ['Product', 'Unit Price', 'Quantity', 'Subtotal']
table = []

index = 1
while True:
    respond = input("Are there any products to input? (y/n): ")
    if respond.lower() == 'n':
        break
    
    # Ask and record product information
    price = int(input(f"Please enter the unit price for Product {index}:\n"))
    num = int(input(f"Please enter the quantity for Product {index}:\n"))
    table.append(['Product ' + str(index), price, num, price * num])
    
    index += 1

# Output the table
print(column_titles)
for row in table:
    print(row)

"""
第三題
"""
higher_temper = (32, 34, 31, 29, 33, 35, 30)
lower_temper = (25, 23, 26, 26, 24, 24, 25)
print(higher_temper)
print(lower_temper)

print("當周最高溫:", max(higher_temper))
print("當周最低溫:", min(lower_temper))
print("最高溫平均:", round(sum(higher_temper)/len(higher_temper),2))
print(f"最低溫平均:{sum(lower_temper)/len(lower_temper):1.1f}")

"""
第四題
"""
_higher_temper = list(higher_temper)
_lower_temper = list(lower_temper)
_higher_temper[5] = 36
_lower_temper[1] = 25
higher_temper = tuple(_higher_temper)
lower_temper = tuple(_lower_temper)
print("修正後當周最高溫:", max(higher_temper))
print("修正後當周最低溫:", min(lower_temper))
print("修正後最高溫平均:", round(sum(higher_temper)/len(higher_temper),2))
print(f"修正後最低溫平均:{sum(lower_temper)/len(lower_temper):1.1f}")