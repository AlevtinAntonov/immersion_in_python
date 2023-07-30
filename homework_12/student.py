from checking import CheckName, CheckEstimations

_LO_ESTIMATION = 2
_HI_ESTIMATION = 5
_LO_TEST_RESILT = 0
_HI_TEST_RESULT = 100


class Student:
    last_name = CheckName(str.isalpha, "Разрешено наличие только букв", str.istitle, "Первая буква заглавная")
    first_name = CheckName(str.isalpha, "Разрешено наличие только букв", str.istitle, "Первая буква заглавная")
    patronymic = CheckName(str.isalpha, "Разрешено наличие только букв", str.istitle, "Первая буква заглавная")

    estimations = CheckEstimations(_LO_ESTIMATION, _HI_ESTIMATION)
    tests = CheckEstimations(_LO_TEST_RESILT, _HI_TEST_RESULT)

    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def get_tests_average(self) -> dict[str, float]:
        res = {}
        for subj, test_results in self.tests.items():
            res[subj] = round(sum(test_results) / len(test_results), 1)
        return res

    def get_estimations_average(self) -> float:
        res = []
        for estimation in self.estimations.values():
            res.append(sum(estimation) / len(estimation))
        return round(sum(res) / len(res), 1)

    def __str__(self):
        return (f'\n{"-" * 38}'
                f'\nСтудент: {self.last_name} {self.first_name} {self.patronymic}'
                f'\nСредний бал по тестам:'
                f'\n{self.averages_str()}'
                f'\nСредняя оценка по всем предметам : {self.get_estimations_average()}'
                f'\n{"-" * 38}')

    def averages_str(self) -> str:
        return '\n'.join([f'{subj + ":":_<34}{test_res:<10}' for subj, test_res in self.get_tests_average().items()])


if __name__ == '__main__':
    print('Запустите main.py')
