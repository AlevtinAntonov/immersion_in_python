import string

LETTERS = string.ascii_letters + " "

def str_replace(text):
    return "".join(i for i in text if i in LETTERS).lower()