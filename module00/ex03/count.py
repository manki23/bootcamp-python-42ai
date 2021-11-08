import re

def analyse_text(text):
    charNb = len(text)
    upperLettersNb = sum(1 for elem in text if elem.isupper())
    lowerLettersNb = sum(1 for elem in text if elem.islower())
    ponctuationMarksNb = len(re.findall(r'[^\w\s]', text))
    spacesNb = len(re.findall(r'[\s]', text))
    print("The text contains", charNb, "characters:")
    print("-", upperLettersNb, "upper letters")
    print("-", lowerLettersNb, "lower letters")
    print("-", ponctuationMarksNb, "ponctuation marks")
    print("-", spacesNb, "spaces")


def text_analyzer(*args):
    """This function counts the number of upper characters, lower chaarcters, punctuation and spaces in a given text."""
    if len(args) == 1 and isinstance(args[0], str):
        text = args[0]
        analyse_text(text)
    elif len(args) > 1 or len(args) == 1 and not isinstance(args[0], str):
        print("ERROR")
    else:
        print("What is the text to analyse?")
        text = input()
        analyse_text(text)
