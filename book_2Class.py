# demo 1
"""
public class Banks {
    // 定義銀行類別
    static String bankname = "台北銀行";

    // 銀行的座右銘
    public static String motto() {
        return "以客為尊";
    }

    public static void main(String[] args) {
        Banks userbank = new Banks();
        System.out.println("目前服務的銀行是：" + userbank.bankname);
        System.out.println("目前服務的理念是：" + motto());
    }
}
"""

print("----------------------------------------", 'demo-class', "-"*40)
class Banks():
    """定義銀行類別"""
    bankname = 'Taipei Bank'
    def motto(self) -> str: #->return type (Tuple)
        return "以客為尊"
userbank = Banks()
print(f"目前服務的銀行是:{userbank.bankname}")
print(f"目前服務的理念是:{userbank.motto()}")

# demo 2
"""
public class Banks {
    // 定義銀行類別
    static String bankname = "Taipei Bank";
    String name;
    double balance;

    // 建構函式
    public Banks(String uname, double money) {
        this.name = uname;
        this.balance = money;
    }

    // 取得餘額方法
    public double getBalance() {
        return this.balance;
    }

    public static void main(String[] args) {
        Banks hungBank = new Banks("hung", 100);
        System.out.println(hungBank.name.substring(0, 1).toUpperCase() + hungBank.name.substring(1) + " 存款餘額: " + hungBank.getBalance());
    }
}
"""
class Banks():
    """定義銀行類別"""
    bankname = 'Taipei Bank'
    # def __init__(self) -> None:
    #     pass
    def __init__(self, uname , money):
        self.name = uname
        self.balance = money        
    def get_balance(self):
        return self.balance
    
hungbank = Banks('hung', 100)
print(hungbank.name.title(), "存款餘額:", hungbank.get_balance())

# demo 3
print("----------------------------------------", 'demo-private_field', "-"*40)
class Banks():
    """定義銀行類別"""
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
    def save_money(self, money):
        self.__balance += money
        print("存款", money, "完成")
    def withdraw_money(self, money):
        self.__balance -= money
        print("提款", money, "完成")
    def get_balance(self):
        print(self.__name.title(), "目前餘額: ", self.__balance)
    # def get_balance(self):
    #     return str(self.__name.title()) + "目前餘額: " + str(self.__balance)
hungank = Banks('hung')
hungank.get_balance()
# hungank.__balance = 100_0000
hungank._Banks__balance = 100_0000
hungank.get_balance()
    
# demo 4
print("----------------------------------------", 'demo-private_method', "-"*40)
class Banks():
    """定義銀行類別"""
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
        self.__rate = 30
        self.__service_charge = 0.1
    def save_money(self, money):
        self.__balance += money
        print("存款", money, "完成")
    def withdraw_money(self, money):
        self.__balance -= money
        print("提款", money, "完成")
    def get_balance(self):
        print(self.__name.title(), "目前餘額: ", self.__balance)
    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result
    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 - self.__service_charge))
hungbank = Banks('hunbg')
usdallor = 50
print(usdallor, "美金可以兌換", hungbank.usa_to_taiwan(usdallor), "台幣")
# hungbank.__cal_rate(50) 
hungbank._Banks__cal_rate(50)

# demo 5
print("----------------------------------------", 'demo-static', "-"*40)
"""
public class MyClass {
    // 類屬性
    static String classAttribute = "我是一個類屬性";

    // 實例屬性
    String instanceAttribute;

    // 建構函式
    public MyClass(String instanceAttribute) {
        this.instanceAttribute = instanceAttribute;
    }

    // 靜態方法
    public static void staticMethod() {
        System.out.println("靜態方法訪問類屬性: " + MyClass.classAttribute);
    }

    // 類方法
    public static void classMethod() {
        System.out.println("類方法訪問類屬性: " + MyClass.classAttribute);
    }

    public static void main(String[] args) {
        // 創建類的實例
        MyClass obj = new MyClass("我是一個實例屬性");

        // 調用靜態方法
        MyClass.staticMethod();

        // 調用類方法
        MyClass.classMethod();
    }
}
"""
class MyClass:
    class_attribute = "我是一個類屬性"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    # 靜態方法可以訪問類屬性
    @staticmethod
    def static_method():
        print("靜態方法訪問類屬性:", MyClass.class_attribute)

    # 類方法可以訪問類屬性
    @classmethod
    def class_method(cls):
        print("類方法訪問類屬性:", cls.class_attribute)
# 創建類的實例
obj = MyClass("我是一個實例屬性")
# 調用靜態方法
MyClass.static_method()
# 調用類方法
MyClass.class_method()

# demo 6
print("----------------------------------------", 'demo-inheritance', "-"*40)
class Father():
    def hometown(self):
        print('我住在埔里')
    def get_postion(self):
        print('Doctor')
class Son(Father):
    def hometown(self):
        print('我住在台中')
    def greet(self):
        print('hi~')
    def get_postion(self):
        print('Engineer')
# Python 沒有 Father people = new Son();
Tseng = Father()
chien = Son()
Tseng.hometown()  
chien.hometown()  
#Tseng.greet() #Father 沒有greeting
chien.greet()
Tseng.get_postion()
chien.get_postion()

# demo 7
print("----------------------------------------", 'demo', "-"*40)
class BanksBASE():
    """定義銀行類別"""
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
        self.__rate = 30
        self.__service_charge = 0.1
    def save_money(self, money):
        self.__balance += money
        print("存款", money, "完成")
    def withdraw_money(self, money):
        self.__balance -= money
        print("提款", money, "完成")
    def get_balance(self):
        print(self.__name.title(), "目前餘額: ", self.__balance)
    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result
    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 - self.__service_charge))
    def bank_title(self):
        return self.__bankname
class Shilin_Banks(BanksBASE):
    pass
hungank = Shilin_Banks('hung')
print("我的存款銀行是: ", hungank.bank_title())

# demo 8
print("----------------------------------------", 'demo-super()', "-"*40)
"""
public class Demo8Super {
    public static void main(String[] args) {
        Animals myCat = new Animals("Lucy", 5);
        System.out.println(myCat.getName() + " is " + myCat.getAge() + " years old.");
        myCat.run();

        Dogs myDog = new Dogs("lily", 6);
        System.out.println(myDog.getName() + " is " + myDog.getAge() + " years old.");
        myDog.run();
    }
}

class Animals {
    private String name;
    private int age;

    public Animals(String animalName, int animalAge) {
        this.name = animalName;
        this.age = animalAge;
    }

    public void run() {
        System.out.println(this.name.substring(0, 1).toUpperCase() + this.name.substring(1) + " is running.");
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }
}

class Dogs extends Animals {
    public Dogs(String dogName, int dogAge) {
        super("My pet " + dogName.substring(0, 1).toUpperCase() + dogName.substring(1), dogAge);
    }
}
"""
class Animals:
    """Animals 基底類別"""
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age
    def run(self):
        print(self.name.title(), " is running.")
class Dogs(Animals):
    """Animals 的衍生類別 Dogs"""
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet '+ dog_name.title(), dog_age)
    def sleeping(self):
        print("My pet is sleeping.")
mycat = Animals('Lucy', 5)
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
mydog.sleeping()

# demo 9
print("----------------------------------------", 'demo-super()', "-"*40)
class Grandfather:
    """Defines grandfather's inheritance"""
    def __init__(self):
        self.grandfathermoney = 1000
        
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):
    """Defines father's inheritance"""
    def __init__(self):
        super().__init__()  # Initialize grandfather's inheritance
        self.fathermoney = 1000
        
    def get_info2(self):
        print("Father's information")
class Sunny(Father):
    """Defines Sunny's inheritance"""
    def __init__(self):
        super().__init__()  # Initialize father's inheritance
        self.sunnymoney = 1000
        
    def get_info3(self):
        print("Asset information")
        print("\nSunny asset:", self.sunnymoney,
              "\nFather asset:", self.fathermoney,
              "\nGrandfather asset:", self.grandfathermoney)

sunny = Sunny()
sunny.get_info3()  # This will print all assets
sunny.get_info2()  # This will print father's information
sunny.get_info1()  # This will print grandfather's information

# demo 10
print("----------------------------------------", 'demo-兄弟類別屬性', "-"*40)
class Father:
    """Defines father's inheritance"""
    def __init__(self):
        self.fathermoney = 10000

class Ira(Father):
    """Defines Ira's inheritance"""
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.iramoney = 8000

class Ivan(Father):
    """Defines Ivan's inheritance"""
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.ivanmoney = 1000

    def get_money(self):
        print("\nIvan asset:", self.ivanmoney,
                "\nFather asset:", self.fathermoney,
                "\nIra asset:", Ira().iramoney)

ivan = Ivan()
ivan.get_money()

# demo 11
print("----------------------------------------", 'demo-self', "-"*40)
class Person():
    def interest(self):
        print("Smiling is my interest")
hung = Person()
hung.interest()
# or
Person.interest(hung)
"""
public class Person {
    public void interest() {
        System.out.println("微笑是我的興趣");
    }
    
    // 靜態方法來模擬呼叫非靜態方法
    public static void interest(Person person) {
        person.interest();
    }

    public static void main(String[] args) {
        Person hung = new Person();
        hung.interest();
        // 或者
        interest(hung);
    }
}
"""