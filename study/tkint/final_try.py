# import the modules
import tkinter
import random
import time
import numpy as np
from threading import Timer

max_num_left = 20
score = 0
numbers_left = 20
color = 'red'
colors = ['green', 'red']
time_begin = 0
time_end = 0
result_time = []


def start(event):
    global score, numbers_left, colors, time_begin, time_end, color

    if numbers_left < max_num_left:
        calculate_time(1)

    if numbers_left > 0:
        # time.sleep(5)
        text = f'Осталось: {numbers_left}'
        first_label.config(text=text)
        random.shuffle(colors)
        color = colors[0]

        if color == 'green':
            time_begin = time.time()
            action = Timer(1, lambda: left_shapes.create_rectangle(500, 500, 200, 200, fill='green'))
            action.start()
            # time.sleep(3)
            action = Timer(4, lambda: left_shapes.create_rectangle(500, 500, 200, 200, fill='white'))
            action.start()

        else:
            time_begin = time.time()
            action = Timer(1, lambda: left_shapes.create_rectangle(500, 500, 200, 200, fill='red'))
            action.start()

            action = Timer(3, lambda: left_shapes.create_rectangle(500, 500, 200, 200, fill='white'))
            action.start()

            action = Timer(5, lambda: left_shapes.create_rectangle(500, 500, 200, 200, fill='gray'))
            action.start()

        numbers_left -= 1

    if numbers_left == 0:
        text = 'Тест завершен.'
        first_label.config(text=text)
        try:
            result = 5 / score * np.mean(result_time)
        except ZeroDivisionError:
            result = 5 / (score + 1) * np.mean(result_time)

        result_label.config(text='Ваш результат: ' + str(round(result, 2)))

        action = Timer(10, lambda: root.quit())
        action.start()


def calculate_time(event):
    global score
    global time_end

    time_end = time.time()
    res = time_end - time_begin
    if color == 'green':
        if res > 5:
            res -= 5
            score += 1
            result_time.append(res)

    else:
        if res > 8:
            res -= 8
            score += 1
            result_time.append(res)


root = tkinter.Tk()
root.geometry('900x500')
root.resizable(False, False)
root.title('Color game')
# root.columnconfigure(2)
# root.rowconfigure(2)
greeting = """
Здравствуйте! Вам предлагается пройти тест на переключаемость внимания.
На экране будут поочередно появляться цветовые сигналы в виде красного, зеленого, белого и серого квадратов.
Если на экране появился зеленый квадрат, то нужно нажать Enter, как только он пропадет и
на его месте появится белый квадрат.
Если на экране появился красный квадрат, то нужно нажать Enter, как только появившийся еа его месте
белый квадрат исчезнет.
Нажмите Enter чтобы начать."""
first_label = tkinter.Label(root, text=greeting, font=('Helvetica', 12))
# first_label.grid(column=2, row=0)
first_label.pack()
result_label = tkinter.Label(root, font=('Helvetica', 12))
# result_label.grid(column=2, row=1)
result_label.pack()
left_shapes = tkinter.Canvas(root)
# left_shapes.grid(column=2, row=5)
left_shapes.pack(fill=tkinter.BOTH)
root.bind('<Return>', start)
# root.bind('<Button-1>', calculate_time)
root.mainloop()
