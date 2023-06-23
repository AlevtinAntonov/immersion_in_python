# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = 'Encodings are specified as strings containing the encoding’s name'
def unicode_text(in_text):
       res = sorted(' '.join(r'\u{:04X}'.format(ord(chr)) for chr in in_text).split(), reverse=True)
       return res

print(unicode_text(text))