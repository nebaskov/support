# import the modules
import tkinter
import random
import time
import numpy as np

score = 0
numbers_left = 5
color = 'red'
colors = ['green', 'red']
time_begin = 0
time_end = 0
result_time = []


def start(event):
    global score, numbers_left, colors, time_begin, time_end, color

    if numbers_left > 0:
        # time.sleep(5)
        text = f'Осталось: {numbers_left}'
        first_label.config(text=text)

        color = random.choice(colors)
        if color == 'green':
            time_begin = time.time()
            left_shapes.create_rectangle(40, 40, 80, 80, fill='green')

        else:
            left_shapes.create_rectangle(40, 40, 80, 80, fill='red')

        numbers_left -= 1

    if numbers_left == 0:
        text = 'Тест завершен.'
        first_label.config(text=text)
        final_result = 5 / score * np.mean(result_time)
        result_label.config(text='Ваш результат: ' + str(final_result))


def calculate_green(event):
    global score, color

    end = time.time()
    result = end - time_begin
    if color == 'green':
        score += 1
    result_time.append(result)

    start()


def calculate_red(event):
    global score, color

    end = time.time()
    result = end - time_begin
    if color == 'red':
        score += 1
    result_time.append(result)



root = tkinter.Tk()
root.geometry('400x400')
root.title('Color game')
greeting = """
Здравствуйте! Вам предлагается пройти тест на переключаемость внимания.
Если на экране зеленый сигнал, нажмите левую кнопку при появлении белого сигнала.
Если на экране красный сигнал, нажмите левую кнопку при исчезновении белого сигнала.
Нажмите Enter чтобы начать."""
first_label = tkinter.Label(root, text=greeting, font=('Helvetica', 12))
first_label.pack()
result_label = tkinter.Label(root, font=('Helvetica', 12))
result_label.pack()
left_shapes = tkinter.Canvas(root)
left_shapes.pack()
# right_shapes = tkinter.Canvas(root)
# right_shapes.pack(side='right')
root.bind('<Return>', start)
root.bind('<Left>', calculate_red)
root.bind('<Right>', calculate_red)
root.mainloop()
