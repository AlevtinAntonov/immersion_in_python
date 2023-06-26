# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

persons = ['Petr', 'Ivan', 'Oleg']
rates = [100, 200, 150]
bonuses = ['10.25%', '15.55%', '9.5%']


def calc_bonus(person_name: list[str], bonus_rate: list[int], per_sent_bonus: list[str]) -> dict:
    res_bonus = dict()
    sum_bonuses = list(zip(person_name, bonus_rate, per_sent_bonus))
    for k, rate, per_cent in sum_bonuses:
        res_bonus[k] = float(str(per_cent).replace('%', '')) * rate

    return res_bonus


print(calc_bonus(persons, rates, bonuses))
