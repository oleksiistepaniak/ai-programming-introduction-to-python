import math
from typing import Union

def get_triangle_area(a: float, b: float, c: float) -> float:
    """Calculate the area of a triangle using Heron's formula."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# My variant is 11
area = get_triangle_area(12, 8, 5)
print(f"Area of the triangle: {area:.2f}")

def calculate_y(a: float, x: float) -> Union[str, float]:
    """Calculate the value of Y based on the given formula, handling math errors."""
    try:
        if not -1 <= x <= 1:
            return "Math error: acos domain out of range"

        numerator = math.exp(-x) + math.log(math.acos(x)) + 1 / math.atan(x) - 1.2 * (math.cos(x) ** 2)

        term = x + a**2
        denominator = math.sqrt(a * (a * math.exp(1) + 3.5e-2)) - math.copysign(abs(term) ** (1/3), term) - 0.3

        return numerator / denominator
    except ValueError as e:
        return f"Math error: {e}"

a = 0.5
x = 3.4e-4

result = calculate_y(a, x)
print(f"Y = {result}")
