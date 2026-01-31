def middle_char(text):
    length = len(text)

    if length % 2 == 0:
        middle = text[length//2 - 1] + text[length//2]
    else:
        middle = text[length//2]

    return middle
