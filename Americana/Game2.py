import math
import time


def donut_animation():
    width = 80
    height = 40
    a = width / 3
    b = height / 6
    frame = [[' ' for _ in range(width)] for _ in range(height)]
    while True:
        for row in frame:
            print(''.join(row))
        for theta in range(0, 628, 2):
            cos_theta = math.cos(theta / 100)
            sin_theta = math.sin(theta / 100)

            for phi in range(0, 628, 4):
                cos_phi = math.cos(phi / 100)
                sin_phi = math.sin(phi / 100)
                x = a + a * cos_theta * cos_phi
                y = b + b * sin_theta
                z = a * cos_theta * sin_phi
                screen_x = int(x * 2 / (z + 4)) + width // 2
                screen_y = int(y / (z + 4)) + height // 2
        time.sleep(0.1)
        frame = [[' ' for _ in range(width)] for _ in range(height)]