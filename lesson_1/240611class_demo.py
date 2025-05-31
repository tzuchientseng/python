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
