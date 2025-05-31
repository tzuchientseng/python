class1 = [72, 96, 88, 79, "absent"]
class2 = [84, "absent", 95, 91,78]
class1.extend(class2)

# 淺copy
combine = class1[:]
print(f"(1):Two clases all scores: {combine}")

# list comprehension
combine_noAbsent = [item for item in combine if str(item).lower() != "absent"]
# while 'absent' in combine_noAbsent: combine_noAbsent.remove('absent')
# 淺copy
print(f"(2):Eliminate absent:{combine_noAbsent}")

sum_ = sum(combine_noAbsent[0:len(combine_noAbsent)])
average_= sum_/len(combine_noAbsent)
print(f"(3):The sum is {sum_}, and the average is {average_: .2f}")

combine_noAbsent[4] = 92
sum_ = sum(combine_noAbsent[0:len(combine_noAbsent)])
average_= sum_/len(combine_noAbsent)
print(f"(4):The new sum is {sum_}, and the new average is {average_: .2f}")
