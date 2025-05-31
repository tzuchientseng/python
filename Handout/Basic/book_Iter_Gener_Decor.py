"""
Iterator
Generator 
Decorator
"""
# demo 1
print("----------------------------------------", 'demo1-iterator', "-"*40)
my_list = [1, 3, 5]
my_iterator = iter(my_list)
print("-------", type(my_iterator), "-------")
print("-------", my_iterator, "-------")
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# demo 2
print("----------------------------------------", 'demo2-Function-Generator yield iterator', "-"*40)
def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x

myiter = iter_data() #很像linkList的結構
print(next(myiter))
print(next(myiter))
print(next(myiter))
# or
myiter = iter_data() #需要再生成一次
for data in myiter:
    print(data)
"""
_iter = (n for n in range(4))
print(next(_iter))
print(next(_iter))
print(next(_iter))
print(next(_iter))
# print(next(_iter)) #報錯
"""

# demo 3
print("----------------------------------------", 'demo3_1-List_Square with listr', "-"*40)
def list_square(n):
    mylist = []
    for data in range(1, n+1):
        mylist.append(data ** 2)
    return mylist
print(list_square(5))
print("-"*4, 'demo3_1-List_Square with list(lambda)', "-"*4)
# ----or----
list_square = lambda n: [data ** 2 for data in range(1, n+1)] #list[]
print(list_square(5))  

print("----------------------------------------", 'demo3_2-List_Square with generatorr', "-"*40)

def iter_square(n):
    for data in range(1, n+1):
        yield data ** 2
myiter = iter_square(5)
for data in myiter: 
    print(data, end=" ")
print()
print("----------------------------------------", 'demo3_2-List_Square with generator(lambda)', "-"*40)
# ----or---- 
iter_square = lambda n: (data ** 2 for data in range(1, n + 1)) #iter()
myiter = iter_square(5)
for data in myiter:
    print(data, end=" ")
print()

# demo 4
print("----------------------------------------", 'demo4-myRange()', "-"*40)
def myRange(start=0, stop=100, step=1):
    n = start 
    while n < stop:
        yield n 
        n += step
print(type(myRange))
for x in myRange(0,5):
    print(x)

# demo 5
print("----------------------------------------", 'demo5-fibonacci', "-"*40)
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a +b
        count += 1
fib = fibonacci(10)
for num in fib:
    print(num, end =' ')
"""
import java.util.Iterator;
class Fibonacci implements Iterable<Integer> {
    private final int n;
    public Fibonacci(int n) {
        this.n = n;
    }
    @Override
    public Iterator<Integer> iterator() {
        return new Iterator<Integer>() {
            private int count = 0;
            private int a = 0;
            private int b = 1;

            @Override
            public boolean hasNext() {
                return count < n;
            }

            @Override
            public Integer next() {
                int temp = a;
                a = b;
                b = temp + b;
                count++;
                return temp;
            }
        };
    }
}
public class Main {
    public static void main(String[] args) {
        Fibonacci fib = new Fibonacci(10);
        for (int num : fib) {
            System.out.print(num + " ");
        }
    }
}
"""

# demo 6
print("----------------------------------------", 'demo6-Decorator', "-"*40)
def upper(func): #Decorator
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱: ', func.__name__)
        print('函數參數: ', args)
        return newresult
    return newFunc
def greeting(string): #問候函數
    return string 
mygreeting = upper(greeting) #將原函數手動裝飾器
print(mygreeting('Hello! iPhone'))

print('----or----')# or

def upper(func): #Decorator
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱: ', func.__name__)
        print('函數參數: ', args)
        return newresult
    return newFunc
@upper  #取代 mygreeting = upper(greeting) #將原函數手動裝飾器
def greeting(string): #問候函數
    return string 
print(greeting('Hello! iPhone'))

print('----or----')# or

def upper(func): 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@upper  # 使用裝飾器語法簡化
def greeting(string): 
    return string 
print(greeting('Hello! iPhone'))

# demo 7
print("----------------------------------------", 'demo7-errcheck', "-"*40)

def errcheck(func):
    def newFunc(*args):
        if args[1] != 0:
            result  = func(*args) #Tuple 
        else:
            result = '除數不為\'0\''
            
        print('函數名稱: ', func.__name__)
        print('函數參數: ', args)
        print('執行解果: ', result)
        return result
    return newFunc
@errcheck
def mydiv(x, y):
    return x/y
print(mydiv(6, 2))
print(mydiv(6, 0))

# demo 8
print("----------------------------------------", 'demo8-decorator stacking', "-"*40)

def upper(func):
    def newfunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newfunc
def AddString(func):
    def wrapper(args):
        return '(addString)' + func(args) 
    return wrapper
@AddString  #Second
@upper #First
def greeting(string):
    return string
print(greeting('Hello! world'))