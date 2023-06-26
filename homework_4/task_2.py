# Напишите функцию для транспонирования матрицы

def matrix_transpose(lst):
    return [list(i) for i in zip(*lst)]


my_lst = [[1, 2, 3], [4, 5, 6]]
print(my_lst)
print(matrix_transpose(my_lst))
