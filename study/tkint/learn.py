import tkinter as tk
import time
import random
from threading import Timer

class App(tk.Tk):
    
    def __init__(self):

        super.__init__()

        self.main_frame = tk.Frame(self)
        self.sup_frame = tk.Frame(self)

        self.start_button = tk.Button(self.main_frame, text='start', command=self.start())

        self.continue_button = tk.Button(self.main_frame, text='continue')
        self.continue_button.bind('<Return>', self.timer())
        
        self.time = []
        self.error = 0


    def start(self):
        
        greeting = '''
        Здравствуйте! Вам предстоит принять участие в тесте.

        Для ответа нажмите f

        Для продолжения нажмите Enter

        Желаем удачи!
        '''

        start_label = tk.Label(self.main_frame, text=greeting)
        start_label.pack(fill='both')

        
    def show_color(self, color):

        self.canvas = tk.Canvas(self.sup_frame)
        self.canvas.create_rectangle(100, 200, 100, 200, fill=color)
        self.canvas.pack(fill='both')

    
    def reset_frame(self):
        self.canvas.destroy()


    def calc_time(self, start):
        self.time = self.time.append(start-time.time())


    def timer(self):
        color = random.choice(['red', 'green'])
        action = Timer(1.0, self.show_color(color))
        action.start()
        
        show_white = Timer(random.choice([2.3, 5.0, 3.6]), self.show_color('white'))
        show_white.start()
        
        if color == 'red':
            time_point = random.choice([2.214, 4.35, 7.321, 5.23])
            reset = Timer(time_point, self.reset_frame())
            reset.start()

            start_point = time.time()
            self.check_button = tk.Button(self.sup_frame)
            self.check_button.bind('<f>', self.calc_time(start_point))
            
            if self.time[-1] < time_point:
                self.error += 1


        elif color=='green':

            start_point = time.time()
            time_point = random.choice([2.214, 4.35, 7.321, 5.23])
            reset = Timer(time_point, self.reset_frame())
            reset.start()

            self.check_button = tk.Button(self.sup_frame)
            self.check_button.bind('<f>', self.calc_time(start_point))
            
            if self.time[-1] > time_point:
                self.error += 1


app = App()

app.mainloop()