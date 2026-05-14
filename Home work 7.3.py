# ДЗ 7.3. Пошук підрядка


def second_index(text, some_str):
    if text.count(some_str) > 1:
        first = text.index(some_str)
        second = text.index(some_str, first + 1)
        return second
    else:
        return None


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"
print("ОК")
