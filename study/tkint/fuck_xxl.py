# import the modules
import tkinter
import random
import time
import numpy as np
from threading import Timer

time_array = np.array([], dtype='float')


def startGame():
    global time_array

    def local_timer(start_time):
        global time_array, root
        nonlocal time_in_color
        
        time_in_color = time.time() - start_time

        if time_in_color > white_timer_interval:
            time_array = np.append(time_array,
                                   time_in_color - white_timer_interval)

        else:
            time_array = np.append(time_array, time_in_color)

    def show_white_in_green():
        nonlocal white_timer_interval

        white_timer_interval = np.random.choice(timer_array)
        action = Timer(white_timer_interval, lambda: label.config(background='white'))
        action.start()

    def show_white_in_red():
        nonlocal white_timer_interval

        white_timer_interval = np.random.choice(timer_array)
        action_show = Timer(white_timer_interval,
                            lambda: label.config(background='white'))
        action_show.start()

        white_timer_interval += np.random.choice(timer_array)
        action_hide = Timer(white_timer_interval, lambda: label.config(background='gray'))
        action_hide.start()

    def choose_green():
        nonlocal time_begin, score
        global root

        time_begin = time.time()
        root.bind('<Return>', local_timer(time_begin))
        # root.bind('Button-1', local_timer(time_begin))
        label.config(background='green')
        show_white_in_green()

        if time_in_color > white_timer_interval:
            score += 1

    def choose_red():
        nonlocal time_begin, score
        global root

        time_begin = time.time()
        root.bind('<Return>', local_timer(time_begin))
        label.config(background='red')
        show_white_in_red()

        if time_in_color > white_timer_interval:
            score += 1

    # necessary variables
    score = 0
    num_left = 20
    time_begin = 0
    time_end = 0
    white_timer_interval = 0
    time_in_color = 0
    colors = ['red', 'green']
    timer_array = np.array([2.42, 4.234, 5.123])

    if num_left > 0:
        color_choice = random.choice(colors)
        if color_choice == 'green':
            choose_green()
            num_left -= 1
            root.bind('<Return>', startGame())
        else:
            choose_red()
            num_left -= 1
            root.bind('<Return>', startGame())

    elif num_left == 0:
        result = 20 / (20 - score) * time_array.mean()
        label.config(text='ваш результат: ' + str(result), background='white')


root = tkinter.Tk()
root.title('COLOR GAME')
root.geometry('375x200')
instructions = tkinter.Label(root, text="""
                            Красный цвет - нажать пробел после изчезновения белого.
                            Зеленый цвет - нажать пробел после появления белого.
                            Нажмите Enter, чтобы продолжить.""", font=('Helvetica', 12))
instructions.pack()
label = tkinter.Label(root)
label.pack()

root.bind('<Return>', startGame())
root.mainloop()
