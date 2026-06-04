import codecs


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()
        new = ""
        flag = True
        for i in html:
            if i == "<":
                flag = False
            elif i == ">":
                flag = True
                continue
            if flag:
                new += i
        print(new)
    with codecs.open(result_file, mode="w", encoding="utf-8") as g:
        g.write(new)


delete_html_tags("draft.html")
