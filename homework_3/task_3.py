# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re

big_string = 'Python’s documentation has long been considered to be good for a free programming language. There ' \
             'are a number of reasons for this, the most important being the early commitment of Python’s creator, ' \
             'Guido van Rossum, to providing documentation on the language and its libraries, and the continuing ' \
             'involvement of the user community in providing assistance for creating and maintaining documentation.'

result = re.sub(r'[.,"\'-?:!;]', '', big_string.lower()).split()

print(result)