V = 10 # Максимальная скорость шариков
livetime = 1000 # Время жизни шариков

from tkinter import *
from random import randrange as rnd, choice, random
import time
import pickle

root = Tk()
root.geometry('800x600')
root.title('Шарики')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH,expand=1)

lbl_score = Label(canv)
lbl_score.pack()
score = 0
total = -2

scores = ()

class Ball:
    id = 0
    def create(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.id = canv.create_oval(round(self.x - self.r), round(self.y - self.r), round(self.x + self.r),
                         round(self.y + self.r), fill=self.color, width=0)

        direction = [-1, 1]
        self.step_x = V * choice(direction) * random()
        self.step_y = V * choice(direction) * random()

    def move(self):
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.step_x *= -1
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.step_y *= -1
        self.x += self.step_x
        self.y += self.step_y
        canv.move(self.id, self.step_x, self.step_y)


    def delete(self):
        canv.delete(self.id)

    def check(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= self.r**2

colors = ['red','orange','yellow','green','blue']

def create(ball):
    global total
    total += 1
    ball.delete()
    ball.create(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors))
    ball.redraw_id = root.after(livetime, create, ball)
    if total > 0:
        lbl_score['text'] = 'Счет: ' + str(score) + '/' + str(total)
    else:
        lbl_score['text'] = 'Счет: ' + str(score) + '/0'

def move(ball):
    ball.move()
    root.after(10, move, ball)

def click(event, ball):
    global lbl_score, score
    if ball.check(event.x, event.y):
        score += 1
        if total > 0:
            lbl_score['text'] = 'Счет: ' + str(score) + '/' + str(total)
        else:
            lbl_score['text'] = 'Счет: ' + str(score) + '/0'
        root.after_cancel(ball.redraw_id)
        create(ball)


ball_1 = Ball()
ball_2 = Ball()

create(ball_1)
move(ball_1)
create(ball_2)
move(ball_2)

canv.bind('<Button-1>', lambda event: (click(event, ball_1), click(event, ball_2)))

lbl_score['text'] = 'Счет: 0/0'

mainloop()
