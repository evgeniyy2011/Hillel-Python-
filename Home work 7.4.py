# ДЗ 7.4. Пошук спільних елементів


def common_elements():
    first_set = set()
    second_set = set()
    for q in range(100):
        if q % 3 == 0:
            first_set.add(q)
        if q % 5 == 0:
            second_set.add(q)
    return first_set.intersection(second_set)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())
