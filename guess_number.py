from random import randint


number = randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    guees = int(input('Введите число: '))

    if guees < number:
        print('Ваше число меньше того, что загадано.')

    elif guees > number:
        print('Ваше число больше того, что загадано')
    
    elif guees == number:
        break
print('Отличная интуиция! Вы угадали число :)')
