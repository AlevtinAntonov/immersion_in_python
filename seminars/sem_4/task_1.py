# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = 'Hello world'
def unicode_text(in_text):
    res = sorted((ord(chr) for chr in in_text), reverse=True)
    return res

print(unicode_text(text))

