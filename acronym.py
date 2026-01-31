def acronym(sentence):
    words = sentence.split()
    result = ""

    for word in words:
        result = result + word[0].upper()

    return result
