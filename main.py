# first lesson

# print("Hello world!")
# print("--------")
# print("|   |   |")
# print("|   |   |")
# print("|   |   |")
# print("|   |   |")
# print("--------")

# second lesson
# age = 22
# print(age + 1)

# third lesson
# name = "Saidakbar"
# print(name * 2)
# print(name + " Makhkamov")
# print(name + str(10))

# fourth lesson
# list = [10, 20, 30]
# print(list)

# fivth lesson
# numbers = (10, 20, 30)
# print(numbers)

# sixth lesson
# ages = {"Saidakbar":22, "Noname":24}
# keys = list(ages.keys())
# values = list(ages.values())
# print(keys)
# print(values)

# seventh lesson Boolens
# boolen = True
# print(boolen)

# eighth lesson comments
""""
Here large comments will be
"""

# nineth lesson Conditions

# age = 26
# if age == 22:
#     print("Age is 22")
# elif age == 24:
#     print("Age is 24")
# elif age>25:
#     print("Age is more than 25")
# elif age< 26:
#     print("Age is less than 26")
# else:
#     print("Unknown age")

# tenth lesson while
# a=0
# while a<10:
#     a+=1
#     print(a,"Hello")

# eleventh lesson for
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for item in numbers:
#     print(item)

# name = "Saidakbar"
# for item in name:
#     print(item)

# contiune and break

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for n in numbers:
#     if n == 4:
#         break
#         # continue
#     print(n)
# from builtins import tuple
#
# taomlar = ['osh', 'somsa', 'grill', 'moshhordi', 'bishfteks']
# nonushta = taomlar[:]
# # print(nonushta)
# del nonushta[0]
# del nonushta[1]
# del nonushta[1]
# nonushta.append('kalbasa')
# nonushta.append('sir')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# # nonushta[0] = 'qaymoq'


# ismlar = ['Sidakbar', 'Rustam', 'Farrux', 'Oybek', 'Toxir']
#
# i=0
# for ism in ismlar:
#     print(f"{ism} qalesan")
#     i = i+1
# print(f"Kod {i} martta takrorlandi")

# toq_sonlar = range(11,100,2)
#
# for toq_son in toq_sonlar:
#     print(toq_son**3)

# kinolar = []
#
# print("O'zingiz yoqtirgan 5 ta kino ni kiriting")
# for n in range(5):
#     kinolar.append(input(f"{n + 1}-kino nomini kiriting:"))
# print(kinolar)
n = int(input(f"Bugun nechta odam bilan suxbatlashdingiz?>>"))
suxbatlashgan_odamlar = []

for odam in range(n):
    suxbatlashgan_odamlar.append(input(f"{odam + 1} - suxbatlashgan odam ismi:"))
print(suxbatlashgan_odamlar)





