# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано: a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка - стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить, является ли треугольник разносторонним, равнобедренным или равносторонним.

a, b, c = map(int, input('Введите стороны треугольника через пробел: ').split())

if a > 0 and b > 0 and c > 0 and a + b > c or a + c > b or b + c > a:

    if a != b and a != c and b != c:
        print('Разносторонний треугольник')
    elif a == b and a != c or a == c and b != c or b == c and a != c:
        print('Равнобедренный треугольник')
    elif a == b and a == c and b == c:
        print('Равносторонний треугольник')
else:
    print('Треугольник не существует')


# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Введите число: '))
k = 2
if num > 0 or num < 100000:
    while k * k <= num and num % k != 0:
        k += 1
    if k*k >num:
        print('Простое число')
    else:
        print('Составное число')

else:
    print('Введено некорректное число')

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

print('УГАДАЙ ЧИСЛО')
num = randint(0, 1000)
i = 1
while i <= 10:
    res = int(input('Введите ваше число: '))
    if res < num:
        print('Загаданное число больше')
    elif res > num:
        print('Загаданное число меньше')
    else:
        print(f'ПОЗДРАВЛЯЕМ!!! Вы угадали число {num} с {i} раза!')
        exit()
    i += 1
print(f'Сожалеем, у вас кончились попытки, загаданное число было {num}')
