# ДЗ 4.1. Перемістити всі нулі до кінця списку

# lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

storage = []
for i in lst:
    if i != 0:
        storage.append(i)
for q in lst:
    if q == 0:
        storage.append(q)
print(storage)
