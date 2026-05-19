def add_one(some_list):
    new = ""
    for w in some_list:
        new += str(w)
    new = int(new) + 1
    result = [int(i) for i in str(new)]
    return result


# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
# assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
