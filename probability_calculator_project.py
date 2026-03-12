"""
Proyecto: Calculadora de Probabilidades
"""
import copy
import random

class Hat:
    """
    Clase que representa un sombrero con bolas de diferentes colores. 
    Permite dibujar bolas al azar y calcular probabilidades de eventos específicos.
    """
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """
        Dibuja un número específico de bolas al azar del sombrero.
        """
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat_obj, expected_balls, num_balls_drawn, num_experiments):
    """
    Realiza un experimento para calcular la probabilidad de 
    obtener una combinación específica de bolas al dibujar el sombrero.
    """
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat_obj)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        if all(drawn_balls.count(color) >= count for color, count in expected_balls.items()):
            success_count += 1

    return success_count / num_experiments

hat1 = Hat(yellow = 3, blue = 2, green = 6)
hat2 = Hat(red = 5, orange = 4)
hat3 = Hat(red = 5, orange = 4, black = 1, blue = 0, pink = 2, striped = 9)

hat = Hat(black=6, red=4, green=3)
PROBABILITY = experiment(hat_obj=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(PROBABILITY)
