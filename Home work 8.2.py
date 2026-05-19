# ДЗ 8.2. Паліандром


def is_palindrome(text):
    first_text = ""
    second_text = ""
    for i in text:
        if i.isalnum():
            first_text += i
    for i in reversed(text):
        if i.isalnum():
            second_text += i
    return first_text.lower() == second_text.lower()


# assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
# assert is_palindrome("0P") == False, "Test2"
# assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
