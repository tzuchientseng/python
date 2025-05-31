# 獲取使用者輸入貸款金額、貸款年限和年利率
loan = eval(input("請輸入貸款金額："))
year = eval(input("請輸入貸款年限："))
rate = eval(input("請輸入年利率（百分比）："))

# 將年利率轉換為月利率
monthrate = rate / (12 * 100)

# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator

# 計算總共還款金額
totalPay = monthlyPay * year * 12

# 打印結果
print(f"每月還款金額: {int(monthlyPay)}")
print(f"總共還款金額: {int(totalPay)}")

print("="*40)
money = 5000
rate = 0.015
n=5
for i in range(n):
    money *= (1 + rate)
    print(f"第{i+1}年本金和 : {int(money)}")