import math

def area_of_triangle(a, b, c):

    s = (a + b + c) / 2 

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area
side_a = 3
side_b = 4
side_c = 5
area_result = area_of_triangle(side_a, side_b, side_c)
print("Area of triangle:", area_result)