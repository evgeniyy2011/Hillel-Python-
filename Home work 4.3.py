# ДЗ 4.3. Список із 3 елементів
import random

lst = random.randrange(3, 11)
storage = []
storage_two = []
for _ in range(lst):
    storage.append(random.randint(0, 100))
storage_two = [storage[0], storage[2], storage[-2]]

print(storage)
print(storage_two)


# Вариант #2


# lst = random.randrange(3, 11)
# storage = []
# storage_two = []
# for _ in range(lst):
#     storage.append(random.randint(0, 100))
# for i in range(len(storage)):
#     if i == 0 or i == 2:
#         storage_two.append(storage[i])
# storage_two.append(storage[len(storage) - 2])
#
# print(storage)
# print(storage_two)
