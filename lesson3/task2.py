from graph import *
import random
import math

width, height = windowSize()

def half_ellipse(xc, yc, rx, ry, fi: int):
    pos = []
    fi *= math.pi / 180
    for i in range(181):
        x = round(rx * math.cos(i * math.pi / 180))
        y = round(ry * math.sin(i * math.pi / 180))

        x0 = x * math.cos(fi) - y * math.sin(fi)
        y0 = x * math.sin(fi) + y * math.cos(fi)
        
        pos.append((xc + x0, yc + y0))
    polygon(pos)

#background
penColor('#fed5a2')
brushColor('#fed5a2')
rectangle(0, 0, width, height // 6)

penColor('#fed5c4')
brushColor('#fed5c4')
rectangle(0, height // 6, width, height // 3)

penColor('#fed594')
brushColor('#fed594')
rectangle(0, height // 3, width, height // 2)

penColor('#b38694')
brushColor('#b38694')
rectangle(0, height // 2, width, height)


#sun
penColor('#fcee21')
brushColor('#fcee21')
circle(width // 2, height // 6, 50)

#mountains
N = 20

penColor('#fc9831')
brushColor(penColor())

pos1 = [(0, height // 3)]

for i in range(N + 1):
        pos1.append((i * width // N, height // 3 - i * (height // 3 - height // 4) // N - random.randint(0, 100) ))

pos1.append((width, height // 4))

polygon(pos1)


penColor('#ac4334')
brushColor(penColor())

pos2 = [(0, height // 2)]

for i in range(N + 1):
	pos2.append((i * width // N, height // 2 - random.randint(0, 100))) 

pos2.append((width, height // 2))

polygon(pos2) 

for i in range(random.randint(1, 3)):
    n = random.randint(2, 7)
    j = random.randint(1, n - 1)
    half_ellipse(j * width // n, height // 2, 50, 100, 180)

run()
