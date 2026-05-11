# ДЗ 6.1. Діапазон букв
import string

new_string = input("Введите две буквы латинского алфавита через дефис (Наример: a-z) ")
first = string.ascii_letters.index(new_string[0])
second = string.ascii_letters.index(new_string[2])
result = ""
for i in range(first, second + 1):
    result += string.ascii_letters[i]
print(result)
