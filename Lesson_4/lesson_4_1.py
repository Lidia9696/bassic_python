s = "Daniil Nikolaev" #это строка
# print(s.lower()) #строка.метод()
# print(s.upper()) #создается новая строка
# print(s.count("i"))
# print(s.count("i",0))
#print(s.count("i",0, end: 6))
# print(s.count("i",0,6))
# print(s.count("a", 0, 6))
# print(s.find("i", 6))
# print(s.rfind("i"))
# print(s.index("y")
# print(s.replace("a", "o"))
# print(s.replace("i", "e", 2))
# print(s.replace(" ", ""))
# print(s.replace(" ", "").isalpha())
#a = "2"
# print(type(a))
#print(a.isdigit())
# a = "22"
# b = "223451"
# c = "3322"
# print(a.rjust(8, "*"))
# print(b.rjust(8, "-"))
# print(c.rjust(8, "+"))
#
# print(a.ljust(8, "*"))
# print(b.ljust(8, "-"))
# print(c.ljust(8, "+"))
# s = "Николаев-Даниил-Александрович"
# name, surname, second_name = s.split("-")
# print(name)
# print(second_name)
# print(surname)

# nums = "1,  ,2,43, 32,33"
# print(nums.replace(" ","").split(","))
# words = ['str', 'float', 'bool']
# print(', '.join(words))
a = "   ААА ааа  "
print(a.strip())
print(a.rstrip())
print(a.lstrip())