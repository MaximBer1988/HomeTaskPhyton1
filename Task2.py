# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = bool(input("Введите число: "))
y = bool(input("Введите число: "))
z = bool(input("Введите число: "))
if not(x or y or z) == (not x and  not y and  not z):
  print("Истинно")
else:
  print("Не истинно")
