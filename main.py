from tkinter import *
import time
import random

window = Tk()  # создаю окно с игровым полем
window.title("Game")
window.resizable(0, 0)  # запрещаем менять размеры окна
window.wm_attributes('-topmost', 1)  #  помещаем игровое окно выше остальных окон

canvas = Canvas(window, width=500, height=400, highlightthickness=0)
canvas.pack()

window.update()


class Ball:

    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        self.canvas.move(self.id, 245, 100)  # помещаем шарик в точку с координатами 245, 100

        starts = [-2, -1, 1, 2]  # список возможных напаврлений для старта
        random.shuffle(starts)
        self.x = starts[0]  # вектор движения шарика
        self.y = -2  # уменьшаем значени по оси y, шарик в начале падает вниз

        self.canvas_height = self.canvas.winfo_height()  # шарик узнает свою высоту и ширину
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False  # достиг шарик дна или нет, пока не достиг значени False

    def hit_paddle(self, pos):
        """Обработка касания платформы"""
        paddle_pos = self.canvas.coords(self.paddle.id)  # получаем координаты платформы через объект paddle
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # если координаты касания совпадают с координатами платформы
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()  # увеличиваем счет
                return True
        return False

    def draw(self):
        """Обрабатываем отрисовку шарика"""
        self.canvas.move(self.id, self.x, self.y)  # передвигаем шарик на заданные координаты
        pos = self.canvas.coords(self.id)  # запоминаем новые координаты шарика
        if pos[1] <= 0:
            self.y = 2  # задаем падение на следующем шаге
        if pos[3] >= self.canvas_height:  # если шарик правым нижним углом коснулся дна
            self.hit_bottom = True  # помечаем в отдельной переменной
            canvas.create_text(250, 120, text="Вы проиграли",
                               font=("Courier", 30), fill="red")
        if self.hit_paddle(pos):  # если было касание платформы
            self.y = -2  # отправляем шарик наверх
        if pos[0] <= 0:  # если коснулись левой стенки
            self.x = 2  # движемся вправо
        if pos[2] >= self.canvas_width:  # если коснулись правой стенки
            self.x = -2  # движемся влево
