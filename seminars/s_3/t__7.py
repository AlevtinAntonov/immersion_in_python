#  Задание №7
# # ✔ Пользователь вводит строку текста.
# # ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# # ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# # ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях

txt = 'asdfghjk dfghjkl;; rtyuiop[uuoi wtrreruwetu'
print(txt)


dict_d = {}

dict_d.get()
for i in txt:
    dict_d[i] = txt.count(i)


print(dict_d)
res = {}
for letter in txt:
    res[letter] = res.get(letter, 0) + 1

print('\n'.join((f'{k} : {v}' for k, v in res)))