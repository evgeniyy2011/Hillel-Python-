# ДЗ 3.3. Розділити один список на два списки

# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []

storage = []
middle = len(lst) // 2
if len(lst) % 2 == 0:
    storage = [lst[:middle]] + [lst[middle:]]
elif len(lst) % 2 != 0:
    storage = [lst[: middle + 1]] + [lst[middle + 1 :]]
print(storage)
