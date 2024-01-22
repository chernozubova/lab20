import time
import sys

class Foo:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return self.city + " " + self.street

class Poo:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return "{} {}".format(self.city, self.street)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factor(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


start_time = time.time()
ineffect_list = []
for i in range(100001):
    ineffect_list.append(i)
end_time = time.time()
print(f'Неэффективное время:{end_time-start_time}')
print(f'Неэффективное использование памяти: {sys.getsizeof(ineffect_list)} байт')

start = time.time()
effect_list = list(range(100001))
end = float(time.time())
print(f'Эффективное время:{end-start}')
print(f'Эффективное использование памяти: {sys.getsizeof(effect_list)} байт\n')

st_time = time.time()
a = factorial(928)
en_time = time.time()
print(f'Неэффективное время:{en_time-st_time}')
print(f'Неэффективное использование памяти: {sys.getsizeof(factorial)} байт')

s_time = time.time()
b = factor(928)
e_time = time.time()
print(f'Эффективное время:{e_time-s_time}')
print(f'Эффективное использование памяти: {sys.getsizeof(factor)} байт\n')

Start_time = time.time()
for i in range(10001):
    c = Poo("Москва", "Набережная")
    c.__str__()
End_time = float(time.time())
print(f'Неэффективное время:', float(End_time-Start_time))
print(f'Неэффективное использование памяти: {sys.getsizeof(Foo)} байт')

starttime = float(time.time())
for i in range(10001):
    d = Poo("Москва", "Набережная")
    d.__str__()
endtime = float(time.time())
print(f'Эффективное время:', float(endtime-starttime))
print(f'Эффективное использование памяти: {sys.getsizeof(Poo)} байт')