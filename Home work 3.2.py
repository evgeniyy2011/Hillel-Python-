# ДЗ 3.2. Перемістити елемент у списку
from operator import index

lst_one = [12, 3, 4, 10]
# lst_one = [1]
# lst_one = []
# lst_one = [12, 3, 4, 10, 8]
new_lst = []
if len(lst_one) >= 1:
    new_lst.append(lst_one[-1])
for i in lst_one[:-1:]:
    new_lst.append(i)
print(new_lst)
