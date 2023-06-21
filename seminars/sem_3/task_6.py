# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# text = input('Введите строку: ')
text = 'j; tttk;k;k aaa;kk;k kldffdfdfdf   hdgjsgjaghdhasdhjhg gjadsjdgasjdgj'.split()
text.sort()

max_len = len(max(text, key=len))

for index, value in enumerate(text, 1):
    print(f'{index}. {value:>{max_len}}')
