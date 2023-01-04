from tkinter import *


class Ball:
    root = Tk()
    root.geometry('600x600')
    canv = Canvas(bg='black')
    canv.pack(fill=BOTH, expand=1)

    initial_speed = 4
    initial_y_position = 150

    def __init__(self):
        # начальная скорость
        self.speedY = Ball.initial_speed

        # размер
        self.r = 20

        # начальное положение (центр окна)
        self.x = 300
        self.y = Ball.initial_y_position

        self.gravitation = 0.87731

    def update(self):

        self.speedY = self.speedY + self.gravitation
        self.y += self.speedY

        # удалить мячик
        Ball.canv.delete('ball')
        # нарисовать в новом месте
        oval = Ball.canv.create_oval(self.x - self.r,
                                     self.y - self.r,
                                     self.x + self.r,
                                     self.y + self.r,
                                     fill='gray', tag='ball')

        if self.y > 550:
            self.speedY = -self.speedY
        if self.y == 549.9794399999997:
            self.restart()

        Ball.root.after(30, self.update)

    def restart(self):
        self.y = Ball.initial_y_position
        self.speedY = Ball.initial_speed


Program = Ball()
Program.update()
Program.root.mainloop()