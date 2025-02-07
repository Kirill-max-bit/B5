import numpy as np
from scipy.integrate import quad

# Определяем функцию
def f(x):
    return 0.5 * x + 1

# Вычисляем площадь под кривой от 0 до 2
area_under_curve, _ = quad(f, 0, 2)

# Площадь прямоугольника под прямой y = 2 от 0 до 2
area_rectangle = 2 * 2

# Искомая площадь фигуры
area_figure = area_under_curve - area_rectangle

print(f"Приближенная площадь фигуры: {area_figure:.4f}")
