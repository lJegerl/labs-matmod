import random
import math

def monte_carlo_integration(func, a, b, n):
    total_sum = 0

    for _ in range(n):
        x = random.uniform(a, b)
        total_sum += func(x)

    result = (b - a) * total_sum / n
    return result

# Интеграл от 0 до 1 (x * e^(x^2)) dx
def func_a(x):
    return x * math.exp(x**2)

a_a, b_a = 0, 1
n_a = 10000

result_a = monte_carlo_integration(func_a, a_a, b_a, n_a)
print("Приближенное значение для интеграла a):", result_a)



# Интеграл от 0 до pi/2 (cos(x) / sqrt(x)) dx
def func_b(x):
    return math.cos(x) / math.sqrt(x)

a_b, b_b = 0, math.pi / 2
n_b = 10000

result_b = monte_carlo_integration(func_b, a_b, b_b, n_b)
print("Приближенное значение для интеграла б):", result_b)



# Интеграл от 0 до pi/2 ((1 + x^2)) / (1 + x^6)) dx
def func_c(x):
    return ((1 + x**2)/(1 + x**6))

a_c, b_c = 0, math.pi / 2
n_c = 10000

result_c = monte_carlo_integration(func_c, a_c, b_c, n_c)
print("Приближенное значение для интеграла в):", result_c)