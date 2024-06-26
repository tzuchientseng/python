class Banks():
    '''基本银行系统'''
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__title = "Taipei Bank"
    
    def save_money(self, money):
        self.__balance += money
        print("存钱 ", money, " 完成")
    
    def withdraw_money(self, money):
        self.__balance -= money
        print("提款 ", money, " 完成")
    
    def get_balance(self):
        print(self.__name.title(), " 目前餘額: ", self.__balance)
    
    def bank_title(self):
        return self.__title

class Shilin_Banks(Banks):
    '''士林银行分行'''
    def __init__(self, uname):
        self.__title = "Taipei Bank - Shilin Branch"
    
    def bank_title(self):
        return self.__title
