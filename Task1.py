# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.
# first_numb = 5
# print(first_numb)
# second_numb = 6
# print(second_numb)
#
# user_digit1 = int(input("Bведите первое значение: "))
# user_digit2 = int(input("Введите второе значение: "))
# sum_digit = user_digit1 + user_digit2
# print(f"Сумма введенных значений: {sum_digit}")
#
# name = input("Ваше имя: ")
# surname = input("Ваша фамилия: ")
# print(f"Добрый день, {name} {surname}!")

# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# time = int(input("Введите время в секундах: "))
# hours = time // 3600
# minutes = (time - hours*3600)//60
# seconds = time - (hours * 3600 + minutes * 60)
# print("%02d:%02d:%02d" % (hours, minutes, seconds))

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
# n = int(input("Введите значение n:"))
# result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# print(f"Сумма n+nn+nnn равна : {result}")

# 4) Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input("Введите целое положительное число: ")))
max_digit = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_digit:
        max_digit = number % 10
    if number > 9:
        continue
    else:
        print(f"Максимальное цифра в числе {max_digit}")
        break
