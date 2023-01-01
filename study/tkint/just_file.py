# import the modules
import tkinter
import random
import time
import numpy as np
from threading import Timer


class Game:
    def __init__(self, parent, canvas_to_change, final_label):
        self.parent = parent
        self.canvas = canvas_to_change
        self.label = final_label
        self.score = 0
        self.num_left = 20
        self.colors = ['green', 'red']
        self.time_array = np.array([], dtype='float')
        self.timer_list = [2.243, 5.2341, 3.123]

    def start(self):
        if self.num_left > 0:
            color_choice = random.choice(self.colors)
            if color_choice == 'green':
                self.choose_green()
            else:
                self.choose_red()

            self.num_left -= 1

        elif self.num_left == 0:
            result = 20 / (20 - self.score) * self.time_array.mean()
            self.label.config(text='Ваш результат: ' + str(result), background='white')

    def choose_green(self):
        time_begin = time.time()
        self.canvas.create_rectangle(10, 10, 80, 80, fill='green')
        timer_time = random.choice(self.timer_list)
        self.parent.bind('<Button-1>', self.make_choice(time_begin, timer_time))
        time.sleep(timer_time)
        self.canvas.create_rectangle(10, 10, 80, 80, fill='white')

    def choose_red(self):
        time_begin = time.time()
        self.canvas.create_rectangle(10, 10, 80, 80, fill='red')
        first_timer = random.choice(self.timer_list)
        time.sleep(first_timer)
        self.canvas.create_rectangle(10, 10, 80, 80, fill='white')

        second_timer = random.choice(self.timer_list)
        time.sleep(second_timer)
        self.canvas.create_rectangle(10, 10, 80, 80, fill='gray')

        overall_timer = first_timer + second_timer
        self.parent.bind('<Button-1>', self.make_choice(time_begin, overall_timer))

    def make_choice(self, time_begin, time_in_timer):
        reaction = time.time() - time_begin
        if reaction > time_in_timer:
            self.time_array = np.append(self.time_array, reaction - time_in_timer)
            self.score += 1
        else:
            self.time_array = np.append(self.time_array, reaction)


root = tkinter.Tk()
root.geometry('400x400')
root.title('Color game')
greeting = """
Green - когда white.
Red - когда gray.
Нажмите Enter чтобы начать."""
first_label = tkinter.Label(root, text=greeting, font=('Helvetica', 12))
first_label.pack()
result_label = tkinter.Label(root, font=('Helvetica', 12))
result_label.pack()
shapes = tkinter.Canvas(root)
shapes.pack()
game = Game(root, shapes, result_label)
root.bind('<Return>', game.start)
root.mainloop()
