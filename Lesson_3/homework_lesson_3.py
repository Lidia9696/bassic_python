# 1. Простая работа с print()
print("Hello, world!")
print(5, 10, 15)
print(10 + 25)

# 2. Использование параметров sep и end в print()
print(1, 2, 3, sep = " & ")

print("Python", end=" ")
print("лучший язык")

# 3. Форматированный вывод с F-строками
x = 3.14
y = -8
print(f"Координаты точки: x = {x}; y = {y}")

name = input("Введите имя: ")
age = input("Введите возраст: ")
print(f"Имя: {name}, возраст: {age}.")

# 4. Работа с input()
name = input("Как вас зовут? ")
print(f"Привет, {name}")

# 5. Преобразование типов
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
sum = a + b
print(f"Сумма числа {a} и числа {b} равняется {sum}")

a = int(input("Введите целое число: "))
print(f"Квадрат числа {a} равняется {a ** 2}.")

# 1. Основы булевой логики
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = (8 > 12)
print(type(res))
print(res)

# 2. Проверка четности и кратности числа
x = 15
print(x % 2 == 0)
print(x % 5)
print(bool(x / 3 and x / 5))

#3. Работа с логическими операторами (and, or, not)
y = 4.5
print(bool(1 <= y and y <= 10))
print(bool(0 <= y <= 5) or (10 <= y <= 15))
print(bool(not(y < 5)))

# 4. Приоритет логических операций ????????????????????????????????????
print(True or False and False)
print(not False and True)
print(False or not True and True)
print(not (10 > 5 or 3 < 1))

# True
# True
# False
# False

# 5. Приведение типов к bool
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))

# # False
# # True
# # True
# # False
# # True
# # True

# # 6. Дополнительное задание
n = 7
print(bool(n>0))
print(bool(n % 2 ==0))
print(bool(n % 3 ==0))

# True
# False
# False

# Срезы строк
# 1. Доступ к символам по индексу.
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2], s[-2], sep = ", ")

# print(s[100])
# Выдает ошибку:"string index out of range"

print(len(s))
print(s[15])

# 3. Создание срезов
a = (s[:6])
print(a)
b = (s[-5:])
print(b)
c = (s[2:7])
print(c)
d = (s[::2])
print(d)
e = (s[::-1])
print(e)

# 4. Работа с шагом в срезах
a = (s[::3])
print(a)

# 5. Проверка неизменяемости строк
s[0] = "п"
В строки нельзя вносить изменения.
s2 = "П" + s[1:]
print(s2)

# 6. Дополнительное задание
word = "abcdefgh"
a = (word[2:5])
print(a)
b = (word[::-1])
print(b)
c = (word[1:-1])
print(c)
