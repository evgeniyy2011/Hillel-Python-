# ДЗ 6.3. Добуток чисел
from copy import deepcopy

# numb = list(input("Enter your number - "))
# new_numb = "*".join(numb)
# result = 0
# while eval(new_numb) > 9:
#     new_numb = "*".join(str(eval(new_numb)))
# print(eval(new_numb))


# Variant #2

numb = list(input("Enter your number - "))
counter = deepcopy(numb)
counter_two = 1
while int("".join(counter)) > 9:
    for i in counter:
        counter_two *= int(i)
    counter = list(str(counter_two))
    counter_two = 1
print("".join(counter))
