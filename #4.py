import math

name = input("Введіть функцію (sqrt, sin) або константу (pi): ")

if name == "pi":
    print("Число π:", math.pi)
elif name == "sqrt":
    x = float(input("Введіть число для sqrt: "))
    print("Квадратний корінь: ", math.sqrt(x))
elif name == "sin":
    degrees = float(input("Введіть кут у градусах: "))
    sin_value = math.sin(math.radians(degrees))
    print("Синус кута:", sin_value)
else:
    print("Такої функції або константи немає")