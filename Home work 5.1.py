# ДЗ 5.1. Ім'я змінної

import keyword

message = input("Enter yor message")
result = True
if not message:
    result = False
for i in message:
    if " " in i or i.isupper():
        result = False
if message[0].isdigit():
    result = False
if message.startswith("__"):
    result = False
if keyword.iskeyword(message):
    result = False
for i in message:
    if not (i.isalnum() or i == "_"):
        result = False
print(result)
