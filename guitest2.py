from Tkinter import *

class GUI(Frame) :
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(row=1, column=1)
        self.create_widgets()

    def create_widgets(self) :
        # Empty spaces for grid
        self.empty_0 = Label(self, text="    ")
        self.empty_1 = Label(self, text="    ")
        self.empty_2 = Label(self, text="    ")
        self.empty_3 = Label(self, text="    ")
        self.empty_4 = Label(self, text="    ")
        self.empty_5 = Label(self, text="    ")
        self.empty_6 = Label(self, text="    ")
        self.empty_7 = Label(self, text="    ")
        self.empty_8 = Label(self, text="    ")

        # All the buttons, sliders and entry's
        self.button_0 = Button(self, text="Play", command=self.playButton)
        self.button_1 = Button(self, text="Stop", command=self.stopButton)
        self.button_2 = Button(self, text="Generate", command=self.generateButton)
        self.amountLabel = Label(self, text="Amount")
        self.slider = Scale(self)
        self.slider.config(orient=HORIZONTAL)
        self.slider.config(length=200, width=20, sliderlength=10)
        self.slider.config(from_=0, to_=100, tickinterval=50)
        self.slider.set(50)
        self.bpmLabel = Label(self, text="bpm:")
        self.bpmEntry = Entry(self)
        self.bpmEntry.config(width=3)
        self.bpmEntry.insert(0, 120)

        # All the widgets placed in the grid!
        self.empty_0.grid(row=0, column=0)
        self.empty_1.grid(row=1, column=0)
        self.button_0.grid(row=1, column=1)
        self.button_1.grid(row=1, column=2)
        self.button_2.grid(row=1, column=3)
        self.empty_2.grid(row=1, column=5)
        self.empty_3.grid(row=2, column=0)
        self.empty_4.grid(row=3, column=0)
        self.amountLabel.grid(row=3, column=1, columnspan=4)
        self.empty_5.grid(row=4, column=0)
        self.slider.grid(row=4,column=1, columnspan=4)
        self.empty_6.grid(row=5, column=0)
        self.empty_7.grid(row=6, column=0)
        self.bpmLabel.grid(row=6, column=1, sticky=E)
        self.bpmEntry.grid(row=6, column=2, sticky=W)
        self.empty_8.grid(row=7, column=0)

    def playButton(self) :
        return (self.bpmEntry.get())
        return 1

    def stopButton(self) :
        return 0

    def generateButton(self) :
        return self.slider.get()

root = Tk()
root.title("Drum Pattern Generator")
app = GUI(root)
root.mainloop()
