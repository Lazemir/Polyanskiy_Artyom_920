from graph import *

windowSize(400, 600)
canvasSize(2000, 2000)
width, height = windowSize()

def ellipse(xc, yc, rx, ry, x0 = 0, y0 = 0, fi = 0):
    pos = []
    fi *= math.pi / 180
    for i in range(361):
        x = round(rx * math.cos(i * math.pi / 180))
        y = round(ry * math.sin(i * math.pi / 180))

        xN = (x - x0) * math.cos(fi) - (y - y0) * math.sin(fi)
        yN = (x - x0) * math.sin(fi) + (y - y0) * math.cos(fi)
        
        x = x0 + xN
        y = y0 + yN
        
        pos.append((xc + x, yc + y))
    polygon(pos)

def tree (x,y,h,l, fi = 0):
    penSize(2)
    brushColor(0,100,0)
    penColor(0,255,127)
    ellipse(y, x-h, l, 1.3*h, x, y, fi) #верхнее
    ellipse(y, x, 2*l, h, x, y, fi) #серединка
    ellipse(y, x+h, l, h, x, y, fi) #нижнее
    
    brushColor(255,182,193)
    ellipse(y-1.5*l, x, l/3.7, h/3.7, x, y, fi) #4
    brushColor(255,192,203)
    ellipse(y+3.4*l/7, x-11.2*h/7, l/3.7, h/3.7, x, y, fi) #1
    ellipse(y+1.5*l, x+l/40, l/3.7, h/3.7, x, y, fi) #2
    ellipse(y+4*l/7, x+11*h/7, l/3.7, h/3.7, x, y, fi) #3
    
    brushColor(211,211,211)
    rectangle(y-l/4, x+2*h, y+l/4, x+3.3*h, x, y, fi) #ствол

def unicorn (x, y, l, f, fi):
    
    brushColor('red')
    a=y+f*0.6*l
    b=x-2.5*l
    c=2.2*l/4
    d=l/4
    
    brushColor(255,215,0)
    penColor(255,215,0)
    ellipse(a+f*l/2, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*2*l/5, b+l/5, c, d, x, y, fi)
    ellipse(a, b, c, d, x, y, fi)
    brushColor(173, 255, 47)
    penColor(173,255,47)
    ellipse(a+f*6*l/7, b-5*l/7, c/1.3, d/1.3, x, y, fi)
    ellipse(a+f*l/5, b-2*l/5, c/1.2, 1.2*d, x, y, fi)
    ellipse(a+f*4*l/7, b-l, c/1.1, d/1.5, x, y, fi)
    ellipse(a, b+0.9*l, c, d, x, y, fi)
    brushColor(176, 224, 230)
    penColor(176,224,230)
    ellipse(a+f*l/5, b-4*l/5, c, d, x, y, fi)
    ellipse(a-f*l/5, b+l/5, c/1.2, d/2, x, y, fi)
    ellipse(a-f*2*l/5, b+3*l/5, c, 1.3*d, x, y, fi)
    brushColor(100, 149, 237)
    penColor(100,149,237)
    ellipse(a+f*1.2*l/2, b+4*l/5, c, d/1.4, x, y, fi)
    ellipse(a-f*3*l/4, b+l, c, d/1.7, x, y, fi)
    ellipse(a-f*l, b+5*l/6, c, d/1.7, x, y, fi)
    
    a=y+f*1.3*l
    b=x-2.7*l
    c=2.2*l/4
    d=l/4
    
    brushColor(240, 128, 128)
    penColor(240,128,128)
    ellipse(a+f*l/2, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*2*l/5, b+l/5, c, d, x, y, fi)
    ellipse(a, b, c, d, x, y, fi)
    brushColor(255, 20, 147)
    penColor(255,20,147)
    ellipse(a+f*6*l/7, b-5*l/7, c/1.3, d/1.3, x, y, fi)
    ellipse(a+f*l/5, b-2*l/5, c/1.2, 1.2*d, x, y, fi)
    ellipse(a+f*4*l/7, b-l, c/1.1, d/1.5, x, y, fi)
    brushColor(255, 140, 0)
    penColor(255,140,0)
    ellipse(a, b+0.9*l, c, d, x, y, fi)
    ellipse(a+f*l/5, b-4*l/5, c, d, x, y, fi)
    ellipse(a-f*l/5, b+l/5, c/1.2, d/2, x, y, fi)
    brushColor(255,255, 0)
    penColor(255,255,0)
    ellipse(a-f*2*l/5, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*1.2*l/2, b+4*l/5, c, d/1.4, x, y, fi)
    ellipse(a-f*3*l/4, b+l, c, d/1.7, x, y, fi)
    ellipse(a-f*l, b+5*l/6, c, d/1.7, x, y, fi)
    
    brushColor('white')
    penColor('white')

    rectangle(y+f*0.7*l, x, y+f*2*l, x-2.1*l, x, y, fi)
    rectangle(y-f*l/2, x, y-f*l, x+2.3*l, x, y, fi)
    rectangle(y-f*1.5*l, x, y-f*1.9*l, x+2.8*l, x, y, fi)
    rectangle(y+f*l/2, x, y+f*l, x+3*l, x, y, fi)
    rectangle(y+f*1.5*l, x, y+f*1.9*l, x+2.3*l, x, y, fi)
              
    ellipse(y, x, 2.2*l, l, x, y, fi)
    ellipse(y+f*1.3*l, x-2.5*l, 1.4*l/1.5, l/1.5, x, y, fi)
    ellipse(y+f*1.94*l, x-2.4*l, 2.5*l/3, l/3, x, y, fi) #telo

    brushColor(255,182,193)
    penColor(255,182,193)
    polygon([(y+f*1.45*l, x-3.1*l),(y+f*1.7*l, x-3*l),(y+f*1.83*l, x-5*l)]) #dildo
    
    a=y-f*2.2*l
    b=x
    c=2.2*l/4
    d=l/4
    
    brushColor(255, 215, 0)
    penColor(255,215,0)
    ellipse(a+f*l/2, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*2*l/5, b+l/5, c, d, x, y, fi)
    ellipse(a, b, c, d, x, y, fi)
    brushColor(255, 0, 255)
    penColor(255,0,255)
    ellipse(a+f*6*l/7, b-5*l/7, c/1.3, d/1.3, x, y, fi)
    ellipse(a+f*l/5, b-2*l/5, c/1.2, 1.2*d, x, y, fi)
    ellipse(a+f*4*l/7, b-l, c/1.1, d/1.5, x, y, fi)
    brushColor(138, 43, 226)
    penColor(138,43,226)
    ellipse(a, b+0.9*l, c, d, x, y, fi)
    ellipse(a+f*l/5, b-4*l/5, c, d, x, y, fi)
    ellipse(a-f*l/5, b+l/5, c/1.2, d/2, x, y, fi)
    brushColor(210, 105, 30)
    penColor(210,105,30)
    ellipse(a-f*2*l/5, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*1.2*l/2, b+4*l/5, c, d/1.4, x, y, fi)
    ellipse(a-f*3*l/4, b+l, c, d/1.7, x, y, fi)
    ellipse(a-f*l, b+5*l/6, c, d/1.7, x, y, fi)
    

    a=y+f*l/4
    b=x-2*l
    c=2.2*l/4
    d=l/4
    
    brushColor('red')
    penColor('red')
    ellipse(a+f*l/2, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*2*l/5, b+l/5, c, d, x, y, fi)
    ellipse(a, b, c, d, x, y, fi)
    brushColor(106, 90, 205)
    penColor(106,90,205)
    ellipse(a+f*6*l/7, b-5*l/7, c/1.3, d/1.3, x, y, fi)
    ellipse(a+f*l/5, b-2*l/5, c/1.2, 1.2*d, x, y, fi)
    ellipse(a+f*4*l/7, b-l, c/1.1, d/1.5, x, y, fi)
    brushColor(218,165,32)
    penColor(218,165,32)
    ellipse(a, b+0.9*l, c, d, x, y, fi)
    ellipse(a+f*l/5, b-4*l/5, c, d, x, y, fi)
    ellipse(a-f*l/5, b+l/5, c/1.2, d/2, x, y, fi)
    brushColor(128, 0, 128)
    penColor(128,0,128)
    ellipse(a-f*2*l/5, b+3*l/5, c, 1.3*d, x, y, fi)
    ellipse(a+f*1.2*l/2, b+4*l/5, c, d/1.4, x, y, fi)
    ellipse(a-f*3*l/4, b+l, c, d/1.7, x, y, fi)
    ellipse(a-f*l, b+5*l/6, c, d/1.7, x, y, fi)

    brushColor(238,130,238)
    penColor(238,130,238)
    circle(y+f*1.75*l, x-2.7*l, l/7)
    brushColor('black')
    penColor('black')
    circle(y+f*1.79*l, x-2.7*l, l/20)
    brushColor('white')
    penColor('white')
    circle(y+f*1.7*l, x-2.75*l, l/30)




def sun(xc, yc, r, color1, color2):
    N = 100
    step_color_r = (color2[0] - color1[0]) / N
    step_color_g = (color2[1] - color1[1]) / N
    step_color_b = (color2[2] - color1[2]) / N
    step_radius = r / N
    
    for i in range(1, N):
        penColor(round(color2[0] - i * step_color_r), round(color2[1] - i * step_color_g), round(color2[2] - i * step_color_b))
        brushColor(penColor())
        circle(xc, yc, r - round(i * step_radius))

#penSize(3)
brushColor(0,255,255)
penColor(0,255,255)
rectangle(0,0, 400, 270, 0, 0, 0)
brushColor(0,255,0)
penColor(0,255,255)
rectangle(0, 270, 400, 600, 0, 0, 0)

tree(140, 120, 49, 49)
tree(240, 30, 49, 30)
tree(270, 145, 30, 40)
tree(350, 100, 37, 37)
tree(450, 44, 37,37)

penColor('black')
brushColor('black')
unicorn(300, 250, 15, 1, 45)
unicorn(480, 190, 30, 1, 0)
unicorn(400,360,20, -1, 0)
unicorn(260,340,10, -1, 0)

#penSize(1)
#for i in range (100):
#polygon([(0,i*20),(2000,i*20)])
#polygon([(i*20,0),(i*20, 2000)])
sun(round(3 * width / 4), round(width / 4), 90, (252, 221, 87), (0, 255, 255)) 

ellipse(100, 100, 100, 50, 100, 100, 0)
ellipse(100, 100, 100, 50, 100, 100, 45)

ellipse(100, 100, 100, 50, 220, 220, 45)
ellipse(100, 100, 100, 50, 220, 220, 50)

run()
