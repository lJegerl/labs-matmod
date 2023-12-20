import numpy as np
import random
import math
import scipy.stats as sts

# Нормальное распределение
def normal_dist(m, s2, N, n):
    arr = []
    for _ in range(n):
        x = 0
        for _ in range(N):
            x += random.random()
        x -= N / 2
        x = m + np.sqrt(12 * s2 / N) * x
        arr.append(x)
    return np.array(arr)


# Распределение Лапласа
def laplace_dist(b):
    u = random.random() - 0.5
    x = 0 - b * math.copysign(1, u) * math.log(1 - 2 * abs(u))
    return x


# Логистическое распределение
def logisctic_dist(a, b):
    u = random.random()
    x = a + b * math.log(u / (1 - u))
    return x


# Распределение Коши
def koshi_dist(a, b, n):
    return a + b * np.tan(np.pi * (np.random.rand(n) - 0.5))


# Распределение Вейбулла
def weibull_dist(a, b, n):
    return b * (-np.log(1 - np.random.rand(n))) ** (1 / a)


# Матожидание
def math_expectation(array):
    return np.sum(array) / len(array)


# Дисперсия
def dispersion(array):
    return math_expectation(array ** 2) - math_expectation(array) ** 2


def median(array, n):
    a = sorted(array)
    return (a[int(n / 2 - 1)] + a[int(n / 2)]) / 2


if __name__ == '__main__':
    print('Нормальное распределение')
    m, s2, N, n = 0, 1, 48, 10000
    a = normal_dist(m, s2, N, n)
    print(f'Матожидание {math_expectation(a)}')
    print(f'Истинное матожидание {m}')
    print(f'Дисперсия {dispersion(a)}')
    print(f'Истинная дисперсия {s2}')
    print('#' * 50)
    print('Распределение Лапласа')
    lmb, x = 0, 0.5
    arr = [laplace_dist(x) for _ in range(n)]
    print(f'Матожидание {math_expectation(arr)}')
    print(f'Истинное матожидание {lmb}')
    print('#' * 50)
    print("Распределение Вейбулла")
    a = 1
    b = 0.5
    arr = weibull_dist(a, b, n)
    print("Истинное матожидание")
    print(b * math.gamma(1 + 1 / a))
    print("Полученное матожидание")
    print(math_expectation(arr))
    print("Истинная дисперсия")
    print((b ** 2) * (math.gamma(1 + 2 / a) - (math.gamma(1 + 1 / a)) ** 2))
    print("Полученная дисперсия")
    print(dispersion(arr))
    print('#' * 50)
    print('Распределение Коши')
    a, b = -1, 1
    print(f'Медиана {median(koshi_dist(a, b, n), n)}')
    print(f'Истинная медиана {a}')
    print('#' * 50)
    print('Распределение Логистическое')
    a, b = 2, 3
    arr = [logisctic_dist(a, b) for _ in range(10000)]
    print(f'Математические ожидание {math_expectation(arr)}')
    print(f'Истинное математическое ожидание {a}')
    print(f'Дисперсия {sum((x - math_expectation(arr)) ** 2 for x in arr) / len(arr)}')
    print(f'Истинная дисперсия {math.pi ** 2 / 3 * b ** 2}')
