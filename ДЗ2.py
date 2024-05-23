import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 3  # Верхня межа

# Розміри прямокутника
width = b - a
height = f(b)

def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині під параболою y = x^2."""
    return y <= f(x)

# Генерація випадкових точок
points = [(random.uniform(a, b), random.uniform(0, height)) for _ in range(15000)]

# Відбір точок, що знаходяться всередині фігури
inside_points = [point for point in points if is_inside(point[0], point[1])]

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)

integral_result = (b**3 / 3) - (a**3 / 3) # Теоретична площа фігури через інтеграл

Sm = (M / N) * (width * height)  # Площа за методом Монте-Карло

# Обчислення інтеграла через функцію quad
result, error = spi.quad(f, a, b)

print(f"Інтеграл, обчислений за допомогою scipy: {result} (похибка: {error})")
# Виведення результатів
print(f"Кількість точок всередині під кривою: {M}, загальна кількість точок: {N}")
print(f"Теоретична площа фігури: {integral_result}, площа за методом Монте-Карло: {Sm}")