# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

persons = ['Petr', 'Ivan', 'Oleg']
rates = [10_000, 20_000, 150_000]
bonuses = ['10.25%', '15.55%', '9.5%']
HUNDRED = 100


def calc_bonus(person_name, bonus_rate, percent_bonus):
    res_bonus = dict()
    for name, rate, percent in zip(person_name, bonus_rate, percent_bonus):
        res_bonus[name] = float(percent[:-1]) * rate / HUNDRED

    return res_bonus


print(calc_bonus(persons, rates, bonuses))
