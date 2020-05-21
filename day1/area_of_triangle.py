import math;

main_side = int(input("Основание: "));
second_side = int(input("Первая сторона: "));
third_side = int(input("Вторая сторона: "));

p = float((main_side+second_side+third_side)/2);
h = float((2*math.sqrt(p*(p-main_side)*(p-second_side)*(p-third_side))) / main_side)

s = float((main_side*h)/2);

print("Площадь треугольника: ", round(s,2))
