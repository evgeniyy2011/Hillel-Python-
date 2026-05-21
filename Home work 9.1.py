def popular_words(text, words):
    text = (text.lower()).split()
    d1ct = {}
    for q in range(len(text)):
        for key in words:
            if key in text:
                d1ct[key] = text.count(key)
            else:
                d1ct[key] = 0
    return d1ct


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
print("OK")
