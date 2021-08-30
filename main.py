'''
for x in range(length_list) :
    print(a[x])




def bubble_sort (a) :
    for i in range(1, len(a)) :
        for j  in range(0, len(a)) :
            if a[j] < a[i] :
                a[j], a[i] = a[i], a[j]



bubble_sort([6,5,8,1,2,4,3])
print(a)




def foo () :
    a = input()
    b = input()
    print(type(a))
    print(type(b))
    if a > b :
        return True
    else:
        return False

print(foo())



a = [-6, -5, -8, -1, -2, -4, -3, 22, -15, -23, 190]


def max_el(a):
    b = a[0]
    for i in range(1, len(a)):
        if a[i - 1] < b:
            b = a[i - 1]
    return b


print(max_el(a))
'''
import string
import math

'''
n = int(input())
stars = '*'
while len(stars) >= n:
    print(stars)
    stars += '*'


i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
'''
'''                                           
user_num = int(input())                             #СПРОСИТЬ У КОЛИ
summ = int(0)
while user_num != int(0):
    summ += user_num
    user_num = int(input())
print(summ)
'''
'''
считываем инт число через ввод, после этого :

если число <= 10 - нам не инетересно 
если число >= 100 - останавливаем программу  +++++++++++++++++
в консоль, отдельными строками выводятся числа от 10 до 100

user_num = -1
while ...:
    user_num = int(input())
    if user_num > 100:
        break
    if user_num >= 10:
        print(user_num)
    if user_num < 10:
        continue

'''
'''
for i in range(0,9,10):
    print('hello'+ '1'*i)
'''
'''
вывод квадрата из звёздочек


def star_rectangle():
    star = '*'
    count_of_stars = int(input())
    rectangle_length = int(input())
    for i in range(rectangle_length):
        print(star * count_of_stars)

star_rectangle()
'''
'''
def st():
    n = int(10)
    for i in range(n):
        print('*', end='\n')

st()
'''
'''
на вход принимаются 4 числа : a,b,c,d - каждое значение в своей строке
программа выводит кусок таблицы умножения, в пределах от a до b, умножая на числа из отрезка от c до d 
при этом (a <=b), (c<=d)
разделять значения с помощью табуляции в выводе \t
'''
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d+1):
    print('\t', c, '\t', d)
    for j in range(a, b+1):
        print(j, '\t', j*c, '\t', j*d)

'''
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d+1):
    print('\t', c, '\t', d)
    for j in range(a, b+1):
        print(a, '\t', j*c, '\t', j*d)
'''
'''      
a, b, c, d = map(int, input().split())

for i in range(c, d):
    print('\t', c, '\t\t', d)
    for j in range(a, b+1):
        print(j, '\t', j*c, '\t', j*d)

'''
'''
from random import randint
times = 1
level = float(input('Какой уровень 1 2 3? '))
if level == 1 or level == 2 or level == 3:
    score = level
    print('ПЕРЕХОДИМ НА 1 УРОВЕНЬ')
    while 2 > level > 0.9:
        z = randint(1, 2)
        n1 = randint(1, 5)
        n2 = randint(1, 5)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        else:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('ПЕРЕХОДИМ НА 2 УРОВЕНЬ')
    while 3 > level > 1.9:
        z = randint(1, 2)
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        else:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('ПЕРЕХОДИМ НА 3 УРОВЕНЬ')
    while 4 > level > 2.9:
        z = randint(1, 4)
        n1 = randint(1, 50)
        n2 = randint(1, 50)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        elif z == 2:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        elif z == 3:
            r = float(input(str(times) + ')' + str(n3) + '*' + str(n4) + '=')) == n3*n4
        else:
            r = float(input(str(times) + ')' + str(n3*n4) + ':' + str(n4) + '=')) == n3*n4/n4
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('Вашь счёт = ' + str(int((level-score)*10)) + ' из ' + str(times-1))
else:
    print('Такого уровня нету!')

'''

'''
string_input = input()

if isinstance(string_input, int):
    print('Integer input')
elif isinstance(string_input, float):
    print('Float input')
else:
    print('String input')
'''
'''

print(type(string_input))
'''
'''

def input_type_search ():
    try:
        input_val = int(input())
        print('Integer input', input_val)
    except ValueError:
        try:
            input_val = str(input)
            print('String input', input_val)
        except ValueError:
            print('Float input', input_val)


user_input1 = input()


-пользователь вводит текст с клавиатуры
-один из типов  : int, float, str
-если пользователь ввёл число int - вывести сообщение типа "это инт"

+++

если в данной строке есть только буквы => это str
если цифры и знаки => int
сли только знаки => 
'''
'''
def input_type_search(user_input):
    try:
        input_val = int(user_input)
        print(input_val, '= Integer input', )
    except ValueError:
        try:
            input_val = float(user_input)
            print(input_val, '= Float input', )
        except ValueError:
            print('= String input')


input1 = input('Enter int, str, or float:\n')
input_type_search(input1)
input2 = input('Enter int, str, or float:\n')  
input_type_search(input1)
input3 = input('Enter int, str, or float:\n')
input_type_search(input1)
'''

'''


user_input = input()
print(user_input[::-1],)
'''

'''
перевернуть вводимый текст ЧЕРЕЗ СПИСОК

# reversed(list)

# list[::-1]

list = []
elem_count = int(input('Ввдите количество элементов\n'))
print('Введите заданное количество элементов списка\n')
for i in range(elem_count):
    new_element = input()
    list.append(new_element)
print('Перевёрнутый список =', list[::-1])

'''

'''

вывод чётных чисел из списка

list_int = []
elem_count = int(input('Введите количество элементов\n'))
print('Введите заданное количество элементов списка\n')
for i in range(elem_count):
    new_int = int(input())
    list_int.append(new_int)
for j in list_int:
    if int(j) % 2 == 0:
        print(j, end='\t')

'''

'''
на вход числа, положительные и отрицательные, на выход только отрицательные

list_int = []
elem_count = int(input('Введите количество элементов\n'))
print('Введите заданное количество элементов списка\n')
for i in range(elem_count):
    new_int = int(input())
    list_int.append(new_int)
for j in list_int:
    if int(j) < 0:
        print(j, end='\t')

'''
'''
stroka = input()
for i in range(len(stroka)):
    print(stroka[i], end='')

'''

'''
каждый второй символ - собачка

user_inp = input()
length = len(user_inp)
i = 0
while i < length:
    if i % 2 == 0:
        user_inp = user_inp.replace(user_inp[i], '@')
    i += 1
print('Вывод ->', user_inp)


'''
'''
каждый второй заменить на собачку


user_inp1 = list(input())
length2 = len(user_inp1)
for i in range(1, length2 +1, 2):
    user_inp1[i] = '@'

print(user_inp1)
'''

'''Программа "Здоровье" с Малышевой

min_sleep = int(input())
max_sleep = int(input())
current_sleep = int(input())

if max_sleep >= current_sleep >= min_sleep:
    print('Это нормально')
elif current_sleep < min_sleep:
    print('Недосып')
elif current_sleep > max_sleep:
    print('Пересып')

'''

'''Требуется определить, является ли данный год високосным.

current_year = float(input())

if current_year % 4 == 0.0 and current_year % 100 != 0.0 or current_year % 400 == 0.0:
    print('Високосный')
else:
    print('Обычный')
'''

''' Таблица умножения

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(' ', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')

print('')
f = a
for i in range(a, b + 1):
    print(f, end='\t')
    f += 1
    for j in range(c, d + 1):
        print(j * i, end='\t')
    print('')

'''
'''
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = float(p*(p - a)*(p - b)*(p - c))
sqrt = math.sqrt(S)
print(sqrt)
'''

'''
A = int(input())


def vhodit(A):
    if -15 < A <= 12 or 14 < A < 17 or 19 <= A < math.inf:
        print(True)
    else:
        print(False)


vhodit(A)
'''
'''
КАЛЬКУЛЯТОР

a = float(input())
b = float(input())
result_S = float()
operation = str(input())


if operation == '*':
    result_S = a * b
elif operation == '+':
    result_S = a + b
elif operation == '-':
    result_S = a - b
elif operation == 'pow':
    result_S = a ** b
print(result_S)

if operation == 'div':
    try:
        result_S = a // b
    except ZeroDivisionError:
        print('Деление на 0!')
    else:
        print(result_S)
elif operation == 'mod':
    try:
        result_S = a % b
    except ZeroDivisionError:
        print('Деление на 0!')
    else:
        print(result_S)
elif operation == '/':
    try:
        result_S = a / b
    except ZeroDivisionError:
        print('Деление на 0!')
    else:
        print(result_S)
'''

'''
a = float(input())
b = float(input())
result_S = float()
operation = str(input())


if operation == '*':
    result_S = a * b
elif operation == '+':
    result_S = a + b
elif operation == '-':
    result_S = a - b
elif operation == 'pow':
    result_S = a ** b
print(result_S)

try:
    1 / b
except ZeroDivisionError:
    print('Деление на 0!')
    if operation == 'div':
        result_S = a // b
        print(result_S)
    elif operation == 'mod':
        result_S = a % b
        print(result_S)
    elif operation == '/':
        result_S = a / b
        print(result_S)

'''

figure = str(input())
a = int(input())
b = int(input())
c = int(input())
result_S = float()
pi = 3.14
half_perimiter = (a + b + c) / 2.0

if figure == 'прямоугольник':
    result_S = a * b
elif figure == 'треугольник':
    result_S = (half_perimiter * (half_perimiter - a) * (half_perimiter - b) * (half_perimiter - c)) ** 0.5
elif figure == 'круг':
    result_S = pi * (a ** 2)

print(result_S)


