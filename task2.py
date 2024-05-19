import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

# Перевірка знаходження точки під параболою
def is_inside(a, b, x, y):
    return y <= f(x)

# Виконання функції Монте-Карло
def monte_carlo_simulation(a, b, num_points):
    points = [(random.uniform(a, b), random.uniform(0, b**2)) for _ in range(num_points)]
    inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

    M = len(inside_points)
    N = len(points)
    area = (M / N) * (b - a) * (b**2)
    return area, points, inside_points

# Розміри прямокутника
a = 0  # Нижня межа
b = 2  # Верхня межа

# Теоретична площа
result, error = spi.quad(f, 0, b)
num_points = 15000

average_area, points, inside_points = monte_carlo_simulation(a, b, num_points)
print(f"Теоретична площа фігури: {result}")
print(f"Середня площа фігури за {num_points} точок: {average_area}")

# Додавання точок на графік
if points and inside_points:  # Додаємо перевірку на наявність точок
    points_x, points_y = zip(*points)
    inside_points_x, inside_points_y = zip(*inside_points)

    # Всі точки
    ax.scatter(points_x, points_y, c='blue', s=1, alpha=0.5, label='Всі точки')

    # Точки, що знаходяться під параболою
    ax.scatter(inside_points_x, inside_points_y, c='green', s=1, alpha=0.5, label='Точки під параболою')

    ax.legend()
else:
    print("Точки не згенеровані")

plt.show()