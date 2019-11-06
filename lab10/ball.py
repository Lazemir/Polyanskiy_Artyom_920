class Ball():
	def __init__(self, canv, x, y, r, color, vx, vy):
		""" Конструктор класса Ball

		Args:
		x - начальное положение мяча по горизонтали
		y - начальное положение мяча по вертикали
		"""
		
		self.canv = canv
		
		
		self.live = 1
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.vx = vx
		self.vy = vy
		self.id = self.canv.create_oval(
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r,
				fill=self.color
		)

	def move(self, A):
		"""Переместить мяч по прошествии единицы времени.

		Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
		self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
		и стен по краям окна (размер окна 800х600).
		"""
		self.vy += A
		
		self.x += self.vx
		self.y += self.vy
		self.canv.move(self.id, self.vx, self.vy)

	def hittest(self, obj):
		"""Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

		Args:
			obj: Обьект, с которым проверяется столкновение.
		Returns:
			Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
		"""
		if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2: 
			return True
		else:
			return False
	
	def wallhit(self, wall1_x, wall1_y, wall2_x, wall2_y, N):
		res = True
		if self.x - self.r <= wall1_x and self.vx < 0:
			self.vx *= -1 * N
		elif self.x + self.r >= wall2_x and self.vx > 0:
			self.vx *= -1 * N
		if self.y - self.r <= wall1_y and self.vy < 0:
			self.vy *= -1 * N
		elif self.y + self.r >= wall2_y and self.vy > 0:
			self.vy *= -1 * N
		else:
			res = False
		return res


	
	def __del__(self):
		self.canv.delete(self.id)
