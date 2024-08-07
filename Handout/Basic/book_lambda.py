# demo 1
print("----------------------------------------", 'demo', "-"*40)
"""
// 定義一個函數式介面
interface MyFunction {
    int apply(int x);
}
public class Main {
    public static void main(String[] args) {
        // 使用 Lambda 表達式創建 MyFunction 介面的實例
        MyFunction square = (int x) -> x * x;

        // 調用 apply 方法計算平方
        System.out.println(square.apply(4)); // 輸出 16
    }
}
"""
def square(x):
    value  = x ** 2
    return value
print(square(10))
#lambda
square = lambda x: x ** 2
print(square(4))
sqrt = lambda x: x ** 0.5
print(sqrt(16))

# demo 2
print("----------------------------------------", 'demo', "-"*40)
"""
import java.util.function.*;
public class Main {
    public static void main(String[] args) {
        // 使用Lambda表達式實現加法
        BinaryOperator<Integer> add = (a, b) -> a + b;
        System.out.println("加法結果：" + add.apply(5, 3));

        // 使用Lambda表達式實現乘法
        BinaryOperator<Integer> multiply = (a, b) -> a * b;
        System.out.println("乘法結果：" + multiply.apply(5, 3));

        // 使用Lambda表達式實現最大值比較
        BinaryOperator<Integer> max = BinaryOperator.maxBy((a, b) -> a - b);
        System.out.println("最大值：" + max.apply(5, 3));

        // 使用Lambda表達式實現字串連接
        BinaryOperator<String> concat = (a, b) -> a + b;
        System.out.println("連接結果：" + concat.apply("Hello ", "world"));
    }
}
"""
product = lambda x, y: x*y
print(product(5, 10))

# demo 3
print("----------------------------------------", 'demo', "-"*40)
"""
    import java.util.function.Function;
    public class Main {
        public static void main(String[] args) {
            Function<Integer, Integer> linear = func(5);
            System.out.println(linear.apply(10));
        }

        public static Function<Integer, Integer> func(int b) {
            return x -> 2 * x + b;
        }
    }
"""
def func(b):
    return lambda x: 2 * x + b
linear = func(5)
print(linear(10))
linear2 = func(4)
print(linear2(4))

# demo 4 (Higher-order function)
print("----------------------------------------", 'demo', "-"*40)
def mycar(cars, func):  #(list, function)
    for car in cars:
        print(func(car))

def wdcar(carbrand):
    return "My dream car is " + carbrand.title()
dreamcars = ['porsche', 'roolls royce', 'maserati']
mycar(dreamcars, wdcar)

# lambda
print("----------------------------------------", 'demo', "-"*40)
def mycar(cars, func):  #(list, function)
    for car in cars:
        print(func(car))
dreamcars = ['porsche', 'roolls royce', 'maserati']
mycar(dreamcars, lambda carbrand: "My dream car is " + carbrand.title())

# demo 5 (filter)
print("----------------------------------------", 'demo', "-"*40)
def oddfn(x):
    return x if (x % 2 == 1) else None
myList = [5, 10, 15, 20 , 25, 30]
filter_object = filter(oddfn, myList)
print("The odd index in list: ", [item for item in filter_object])
print([n for n in myList if n % 2 == 1])
print([n for n in filter_object]) #n for n 只能迭代(iterate)一次 因此輸出空集合

# lambda
print("----------------------------------------", 'demo', "-"*40)
myList = [598, 103, 215, 204 , 235, 430]

print("The odd index in list: ", list(filter(lambda x : (x % 2 == 1), myList)))

# demo 6 (map())
print("----------------------------------------", 'demo', "-"*40)
# x, y = map(int, input().split()) #map(func, iterable)
myList = [598, 103, 215, 204 , 235, 430]
squareList = list(map(lambda x : x ** 2, myList))
print("The squareList: ", squareList)

# demo 7 (reduce())
print("----------------------------------------", 'demo', "-"*40)
from functools import reduce

from numpy import integer
def multiply(x, y):
    """
        Time complexity: O(n), Space complexity O(1)。
    """
    return x * y
numbers = [1, 2, 3, 4, 5]
# 使用 reduce() 函式計算累積乘積
result = reduce(multiply, numbers)
print(result)  # 輸出 120 (1 * 2 * 3 * 4 * 5)

print("----------------------------------------", 'demo', "-"*40)
# string to integer
def strToInt(s):
    def func(x, y):
        return 10*x + y
    def charToNum(s):
        print("s = ", type(s), s)
        mydict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
        n = mydict[s]
        print("n = ", type(n), n)
        return n 
    return reduce(func, map(charToNum,s))
string = '5487'
x = strToInt(string) + 10
print("x + 10 =", x)

# lambda
print("----------------------------------------", 'demo', "-"*40)
def strToInt(s):
    def charToNum(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }[s]
    return reduce(lambda x, y : (10*x +y), map(charToNum,s))
string = '5487'
x = strToInt(string) + 10
print("x + 10 =", x)

# demo 8 (len())
print("----------------------------------------", 'demo', "-"*40)

strs = ['abc', 'ab', 'abcde']
# str_len = lambda x:len(x)
# print([str_len(e) for e in strs])
print("The length:", [(lambda x: len(x))(i) for i in strs])
# print([lambda x:len(x)(i) for i in strs]) #不能這樣寫進去 lambda 需要先呼叫(); print((lambda x: len(x))('abc')) 不能print(lambda x:len(x)('abc'))

# demo 9 (sorted())
print("----------------------------------------", 'demo', "-"*40)
"""
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// 使用 Lambda 表達式對字串列表進行排序
Collections.sort(names, (a, b) -> a.compareTo(b));

// 輸出排序後的列表
names.forEach(System.out::println);
"""
sc = [['Johhn', 80], ['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x: x[1], reverse="True") #返回值是None
print(sc)
print(sorted(sc, key = lambda x: x[1], reverse="True"))
