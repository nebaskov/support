# import the modules
import tkinter
import random
import time
import numpy as np
from threading import Timer


class App(tkinter.Frame):
    def __int__(self, parent):
        super().__init__(parent)
        global root

        self.score = 0
        self.numbers_left = 20
        self.time_begin = None
        self.time_end = None
        self.colors = ['red', 'green']
        self.timer_array = np.array([2.42, 4.234, 5.123])
        self.time_array = np.array([], dtype='float')
        self.white_timer_interval = 0
        self.time_in_color = 0

        self.label = tkinter.Label(self, font=('Helvetica', 12))
        self.label.pack()

        root.bind('<Return>', self.startGame())
        root.bind('<space>', self.local_timer(self.time_begin))

    # function that will start the game.
    def startGame(self):

        if self.numbers_left == 20:
            self.time_begin = time.time()

        if self.numbers_left > 0:
            self.check()

        if self.numbers_left == 0:
            self.time_end = time.time()

            # compute and print test result
            result = 20 / (20 - self.score) * self.time_array.mean()
            self.label.config(text='Ваш результат: ' + str(result))

    def check(self):
        color_choice = random.choice(self.colors)
        if color_choice == 'green':
            self.choose_green()
        else:
            self.choose_red()

    def local_timer(self, start_time):
        self.time_in_color = time.time() - start_time

        if self.time_in_color > self.white_timer_interval:
            self.time_array = np.append(self.time_array,
                                        self.time_in_color - self.white_timer_interval)

        else:
            self.time_array = np.append(self.time_array, self.time_in_color)

    def show_white_in_green(self):
        self.white_timer_interval = np.random.choice(self.timer_array)
        action = Timer(self.white_timer_interval, lambda: self.label.config(background='white'))
        action.start()

    def show_white_in_red(self):
        self.white_timer_interval = np.random.choice(self.timer_array)
        action_show = Timer(self.white_timer_interval,
                            lambda: self.label.config(background='white'))
        action_show.start()

        self.white_timer_interval += np.random.choice(self.timer_array)
        action_hide = Timer(self.white_timer_interval, lambda: self.label.config(background='gray'))
        action_hide.start()

    def choose_green(self):
        self.time_begin = time.time()
        self.label.config(background='green')
        self.show_white_in_green()

        if self.time_in_color > self.white_timer_interval:
            self.score += 1

    def choose_red(self):
        self.time_begin = time.time()
        self.label.config(background='green')
        # self.label.config(background=ImageColor.getcolor('green', mode='L'))
        self.show_white_in_red()

        if self.time_in_color > self.white_timer_interval:
            self.score += 1


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('COLOR GAME')
    root.geometry('375x200')
    instructions = tkinter.Label(root, text="""
                    Красный цвет - нажать пробел после изчезновения белого.
                    Зеленый цвет - нажать пробел после появления белого.
                    Нажмите Enter, чтобы продолжить.""",
                                 font=('Helvetica', 12))
    instructions.pack()
    frame = App(root)
    frame.pack()
    root.mainloop()
