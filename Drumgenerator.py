import random
from Tkinter import *
import pygame
import time
import pygame.midi

# ------------------------------------------------------------------------------
AMOUNT = 50
gen = 0

# Pattern lists
KICK=[]
SNARE=[]
CLAP=[]
CH=[]
OH=[]

# Midi notes
MIDIKICK = 36
MIDISNARE = 38
MIDICLAP = 34
MIDICH = 42
MIDIOH = 46

for I in range(0,16) :
    KICK.append([0,0])
    SNARE.append([0,0])
    CLAP.append([0,0])
    CH.append([0,0])
    OH.append([0,0])

# ------------------------------------------------------------------------------
class GUI(Frame) :
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        self.playButton()
        self.stopButton()
        self.generateButton()

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
        print (self.slider.get())
        return self.slider.get()
# ------------------------------------------------------------------------------

guiclass = GUI

# Gives random int between 0 - 100
def R100() :
    x =  random.randint(1, 100)
    return x

# Gives random velocity. First argument is the initial velocity, second is
# the devider for the minimum and maximum for random. Example:
# Rvel(100, 0.2) gives a random int between 80 and 120.
def Rvel(x, y) :
    if y < 0 :
        Y = 0 # Devider cant go below 0
    if y > 1:
        Y = 1 # Devider cant go above 1
    min = int(x * (1 - y))
    max = int(x * (1 + y))
    if min < 1 :
        min = 1
    if max > 127 :
        max = 127
    result = random.randint(min, max)
    return result

# Scaling function. Scales a value to a new minimum and maximum. Used in the
# chance() function.
def scale(x, oMin, oMax, nMin, nMax):
    if oMin == oMax:
        return None
    if nMin == nMax:
        return None

    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    reverseOutput = False
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

# Scales a int with the "AMOUNT" input for function notechance()
def chance(x, y) :
    if x <= 50 :
        resultx = scale(x, 0, 100, 100, 0)
    if x > 50 :
        resultx = x
    z = y * resultx
    result = x * z
    result = int(result)
    if result <= 1 :
        result = 2
    if result > 100 :
        result = 100
    return result

# Generates a list for pattern. Arguments: Chance of note being placed (this
# scales to the given "AMOUNT"), Velocity initial, Velocity devider (lookup
# Rvel() function)
def notechance(x, y, z) :
    list = [0, 0]
    if R100() < chance(AMOUNT, (0.0004 * x)) :
        list = [1, Rvel(y, z)]
    return list

# Can give amount of hits in a pattern. First argument is the list. This func-
# tion only works BEFORE the convertion to midi notes.
def countList(x) :
    y = 0
    for i in range(0, len(x)) :
        if x[i][0] == 1 :
            y = y + 1
    return y

# ------------------------------------------------------------------------------
while gen == 1 :
    # Generate kick
    whileVar1 = 0
    while whileVar1 == 0 :
        KICK[0] = notechance(100, 100, 0.1)
        KICK[4] = notechance(80, 90, 0.12)
        KICK[8] = notechance(90, 100, 0.1)
        KICK[12] = notechance(80, 100, 0.13)

        if KICK[4] == [0,0] :
            KICK[1] = notechance(20, 25, 0.8)
            KICK[2] = notechance(10, 50, 0.3)
            KICK[3] = notechance(60, 75, 0.5)
            KICK[5] = notechance(60, 75, 0.5)
        else :
            KICK[1] = notechance(20, 25, 0.8)
            KICK[2] = notechance(60, 50, 0.4)
            KICK[3] = notechance(30, 50, 0.2)
            KICK[5] = notechance(10, 20, 0.75)

        if KICK[8] == [0,0] :
            if KICK[5] == [0,0] :
                KICK[5] = notechance(35, 25, 0.8)
            KICK[6] = notechance(10, 50, 0.3)
            KICK[7] = notechance(60, 75, 0.5)
            KICK[9] = notechance(60, 75, 0.5)
        else :
            if KICK[5] == [0,0] :
                KICK[5] = notechance(20, 25, 0.8)
            KICK[6] = notechance(50, 50, 0.4)
            KICK[7] = notechance(30, 50, 0.2)
            KICK[9] = notechance(10, 50, 0.75)

        if KICK[12] == [0,0] :
            if KICK[9] == [0,0] :
                KICK[9] = notechance(35, 25, 0.8)
            KICK[10] = notechance(10, 50, 0.3)
            KICK[11] = notechance(60, 75, 0.5)
            KICK[13] = notechance(60, 75, 0.5)
        else :
            if KICK[9] == [0,0] :
                KICK[9] = notechance(20, 25, 0.8)
            KICK[10] = notechance(50, 50, 0.4)
            KICK[11] = notechance(30, 50, 0.2)
            KICK[13] = notechance(10, 50, 0.75)

        if KICK[13] == [0,0] :
            KICK[14] = notechance(60, 50, 0.5)
            if KICK[1] == [0,0] :
                KICK[15] = notechance(20, 50, 0.2)
            else :
                KICK[15] = notechance(10, 50, 0.2)
        else :
            KICK[14] = notechance(60, 50, 0.5)
            if KICK[1] == [0,0] :
                KICK[15] = notechance(50, 50, 0.2)
            else :
                KICK[15] = notechance(30, 50, 0.2)

        if countList(KICK) > 0 :
            whileVar1 = 1

    # Generate snare
    whileVar2 = 0
    while whileVar2 == 0 :
        if R100() < 50 :
            SNARE[4] = notechance(90, 100, 0.1)
            SNARE[12] = notechance(90, 100, 0.1)
        else :
            SNARE[8] = notechance(95, 100, 0.1)

        if SNARE[4] != [0,0] :
            KICK[4] = [0,0]
        if SNARE[8] != [0,0] :
            KICK[8] = [0,0]
        if SNARE[12] != [0,0] :
            KICK[12] = [0,0]

        if countList(KICK) >= 8 :
            SNARE[1] = notechance(20, 50, 0.2)

            if SNARE[1] == [0,0] :
                SNARE[2] = notechance(25, 50, 0.1)
            else :
                SNARE[2] = notechance(10, 20, 0.2)

            if SNARE[4] == [0,0] :
                SNARE[4] = notechance(10, 70, 0.5)

            if SNARE[4] == [0,0] :
                SNARE[3] = notechance(25, 60, 0.2)
                SNARE[5] = notechance(20, 40, 0.5)
            else :
                SNARE[3] = notechance(5, 20, 0.5)
                SNARE[5] = notechance(5, 20, 0.5)

            if SNARE[5] == [0,0] :
                SNARE[5] = notechance(10, 50, 0.2)

            if SNARE[5] == [0,0] :
                SNARE[6] = notechance(25, 50, 0.1)
            else :
                SNARE[6] = notechance(10, 20, 0.2)

            if SNARE[8] == [0,0] :
                SNARE[8] = notechance(10, 70, 0.5)

            if SNARE[8] == [0,0] :
                SNARE[7] = notechance(25, 60, 0.2)
                SNARE[9] = notechance(20, 40, 0.5)
            else :
                SNARE[7] = notechance(5, 20, 0.5)
                SNARE[9] = notechance(5, 20, 0.5)

            if SNARE[9] == [0,0] :
                SNARE[9] = notechance(10, 50, 0.2)

            if SNARE[9] == [0,0] :
                SNARE[10] = notechance(25, 50, 0.1)
            else :
                SNARE[10] = notechance(10, 20, 0.2)

            if SNARE[12] == [0,0] :
                SNARE[12] = notechance(10, 70, 0.5)

            if SNARE[12] == [0,0] :
                SNARE[11] = notechance(25, 60, 0.2)
                SNARE[13] = notechance(20, 40, 0.5)
            else :
                SNARE[11] = notechance(5, 20, 0.5)
                SNARE[13] = notechance(5, 20, 0.5)

            if SNARE[13] == [0,0] :
                SNARE[14] = notechance(20, 30, 0.5)
            else :
                SNARE[14] = notechance(5, 30, 0.5)

            if SNARE[1] == [0,0] :
                SNARE[15] = notechance(20, 30, 0.5)
            else :
                SNARE[15] = notechance(5, 30, 0.5)

        else :
            SNARE[1] = notechance(40, 50, 0.2)

            if SNARE[1] == [0,0] :
                SNARE[2] = notechance(50, 50, 0.1)
            else :
                SNARE[2] = notechance(20, 20, 0.2)

            if SNARE[4] == [0,0] :
                SNARE[4] = notechance(20, 70, 0.5)

            if SNARE[4] == [0,0] :
                SNARE[3] = notechance(50, 60, 0.2)
                SNARE[5] = notechance(40, 40, 0.5)
            else :
                SNARE[3] = notechance(10, 20, 0.5)
                SNARE[5] = notechance(10, 20, 0.5)

            if SNARE[5] == [0,0] :
                SNARE[5] = notechance(20, 50, 0.2)

            if SNARE[5] == [0,0] :
                SNARE[6] = notechance(50, 50, 0.1)
            else :
                SNARE[6] = notechance(20, 20, 0.2)

            if SNARE[8] == [0,0] :
                SNARE[8] = notechance(20, 70, 0.5)

            if SNARE[8] == [0,0] :
                SNARE[7] = notechance(50, 60, 0.2)
                SNARE[9] = notechance(40, 40, 0.5)
            else :
                SNARE[7] = notechance(10, 20, 0.5)
                SNARE[9] = notechance(10, 20, 0.5)

            if SNARE[9] == [0,0] :
                SNARE[9] = notechance(20, 50, 0.2)

            if SNARE[9] == [0,0] :
                SNARE[10] = notechance(50, 50, 0.1)
            else :
                SNARE[10] = notechance(20, 20, 0.2)

            if SNARE[12] == [0,0] :
                SNARE[12] = notechance(20, 70, 0.5)

            if SNARE[12] == [0,0] :
                SNARE[11] = notechance(50, 60, 0.2)
                SNARE[13] = notechance(40, 40, 0.5)
            else :
                SNARE[11] = notechance(10, 20, 0.5)
                SNARE[13] = notechance(10, 20, 0.5)

            if SNARE[13] == [0,0] :
                SNARE[14] = notechance(40, 30, 0.5)
            else :
                SNARE[14] = notechance(10, 30, 0.5)

            if SNARE[1] == [0,0] :
                SNARE[15] = notechance(40, 30, 0.5)
            else :
                SNARE[15] = notechance(10, 30, 0.5)

        if countList(SNARE) > 0 :
                whileVar2 = 1

    # Generate clap
    whileVar3 = 0
    while whileVar3 == 0 :
        if countList(SNARE) >= 5 :
            CLAP[0] = notechance(5, 60, 0.99)
            CLAP[1] = notechance(5, 60, 0.99)
            CLAP[2] = notechance(5, 60, 0.99)
            CLAP[3] = notechance(5, 60, 0.99)

            if SNARE[4] == [0,0] :
                CLAP[4] = notechance(50, 60, 0.99)
            else :
                CLAP[4] = notechance(5, 60, 0.99)

            CLAP[5] = notechance(5, 60, 0.99)
            CLAP[6] = notechance(5, 60, 0.99)
            CLAP[7] = notechance(5, 60, 0.99)

            if SNARE[8] == [0,0] :
                CLAP[8] = notechance(50, 60, 0.99)
            else :
                CLAP[8] = notechance(5, 60, 0.99)

            CLAP[9] = notechance(5, 60, 0.99)
            CLAP[10] = notechance(5, 60, 0.99)
            CLAP[11] = notechance(5, 60, 0.99)

            if SNARE[12] == [0,0] :
                CLAP[12] = notechance(50, 60, 0.99)
            else :
                CLAP[12] = notechance(5, 60, 0.99)

            CLAP[13] = notechance(5, 60, 0.99)
            CLAP[14] = notechance(5, 60, 0.99)
            CLAP[15] = notechance(5, 60, 0.99)

        else :
            CLAP[0] = notechance(10, 60, 0.99)
            CLAP[1] = notechance(10, 60, 0.99)
            CLAP[2] = notechance(10, 60, 0.99)
            CLAP[3] = notechance(10, 60, 0.99)

            if SNARE[4] == [0,0] :
                CLAP[4] = notechance(70, 60, 0.99)
            else :
                CLAP[4] = notechance(10, 60, 0.99)

            CLAP[5] = notechance(10, 60, 0.99)
            CLAP[6] = notechance(10, 60, 0.99)
            CLAP[7] = notechance(10, 60, 0.99)

            if SNARE[8] == [0,0] :
                CLAP[8] = notechance(70, 60, 0.99)
            else :
                CLAP[8] = notechance(10, 60, 0.99)

            CLAP[9] = notechance(10, 60, 0.99)
            CLAP[10] = notechance(10, 60, 0.99)
            CLAP[11] = notechance(10, 60, 0.99)

            if SNARE[12] == [0,0] :
                CLAP[12] = notechance(70, 60, 0.99)
            else :
                CLAP[12] = notechance(10, 60, 0.99)

            CLAP[13] = notechance(10, 60, 0.99)
            CLAP[14] = notechance(10, 60, 0.99)
            CLAP[15] = notechance(10, 60, 0.99)

        if countList(CLAP) > 0 :
            whileVar3 = 1

    # Generate closed hi-hat
    whileVar4 = 0
    while whileVar4 == 0 :
        CH[0] = notechance(50, 100, 0.2)
        CH[2] = notechance(50, 50, 0.99)
        CH[4] = notechance(50, 80, 0.2)
        CH[6] = notechance(50, 50, 0.99)
        CH[8] = notechance(50, 100, 0.2)
        CH[10] = notechance(50, 50, 0.99)
        CH[12] = notechance(50, 80, 0.2)
        CH[14] = notechance(50, 50, 0.99)

        if countList(CH) <= 5 :
            CH[1] = notechance(30, 50, 0.2)
            CH[3] = notechance(30, 50, 0.2)
            CH[5] = notechance(30, 50, 0.2)
            CH[7] = notechance(30, 50, 0.2)
            CH[9] = notechance(30, 50, 0.2)
            CH[11] = notechance(30, 50, 0.2)
            CH[13] = notechance(30, 50, 0.2)
            CH[15] = notechance(30, 50, 0.2)
        else :
            CH[1] = notechance(10, 50, 0.2)
            CH[3] = notechance(10, 50, 0.2)
            CH[5] = notechance(10, 50, 0.2)
            CH[7] = notechance(10, 50, 0.2)
            CH[9] = notechance(10, 50, 0.2)
            CH[11] = notechance(10, 50, 0.2)
            CH[13] = notechance(10, 50, 0.2)
            CH[15] = notechance(10, 50, 0.2)

        if countList(CH) > 0 :
            whileVar4 = 1

    # Generate open hi-hat
    whileVar5 = 0
    while whileVar5 == 0 :
        if countList(CH) <= 5 :
            OH[0] = notechance(20, 50, 0.75)
            OH[1] = notechance(30, 80, 0.5)
            OH[2] = notechance(20, 50, 0.75)
            OH[3] = notechance(30, 80, 0.5)
            OH[4] = notechance(20, 50, 0.75)
            OH[5] = notechance(30, 80, 0.5)
            OH[6] = notechance(20, 50, 0.75)
            OH[7] = notechance(30, 80, 0.5)
            OH[8] = notechance(20, 50, 0.75)
            OH[9] = notechance(30, 80, 0.5)
            OH[10] = notechance(20, 50, 0.75)
            OH[11] = notechance(30, 80, 0.5)
            OH[12] = notechance(20, 50, 0.75)
            OH[13] = notechance(30, 80, 0.5)
            OH[14] = notechance(20, 50, 0.75)
            OH[15] = notechance(30, 80, 0.5)
        else :
            OH[0] = notechance(10, 50, 0.75)
            OH[1] = notechance(15, 80, 0.5)
            OH[2] = notechance(10, 50, 0.75)
            OH[3] = notechance(15, 80, 0.5)
            OH[4] = notechance(10, 50, 0.75)
            OH[5] = notechance(15, 80, 0.5)
            OH[6] = notechance(10, 50, 0.75)
            OH[7] = notechance(15, 80, 0.5)
            OH[8] = notechance(10, 50, 0.75)
            OH[9] = notechance(15, 80, 0.5)
            OH[10] = notechance(10, 50, 0.75)
            OH[11] = notechance(15, 80, 0.5)
            OH[12] = notechance(10, 50, 0.75)
            OH[13] = notechance(15, 80, 0.5)
            OH[14] = notechance(10, 50, 0.75)
            OH[15] = notechance(15, 80, 0.5)

        for x in range(0,16) :
            if OH[x] != [0,0] :
                CH[x] = [0,0]

        if countList(OH) > 0 :
            whileVar5 = 1
# ------------------------------------------------------------------------------

# guiclass.generateButton()

root = Tk()
root.title("Drum Pattern Generator")
app = GUI(root)
root.mainloop()
