from datetime import datetime as dt


def calculation_logger(operation, data, bal):
    '''Creates log file with current time and action'''
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time}; номер операции -> {operation};  сумма -> {data}; баланс -> {bal}\n')
