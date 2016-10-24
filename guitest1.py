from Tkinter import *

class GUIclass(Frame) :
    def __init__(self, master) :
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :
        self.titleLabel = Label(self, text="Python Drum Generator")
        self.titleLabel.grid(row=0,)

        self.button_0 = Button(self, text= "Play")
        self.button_0.grid(row=1, column=0)
        self.button_1 = Button(self, text= "Stop")
        self.button_1.grid(row=1, column=1)

        self.bpmLabel = Label(self, text="set bpm:")
        self.bpmLabel.grid(row=1, column=0, sticky=E)
        self.bpmEntry = Entry(self)
        self.bpmEntry.grid(row=2, column=1)


        self.button_2 = Button(self, text="Generate drum pattern")
        self.button_2.grid(row=3, columnspan=2)

        self.slider1 = Scale(self)
        self.slider1.config(orient=HORIZONTAL)
        self.slider1.config(length=500)
        self.slider1.config(width=10)
        self.slider1.config(sliderlength=50)
        self.slider1.config(from_=0)
        self.slider1.config(to_=100)
        self.slider1.set(50)
        self.slider1.grid(row=4)

root = Tk()

root.title("Python Drum Generator")

gui = GUIclass(root)

root.mainloop()
