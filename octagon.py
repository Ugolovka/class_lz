import math
import matplotlib.pyplot as plt
import numpy as np

class Octagon:
    def __init__(self, side_length):
        self.side = side_length
        self.angle = 135  
        self.k = 1 + math.sqrt(2)
    def circumcircle_radius(self):
        ""
        return self.side * self.k/2
    def circumcircle_area(self):
        ""
        return math.pi * r **2
    def incircle_radius(self):
        ""
        return self.side/(2*(math.sqrt(2)+1))
    def incircle_area(self):
        ""
        return math.pi * r**2
    def area(self):
        ""
        return 2*self.side**2(1+math.sqrt(2))
    def perimetr(self):
        ""
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
        circle_circ = plt.Circle((0,0), r_circ, color="", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)
        r_in = self.incircle_radius()
        circle_in = plt.Circle((0,0), r_in, color="", fill=False, label="Вписаннная окружность")
        ax.add_patch(circle_in)


        plt.legend()
        plt.grid()
        plt.show()

        octagon = Octagon(5)
        



















    def sounding(self):
        print(f"Чик-чирик")
    def eating(self):
        print(f"птица {self.name} питается")
    def sleeping(self):
        print(f"птица {self.name} спит")
    def flying_range(self,N):
        if self.f_a==True:
            print(self.size*N)
        else:
            print("Error")
    def __del__(self):
        print("dell done")

vorobey= Birds("vorobey", True, 50)
vorobey.flying_range(10)



  def __init__(self, side_length):
        self.side = side_length
        self.angle = 135  # Фиксированный угол (в градусах)
        self.k = 1 + math.sqrt(2)  # Константа k