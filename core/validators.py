from django.core.exceptions import ValidationError

def check_raiting(value):
    if value > 10 or value < 1:
        raise ValidationError('Рейтинг выставляется от 1 до 10')

def check_phonenum(phonenum):
    if len(phonenum) != 13 or phonenum[0] != '+':
        raise ValidationError('Проверьте введенный номер телефона')

def check_age(age):
    if age < 18:
        raise ValidationError('Вы должны быть совершеннолетним')