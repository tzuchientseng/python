x, y = map(int, input("Please enter two numbers separated by a space: \n").split())  
try:
    if y < x:  
        raise ValueError("y must be greater than or equal to x")  
except ValueError as e:
    print(e) 
else:
    result = sum(i for i in range(x, y+1)) 
    print("The sum of integers from", x, "to", y, "is:", result)  

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_of_lists = map(lambda x, y: x + y, list1, list2)  # Adding corresponding elements of list1 and list2 using a lambda function
print(list(sum_of_lists))  # Output: [5, 7, 9] - Printing the result of adding corresponding elements of list1 and list2

words = ['hello', 'world', 'python']
uppercase_words = map(str.upper, words)  # Converting each word in the list to uppercase using the str.upper function
print(list(uppercase_words))  # Output: ['HELLO', 'WORLD', 'PYTHON'] - Printing the list of uppercase words
