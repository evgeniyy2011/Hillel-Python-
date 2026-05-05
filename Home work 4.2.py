# ДЗ 4.2. Знайти суму елементів із парними індексами

lst = [1, 3, 5]
# lst = [6]
# lst = []

storage = 0
if lst:
    for i in range(len(lst)):
        if i % 2 == 0:
            storage += lst[i]
    print(storage * lst[-1])
else:
    print(0)
