# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются
# в одноимённые переменные без s на конце.


glb = globals()
def func():
    for var_name in list(glb):
        if var_name.endswith('s') and var_name != 's':
            glb[f'{var_name[:-1:]}'], glb[f'{var_name}'] = glb[f'{var_name}'], None


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello World'
names = 'NoName', 'OtherName', 'NewName'
sx = 42

print(f'{datas=}')
print(f'{s=}')
print(f'{names=}')
print(f'{sx=}')

func()

print(f'{datas=}')
print(f'{s=}')
print(f'{names=}')
print(f'{sx=}')

print(f'{data=}')
print(f'{s=}')
print(f'{name=}')
print(f'{sx=}')
