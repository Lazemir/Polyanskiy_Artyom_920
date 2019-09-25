from graph import *

width, height = windowSize()
penColor(200, 200, 200)
brushColor(200, 200, 200)
rectangle(0, 0, width, height)

penColor(0, 0, 0)
brushColor(255, 255, 0)

circle(200, 200, 100)

brushColor(0, 0, 0)

rectangle(150, 240, 250, 260)

brushColor(255, 0, 0)
circle(150, 170, 20)
circle(250, 170, 15)


brushColor(0, 0, 0)
circle(150, 170, 7)
circle(250, 170, 7)

penSize(10)
line(100, 110, 180, 160)
line(300, 130, 220, 160)

run()
