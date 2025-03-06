import math
import matplotlib.pyplot as plt
import numpy as np

class Octagon:
    def __init__(self, side_length):
        self.side = side_length
        self.angle = 135  # Фиксированный угол (в градусах)
        self.k = 1 + math.sqrt(2) # Константа k

    def circumcircle_radius(self):
        "Радиус описанной окружности"
        return self.side*self.k/2
    
    def circumcircle_area(self):
        "Площадь описанной окружности"
        r = self.circumcircle_radius()
        return math.pi*r*2
    
    def incircle_radius(self):
        "Радиус вписанной окружности"
        return self.side/(2*(math.sqrt(2)+1))
    
    def incircle_area(self):
        "Площадь вписанной окружности"
        r = self.incircle_radius()
        return math.pi*r*2
    
    def area(self):
        "Площадь октогона"
        return 2*self.side**2*(1 + math.sqrt(2))
    
    def perimetr(self):
        "Периметр октогона"
        return self.side*8
    
    def draw(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_aspect('equal')
        ax.set_xlim(-self.k * self.side, self.k * self.side)
        ax.set_ylim(-self.k * self.side, self.k * self.side)

        theta = np.linspace(0, 2 * np.pi, 9)[:-1] + np.pi / 8
        x = self.side * np.cos(theta) * self.k / 2
        y = self.side * np.sin(theta) * self.k / 2
        ax.fill(x, y, color='lightblue', label='Октогон')

        r_circ = self.circumcircle_radius()
        circle_circ = plt.Circle((0,0), r_circ, color="blue", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)
        r_in = self.incircle_radius()
        circle_in = plt.Circle((0,0), r_in, color="red", fill=False, label="Вписаннная окружность")
        ax.add_patch(circle_in)


        plt.legend()
        plt.grid()
        plt.show()

octagon = Octagon(10)
print("Радиус описанной окружности", octagon.circumcircle_radius())
print("Площадь описанной окружности", octagon.circumcircle_area())
print("Радиус вписанной окружности", octagon.incircle_radius())
print("Площадь вписанной окружности", octagon.incircle_area())
print("Площадь октогона", octagon.area())
print("Периметр октогона", octagon.perimetr())

octagon.draw()