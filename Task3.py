# 3 Запишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = float(input("Введите координату X: "))
y = float(input("Введите координату Y: "))
if x>0 and y>0 and x != 0 and y !=0:
  print("Точка в координатной плоскости 1")
elif x<0 and y>0 and x != 0 and y != 0:
  print("Точка в координатной плоскости 2") 
elif x<0 and y<0 and x != 0 and y !=0:
  print("Точка в координатной плоскости 3")
elif x>0 and y<0 and x != 0 and y !=0:
  print("Точка в координатной плоскости 4")
else:
  print("Введите занчение отличное от 0")
