"""Модуль генерации числа"""
from random import randint

from_int = int(input('Начальная точка (число): '))
to_int = int(input('Последняя точка (число): '))

rand_int = randint(from_int, to_int)

print('Программа сгенерировала число.',
     f'Оно находится в промежутке между {from_int} и {to_int} включительно.', 
      'Попробуйте угадать!')

guess_number = int(input('Загадайте число: '))

while guess_number != rand_int:
    if rand_int > guess_number:
        print('Неверно! Загаданное число больше.')
        guess_number = int(input('Загадайте число заново: '))
    else:
        print('Неверно! Загаданное число меньше.')
        guess_number = int(input('Загадайте число заново: '))

print('Верно! Вы угадали число!')
