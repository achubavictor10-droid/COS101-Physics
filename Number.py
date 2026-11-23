from statistics import median,mode,multimode 
numbers = [10,20,19,20,13,17,10,20,16,18,40]

add = sum(numbers)
avg = sum(numbers)/len(numbers)
middle_num = median(numbers)
mode_num = mode(numbers)

print(add)
print(avg)
print(middle_num)
print(mode_num)
