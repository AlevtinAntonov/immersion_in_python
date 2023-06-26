# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
import sys

START_SUM = 0
START_OPERATION = 0

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
    return bal, op


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
    return bal, op


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
                balance, operations = increase(balance, operations)
            case 2:
                balance, operations = decrease(balance, operations)
            case 3:
                sys.exit()
            case _:
                print('Повторите попытку')


start()