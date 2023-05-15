import math
import time
from mouse import move

radius = 50
angle_step = 0.1

x0, y0 = 500, 500

while True:
    for angle in range(0, 360):
        x = int(x0 + radius * math.cos(angle))
        y = int(y0 + radius * math.sin(angle))

        move(x, y)

        time.sleep(angle_step)