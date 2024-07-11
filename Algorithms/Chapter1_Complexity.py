print("----------------------------------------", 'demo', "-"*40)
def recusive_sum(lst):
    """
     Time complexity: O(n) (因為越切越短為線性關係)
     Space complexity: O(n)
    """
    if not lst: 
        return 0 
    else: 
        return lst[0] + recusive_sum(lst[1:]) #自動切到尾巴
        
list = [5, 7, 9, 15, 21, 6]
print(recusive_sum(list))


print("----------------------------------------", 'demo', "-"*40)
# 以下Stack會爆掉
# def recursive_sum(lst):
#     if not lst: 
#         return 0 
#     else: 
#         middle = len(lst) // 2
#         return recursive_sum(lst[:middle]) + recursive_sum(lst[middle:])

# lst = [1, 2, 3, 4, 5]
# print(recursive_sum(lst))
# Time complexity: O(n^2) (切一次為線性關係切兩次n^2)
# Space complexity: O(n)
# print("-"*20,'NEXT',"-"*20)

def f(i):
    """
    Time Complexity: O(1) (因為1/i)
    Space Complexity:  O(n)
    """
    if i == 1: 
        return 1
    else: 
        return 1/i + f(i-1)

n = int(input("Enter n:"))
print([round(f(i), 3) for i in range(1,n+1)])  

print("----------------------------------------", 'demo', "-"*40)

def f2(i):
    """
    Time Complexity: O(n)
    Space Complexity:  O(n) (因為i/i+1)
    """
    if i == 1:
        return 1/2
    else:
        return i/(i+1) + f2(i-1)
    
n = int(input("Enter n:"))
print([round(f2(i), 3) for i in range(1,n+1)])  

print("----------------------------------------", 'demo', "-"*40)

def combination(n, k):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n) 
    """
    # Base Cases
    if k == 0 or k == n:
        return 1
    # Recursive case
    return combination(n-1, k-1) + combination(n-1, k) 

def permutation(n, k):
    """
    Time Complexity:  O(n!)
    Space Complexity: O(n)
    """
    # Base Case
    if k == 0:
        return 1
    # Recursive case
    return n * permutation(n-1, k-1)

n = 20  # 數列的長度
total_combinations = combination(n, 2)  # 計算 20 個元素的排列組合有多少種方法
print("Total combinations:", total_combinations)

print("----------------------------------------", 'demo', "-"*40)

n = 20  # 集合的大小
k = 20   # 選取的元素個數
total_permutations = permutation(n, k)  # 計算排列的方法數
print("Total permutations:", total_permutations)

print("----------------------------------------", 'demo', "-"*40)

# from itertools import permutations
# # 定義字符列表
# chars = ['a', 'b', 'c', 'd', 'e']
# # 初始化一個空列表來存儲所有排列
# all_permutations = []
# # 生成所有排列並添加到列表中
# for r in range(1, len(chars) + 1):
#     all_permutations.extend(permutations(chars, r))
# # 打印所有排列
# for permutation in all_permutations:
#     print(''.join(permutation))
# # Time Complexity:  O(n!)
# # Space Complexity: O(1)

def permutations_recursive(chars, prefix='', length=None):
    """
    Time Complexity:  O(n*n!)
    Space Complexity: O(n)
    """
    if length is None:
        length = len(chars)
    if length == 0:
        print(prefix)
    else:
        for i in range(len(chars)):
            permutations_recursive(chars[:i] + chars[i+1:], prefix + chars[i], length - 1)

# 定義字符列表
chars = ['a', 'b', 'c', 'd', 'e']

# 調用遞迴函數並打印所有排列
permutations_recursive(chars)

print("----------------------------------------", 'demo', "-"*40)