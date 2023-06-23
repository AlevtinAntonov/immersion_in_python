# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(list_1):
    has_swapped = True

    while (has_swapped):
        has_swapped = False
        for i in range(len(list_1) - 1):
            if list_1[i] > list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
                has_swapped = True
    return list_1


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


my_list = [5, 3, 12, 89, 8, 6, 4, 7, 2, 1]
print(sorted(my_list))
print(bubble_sort(my_list))
print(quicksort(my_list))
