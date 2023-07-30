class CheckName:
    def __init__(self, check_fst, response_fst, check_scd, response_scd):
        self.check_fst = check_fst
        self.check_scd = check_scd
        self.response_fst = response_fst
        self.response_scd = response_scd

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if not self.check_fst(value):
            raise ValueError(self.response_fst + f': {value}')
        if not self.check_scd(value):
            raise ValueError(self.response_scd + f': {value}')
        setattr(instance, self.param_name, value)


class CheckEstimations:
    def __init__(self, lo_limit: int, hi_limit: int) -> None:
        self.lo_limit = lo_limit
        self.hi_limit = hi_limit

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        student = f'{instance.last_name} {instance.first_name} {instance.patronymic} '
        self.validate(value, student)
        setattr(instance, self.param_name, value)

    def validate(self, checked: dict, student_name):
        for subject, estimations_list in checked.items():
            self.validate_estimation(estimations_list, subject, student_name)

    def validate_estimation(self, estimation_list: list, subject: str, student_name):
        for estimation in set(estimation_list):
            if not (self.lo_limit <= estimation <= self.hi_limit):
                raise ValueError(f'{student_name}: Estimation value: {estimation} is out of range; subject: {subject}')


if __name__ == '__main__':
    print('Запустите main.py')
