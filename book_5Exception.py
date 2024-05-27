print("----------------------------------------", 'demo-try_exception', "-"*40)
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Divisor cannot be zero.')
print(division(10, 0))

print("----------------------------------------", 'demo', "-"*40)
