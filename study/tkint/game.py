# import the modules
import tkinter
import random
import time


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
score = 0
numbers_left = 20
time_begin = 0
time_end = 0


# function that will start the game.
def startGame(event):
    global score
    global numbers_left
    global time_begin
    global time_end
    if numbers_left == 20:
        time_begin = time.time()
    if numbers_left > 0:
        e.focus_set()
        if e.get() == str(int(numbers[0]) % 2):
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(numbers)
        label.config(text=numbers[0])
        scoreLabel.config(text="Score: " + str(score))
        numbers_left -= 1
        numberLabel.config(text="Number left: " + str(numbers_left))
    if numbers_left == 0:
        time_end = time.time()
        label.config(text=str(time_end-time_begin))


root = tkinter.Tk()
root.title("ODD GAME")
root.geometry("375x200")
instructions = tkinter.Label(root, text="Четное (0) или нечетное (1)", font=('Helvetica', 12))
instructions.pack()
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
numberLabel = tkinter.Label(root, text="Numbers left: " + str(numbers_left), font=('Helvetica', 12))
numberLabel.pack()
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
