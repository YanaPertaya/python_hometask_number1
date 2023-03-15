# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


number = int(input('Введите трехзначное натуральное число: '))

number_1 = number // 100
number_2 = number // 10%10
number_3 = number % 10
print(number_1 + number_2 + number_3)
