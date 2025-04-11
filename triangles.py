import math
import os

os.system("cls")

class Triangle:
    def __init__(self, right, left, bottom):
        self.right = right
        self.left = left
        self.bottom = bottom
        
class Equilateral(Triangle):
    def __init__(self, right, left, bottom):
        super().__init__(right, left, bottom)
    
    def calculate_area(self):
        s = (self.right + self.left + self.bottom) / 2
        area = math.sqrt(s*(s - self.right) * (s - self.left) * (s - self.bottom))
        return area
    
class Scalene(Triangle):
    def __init__(self, right, left, bottom):
        super().__init__(right, left, bottom)
        
    def calculate_area(self):
        s = (self.right + self.left + self.bottom) / 2
        area = math.sqrt(s*(s - self.right) * (s - self.left) * (s - self.bottom))
        return area
    
class Isosceles(Triangle):
    def __init__(self, right, left, bottom):
        super().__init__(right, left, bottom)
    
    def calculate_area(self):
        s = (self.right + self.left + self.bottom) / 2
        area = math.sqrt(s*(s - self.right) * (s - self.left) * (s - self.bottom))
        return area
    
equilateral_triangle = Equilateral(5, 5, 5)
equilateral_rounded_area = round(equilateral_triangle.calculate_area(), 2)
print(f"El área del Triangulo Equilateral es: {equilateral_rounded_area}m²")

scalene_triangle = Scalene(6, 5, 8)
rounded_scalene_area = round(scalene_triangle.calculate_area(), 2)
print(f"El área del Triángulo Escaleno es: {rounded_scalene_area}m²")

isosceles_triangle = Isosceles(7, 7, 4)
rounded_isosceles_triangle = round(isosceles_triangle.calculate_area(), 2)
print(f"El área del Triángulo Isósceles es: {rounded_isosceles_triangle}m²")