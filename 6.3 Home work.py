# ДЗ 6.3. Добуток чисел

numb = list(input("Enter your number - "))
new_numb = "*".join(numb)
result = 0
while eval(new_numb) >= 9:
    new_numb = "*".join(str(eval(new_numb)))
print(eval(new_numb))


