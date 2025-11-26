# № 1
name = "Lida"
age = 29
height = 1.65

print("Your name:", name)
print("Your age:", age)
print("Your height:", height)

# № 2
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
print(x)


# № 3
a = b = 7
print(a)
print(b)
a = 10
print(b)
# Значение b не изменилось, т.к. эта переменная ссылается на объект "7".

# № 4
x = y = z = 100
print(id(x))
print(id(y))
print(id(z))
# ID одинаковые

x = 1
y = 2
z = 3

print(x)
print(y)
print(z)

print(id(x))
print(id(y))
print(id(z))
# ID разные

# № 5
a = 5
b = 10
a, b = b, a
print(a)
print(b)

# № 6
# True = Lida
# print = sun
# if = choice
# Выдаёт ошибку. Переменные так нельзя называть, т.к. эти слова имеют специальное значение в языке Python.\

import keyword
print(keyword.kwlist)

# № 7
var1 = 42
var2 = 3.14
var3 = "Hello"
print(var1)
print(var2)
print(var3)
var1 = "Good morning"
print(var1)

# № 8
name = "Vika"
surname = "Petrova"
age = 25
job = "accountant"
height = 1.7
print(name)
print(surname)
print(age)
print(job)
print(height)
print(type(name))
print(type(surname))
print(type(age))
print(type(job))
print(type(height))

переменная = 10
print(переменная)
# Да, получилось создать переменную на кириллице, но это нарушает общепринятую традицию использовать латиницу.
