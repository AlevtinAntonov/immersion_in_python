# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import sys
from logger import calculation_logger

START_SUM = 0
START_OPERATION = 0
global inc, dec


def check_input(message):
    while True:
        inp = int(input(message))
        if inp % 50 != 0:
            print('Недопустимая сумма. Сумма должна быть кратна 50!')
        else:
            return inp


def increase(bal, op):
    inc = check_input("Введите сумму для пополнения ")
    if op % 3 == 0 and op != 0:
        bal += bal * 0.03
    bal += inc
    op += 1
    if bal > 5_000_000:
        bal -= bal // 10
    return bal, op, inc


def decrease(bal, op):
    if bal > 5_000_000:
        bal -= bal // 10
    dec = check_input('Введите сумму для снятия ')
    percent = dec * 0.015
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    dec += percent
    if bal > dec:
        bal -= dec
    else:
        print('Недостаточно средств!')
    if op % 3 == 0 and op != 0:
        bal += bal * 0.03
    op += 1
    return bal, op, dec


def start():
    balance = START_SUM
    operations = START_OPERATION
    while True:
        select = int(input(f"""Баланс: {balance}
Операции со счетом: {operations}

Доступные действия:
1. Пополнить
2. Снять
3. Выход

Выберите действие: """))
        match select:
            case 1:
                balance, operations, inc = increase(balance, operations)
                calculation_logger(select, inc, balance)
            case 2:
                balance, operations, dec = decrease(balance, operations)
                calculation_logger(select, dec, balance)
            case 3:
                calculation_logger(select, 'Выход', balance)
                sys.exit()
            case _:
                print('Повторите попытку')
                calculation_logger(select, 'Повторите попытку', balance)


start()
