print("----------------------------------------", 'demo-class', "-"*40)
class Student():
    Studentname = "Sunny"
    def order(self):
        return 'nice'

x = Student()
print(x.Studentname, x.order())

print("----------------------------------------", 'demo-class', "-"*40)
class School():
    Studentname = "Sunny"
    def __init__(self, name, score) -> None:
        self.name = name
        self.__score =score
    def get_name(self):
        return self.name
    def get_score(self):
        return self.__score

x = School('Sunny', 100) 
print(x.get_name(), "\'s Score: ", x.get_score())

print("----------------------------------------", 'demo', "-"*40)
class Bank:
    bankname = "銀行"
    
    def __init__(self, name):
        self.name = name
        self.money = 0
        
    def deposit(self, amount):
        self.money += amount
        print(f"{self.name} 存入 {amount}, 完成")
        
    def withdraw(self, amount):
        if amount > self.money:
            print(f"{self.name} 餘額不足, 未完成")
            print(f"{self.name} 餘額 {self.money}")
        else:
            self.money -= amount
            print(f"{self.name} 取出 {amount}, 完成")
        
    def balance(self):
        print(f"{self.name} 餘額 {self.money}")

x = Bank("Sunny")
x.deposit(2000)
x.balance()
x.withdraw(1200)
x.balance()
x.withdraw(2000)
x.balance()

print("----------------------------------------", 'demo', "-"*40)
class Bank:
    bankname = "銀行"
    
    def __init__(self, name):
        self._name = name
        self._money = 0
        
    def deposit(self, amount):
        self._money += amount
        print(f"{self._name} 存入 {amount}, 完成")
        
    def withdraw(self, amount):
        if amount > self._money:
            print(f"{self._name} 餘額不足, 取出 未完成")
            print(f"{self._name} 餘額 {self._money}")
        else:
            self._money -= amount
            print(f"{self._name} 取出 {amount}, 完成")
        
    def balance(self):
        print(f"{self._name} 餘額 {self._money}")

class newBank(Bank):
    def transfer(self, x):
        y = int(x / 35)
        print(f"新台幣 {x} 換匯美金 {y} 元")

x = newBank("Sunny")
x.deposit(3000)
x.balance()
x.withdraw(1800)
x.balance()
x.deposit(7000)
x.balance()
x.transfer(35000)

print("----------------------------------------", 'demo', "-"*40)
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)

# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={'projection': '3d'})

# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")  # cmap設置顏色新層為 藍-白-紅
ax[0].set_title('Draw curve surface plot', fontsize=7, color='gray')

# 繪製曲線框線圖
ax[1].plot_wireframe(X, Y, Z, color='g')
ax[1].set_title('Draw curve frame line drawing', fontsize=7, color='gray')

plt.show()

print("----------------------------------------", 'demo', "-"*40)
