# https://www.youtube.com/watch?v=HVQeV7xe310

from Tkinter import *

class Application(Frame):
  """ A GUI app """

  def __init__(self,master):
    """ Constructor: init the frame """
    Frame.__init__(self,master)
    self.grid()
    self.button_clicks=0
    self.create_widgets()

  def create_widgets(self):
    self.button1 =  Button(self, text="Button 1")
    self.button1.grid()

    self.button2 =  Button(self, text="Button 2")
    self.button2.grid()

    self.button3 =  Button(self, text="Button 3")
    self.button3.grid()

    # self.slider4 =

# create a window
root = Tk()

# set window props
root.title("ME Gui")
root.geometry("300x200")

app = Application(root)

root.mainloop()
