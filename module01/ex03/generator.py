import random  # randint authorized


def generator(text, sep, option=None):
    '''Option is an optional arg, sep is mandatory'''
    if (
        isinstance(text, str) and
        option in ["shuffle", "unique", "ordered", None] and
        isinstance(sep, str) and
        len(sep) > 0
    ):
        split_text = text.split(sep)
        if option == "shuffle":
            split_text_copy = split_text.copy()
            split_text = []
            while len(split_text_copy) > 0:
                random_index = random.randint(0, len(split_text_copy) - 1)
                split_text.append(split_text_copy[random_index])
                split_text_copy.pop(random_index)
        elif option == "unique":
            split_text = list(dict.fromkeys(split_text))
        elif option == "ordered":
            split_text.sort()

        for elem in split_text:
            yield elem
    else:
        print("ERROR")
