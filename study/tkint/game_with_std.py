# import the modules
import tkinter
import random
import time
import numpy as np
from PIL import ImageColor
from threading import Timer

# colors = ['red', 'green']
# score = 0
# numbers_left = 20
# time_begin = 0
# time_end = 0


class Game(tkinter.Tk):


    def __init__(self) -> None:

        super.__init__(self)

        self.title('COLOR GAME')
        self.geometry('375x200')
        
        self.instructions = tkinter.Label(self, text="Четное (0) или нечетное (1)", font=('Helvetica', 12))
        self.instructions.pack()
        self.scoreLabel = tkinter.Label(self, text="Press enter to start", font=('Helvetica', 12))
        self.scoreLabel.pack()
        self.numberLabel = tkinter.Label(self, text="Numbers left: " + str(numbers_left), font=('Helvetica', 12))
        self.numberLabel.pack()
        self.label = tkinter.Label(self, font=('Helvetica', 60))
        self.label.pack()

        # e = tkinter.Entry(root)
        self.bind('<Return>', self.startGame())

        self.score = 0
        self.numbers_left = 20
        self.time_begin = 0
        self.time_end = 0
        self.colors = ['red', 'green']

        # array to collect time for each answer
        self.time_array = np.array([], dtype='float')


    # function that will start the game.
    def startGame(self):
        if self.numbers_left == 20:
            self.time_begin = time.time()
        if self.numbers_left > 0:
            self.bind('<space>', self.check())
        if self.numbers_left == 0:
            self.time_end = time.time()

            # label.config(text=str(time_end-time_begin))
            self.label.config(text=str(self.time_array.std()))  # print standard deviation of the time array


    def check(self):
        local_start = time.time()  # start time for the answer
        color_choice = random.choice(self.colors)
        timer_time = np.array([2, 3, 5])

        self.label.config(background=ImageColor.getcolor(color_choice))
        self.scoreLabel.config(text="Score: " + str(self.score))
        self.numbers_left -= 1
        self.numberLabel.config(text="Number left: " + str(self.numbers_left))

        local_end = time.time()  # end time for the answer
        local_result_time = local_start - local_end
        self.time_array = np.append(self.time_array, local_result_time)  # add time taken for the answer to the array


    def show_white(self, previous_color):
        if previous_color == 'green':
            reaction_time_start = time.time()
            self.label.config(background=ImageColor.getcolor('white'))

            def check_time():
                global green_result

                green_result = reaction_time_start - time.time()
                return 
        
            self.bind('<space>', check_time)

game = Game()
# root.title("COLOR GAME")
# root.geometry("375x200")
# instructions = tkinter.Label(root, text="Четное (0) или нечетное (1)", font=('Helvetica', 12))
# instructions.pack()
# scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
# scoreLabel.pack()
# numberLabel = tkinter.Label(root, text="Numbers left: " + str(numbers_left), font=('Helvetica', 12))
# numberLabel.pack()
# label = tkinter.Label(root, font=('Helvetica', 60))
# label.pack()
# # e = tkinter.Entry(root)
# root.bind('<Return>', startGame)
# # e.pack()
# e.focus_set()
game.mainloop()
