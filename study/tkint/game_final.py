# import the modules
import tkinter
import random
import time
import numpy as np
from threading import Timer

score = 0
numbers_left = 20
time_begin = None
time_end = None
colors = ['red', 'green']
timer_array = np.array([2.42, 4.234, 5.123])
time_array = np.array([], dtype='float')
white_timer_interval = 0
time_in_color = 0


def startGame():
    global time_begin
    global time_end
    global label
    global numbers_left
    global final_label

    if numbers_left > 0:
        check()
        numbers_left -= 1

    elif numbers_left == 0:
        # compute and print test result
        result = 20 / (20 - score) * time_array.mean()
        final_label.config(text='Ваш результат: ' + str(result))


def check():
    global colors

    color_choice = random.choice(colors)
    if color_choice == 'green':
        choose_green()
    else:
        choose_red()


def local_timer():
    global time_in_color
    global time_array
    global white_timer_interval
    global numbers_left
    global time_begin

    time_in_color = time.time() - time_begin
    if time_in_color > white_timer_interval:
        time_array = np.append(time_array,
                               time_in_color - white_timer_interval)
    else:
        time_array = np.append(time_array, time_in_color)


def show_white_in_green():
    global white_timer_interval
    global label
    global time_array

    white_timer_interval = np.random.choice(timer_array)
    time.sleep(white_timer_interval)
    label.create_oval(10, 10, 80, 80, fill='white')
    time.sleep(2)
    white_timer_interval += 2


def clear_label():
    global label

    label.config()


def show_white_in_red():
    global white_timer_interval
    global time_array
    global label

    white_timer_interval = np.random.choice(timer_array)
    time.sleep(white_timer_interval)
    label.create_oval(10, 10, 80, 80, fill='white')
    time.sleep(2)

    second_white_timer = np.random.choice(timer_array)
    white_timer_interval += second_white_timer + 2

    time.sleep(second_white_timer)
    label.create_oval(10, 10, 80, 80, fill='gray')


def choose_green():
    global time_begin
    global label
    global time_in_color
    global white_timer_interval
    global score
    global root

    time_begin = time.time()
    label.create_oval(10, 10, 80, 80, fill='green')
    show_white_in_green()
    if time_in_color > white_timer_interval:
        score += 1


def choose_red():
    global time_begin
    global label
    global time_in_color
    global white_timer_interval
    global score
    global root

    time_begin = time.time()
    label.create_oval(10, 10, 80, 80, fill='red')
    show_white_in_red()
    if time_in_color > white_timer_interval:
        score += 1


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("COLOR GAME")
    root.geometry("375x200")
    instructions = tkinter.Label(root, text="Green or Red", font=('Helvetica', 12))
    instructions.pack()
    scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
    scoreLabel.pack()
    numberLabel = tkinter.Label(root, text="Colors left: " + str(numbers_left), font=('Helvetica', 12))
    numberLabel.pack()
    label = tkinter.Canvas(root)
    label.pack(fill='both')
    final_label = tkinter.Label(root, font=('Helvetica', 12))
    final_label.pack()
    root.bind('<Return>', startGame())
    root.mainloop()
