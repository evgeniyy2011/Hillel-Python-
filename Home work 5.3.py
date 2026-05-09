# ДЗ 5.3. hashtag

sentence = input("Enter string")
result = []
new = []
for i in sentence.split(" "):
    result.append(i.title())
result = list("".join(result))
new.append("#")
for q in result:
    if q.isalnum():
        new.append(q)
new = "".join(new)
print(new[:140])
