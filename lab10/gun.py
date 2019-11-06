V = 20
A = 0.1
N = 0.8

from random import randrange as rnd, choice
import random
import tkinter as tk
import math, time, ball

root = tk.Tk()
root.title ('Шарики')
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

balls = []

class Gun():
	def __init__(self):
		self.f2_power = 10
		self.f2_on = 0
		self.an = 1
		self.id = canv.create_line(20,450,50,420,width=7)

	def fire2_start(self, event):
		self.f2_on = 1

	def fire2_end(self, event):
		"""Выстрел мячом.

		Происходит при отпускании кнопки мыши.
		Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
		"""
		global balls, bullet
		bullet += 1
		new_ball = ball.Ball(canv, self.xe, self.ye, 15, choice(['blue', 'green', 'red', 'brown']), V / 100 * self.f2_power * math.cos(self.an), V / 100 * self.f2_power * math.sin(self.an))
		balls.append(new_ball)
		self.f2_on = 0
		self.f2_power = 10

	def targetting(self, event=0):
		"""Прицеливание. Зависит от положения мыши."""
		if event:
			if (event.x-20) > 0:
				self.an = math.atan((event.y-450) / (event.x-20))
			elif (event.x-20) == 0:
				if (event.y-450) > 0:
					self.an = math.pi/2
				else:
					self.an = -math.pi / 2
			else:
				self.an = math.pi + math.atan((event.y - 450) / (event.x - 20))
		if self.f2_on:
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')

		self.xe = 20 + max(self.f2_power, 20) * math.cos(self.an)
		self.ye = 450 + max(self.f2_power, 20) * math.sin(self.an)
		canv.coords(self.id, 20, 450, self.xe, self.ye)

	def power_up(self):
		if self.f2_on:
			if self.f2_power < 100:
				self.f2_power += 1
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')

class Target(ball.Ball):
	points = 0
	id_points = canv.create_text(30, 30, text=points, font=('', 28))

	def hit(self, points=1):
		"""Попадание шарика в цель."""
		Target.points += points
		canv.itemconfig(Target.id_points, text=Target.points)

def new_game(event=''):
	global balls, bullet, sreen1, canv
	g1 = Gun()
	bullet = 0
	balls = []
	targets = []
	canv.bind('<Button-1>', g1.fire2_start)
	canv.bind('<ButtonRelease-1>', g1.fire2_end)
	canv.bind('<Motion>', g1.targetting)
	
	for i in range(random.randint(1, 3)):
		t = Target(canv, rnd(600, 780), rnd(300, 550), rnd(2, 50), 'red', V / 2**0.5 * random.random(), V / 2**0.5 * random.random())
		targets.append(t)
	    
	canv.itemconfig(screen1, text='')
	
	while targets or balls:
		for t in list(targets):
			if not t.live:
				targets.remove(t)
				del t
				continue
			t.move(0)
			t.wallhit(0,0, 800, 600, 1)
		
		for b in list(balls):
			b.move(A)
			if b.wallhit(0,0, 800, 600, N) and abs(b.vy) <= A or not targets:
				balls.remove(b)
				del b
				continue
			for t in targets:
				if b.hittest(t) and targets:
					t.live = 0
					t.hit()
		
		if not targets:
			canv.bind('<Button-1>', '')
			canv.bind('<ButtonRelease-1>', '')
			if 10 <= bullet % 100 <= 20 or 5 <= bullet % 10 <= 9 or bullet % 10 == 0:
				shot = ' выстрелов'
			elif bullet % 10 == 1:
				shot = ' выстрел'
			else:
				shot = ' выстрела'
			canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + shot)
			print('Yes')


		canv.update()
		time.sleep(0.03)
		g1.targetting()
		g1.power_up()
	canv.delete(g1.id)
	root.after(2000, new_game)

screen1 = canv.create_text(400, 300, text='', font=('', 28))

new_game()

root.mainloop()
