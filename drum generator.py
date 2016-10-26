from Tkinter import *
import random
import time
import pygame.midi

class DrumGenerator(Frame) :

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

    # Gives every pattern list 16 lists with [0, 0]
    for I in range(0,16) :
        KICK.append([0,0])
        SNARE.append([0,0])
        CLAP.append([0,0])
        CH.append([0,0])
        OH.append([0,0])

    # Initial for pygame.midi
    pygame.midi.init()
    player = pygame.midi.Output(1, 0)
    player.set_instrument(0,1)

    # Parameter for intensity of notes (class variable)
    INTENSITY = 50

    # Initializing GUI
    def __init__(self):
        self.master = Tk()
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title("Drum Generator")
        self.master.resizable(0,0)
        self.create_widgets()

    def create_widgets(self) :
        # Empty spaces for grid - Not the best way but it works!
        self.empty_0 = Label(self.frame, text="    ")
        self.empty_1 = Label(self.frame, text="    ")
        self.empty_2 = Label(self.frame, text="    ")
        self.empty_3 = Label(self.frame, text="    ")
        self.empty_4 = Label(self.frame, text="    ")
        self.empty_5 = Label(self.frame, text="    ")
        self.empty_6 = Label(self.frame, text="    ")
        self.empty_7 = Label(self.frame, text="    ")
        self.empty_8 = Label(self.frame, text="    ")

        # All the buttons, sliders and entry's
        self.button_0 = Button(self.frame, command=self.playButton, text="Play")
        self.button_2 = Button(self.frame, command=self.generateButton, text="Generate")
        self.amountLabel = Label(self.frame, text="Intensity")
        self.slider = Scale(self.frame)
        self.slider.config(orient=HORIZONTAL)
        self.slider.config(length=200, width=20, sliderlength=10)
        self.slider.config(from_=0, to_=100, tickinterval=50)
        self.slider.set(50)
        self.bpmLabel = Label(self.frame, text="bpm:")
        self.bpmEntry = Entry(self.frame)
        self.bpmEntry.config(width=3)
        self.bpmEntry.insert(0, 120)

        # All the widgets placed in the grid
        self.empty_0.grid(row=0, column=0)
        self.empty_1.grid(row=1, column=0)
        self.button_0.grid(row=1, column=1)
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

# Algorithm Functions
# ------------------------------------------------------------------------------
    # Gives random int between 0 - 100
    def R100(self) :
        x =  random.randint(1, 100)
        return x

    # Gives random velocity. First argument is the initial velocity, second is
    # the devider for the minimum and maximum for random. Example:
    # Rvel(100, 0.2) gives a random int between 80 and 120.
    def Rvel(self, x, y) :
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
    def scale(self, x, oMin, oMax, nMin, nMax):
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

    # Scales a int with the "INTENSITY" input for function notechance()
    def chance(self, x, y) :
        if x <= 50 :
            resultx = self.scale(x, 0, 100, 100, 0)
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
    def notechance(self, x, y, z) :
        list = [0, 0]
        if self.R100() < self.chance(self.INTENSITY, (0.0004 * x)) :
            list = [1, self.Rvel(y, z)]
        return list

    # Can give amount of hits in a pattern. First argument is the list. This func-
    # tion only works BEFORE the convertion to midi notes.
    def countList(self, x) :
        y = 0
        for i in range(0, len(x)) :
            if x[i][0] == 1 :
                y = y + 1
        return y

# GUI functions
# ------------------------------------------------------------------------------
    # Plays midi with the given BPM
    def playButton(self) :
        print "Playing..."
        sleeptime = float((60000. / int(self.bpmEntry.get())) / 8.) # Dertermines BPM
        for i in range(0, 2) :
            for x in range(0, 16) :
                self.player.note_on(self.KICK[x][0], self.KICK[x][1])
                self.player.note_on(self.SNARE[x][0], self.SNARE[x][1])
                self.player.note_on(self.CLAP[x][0], self.CLAP[x][1])
                self.player.note_on(self.CH[x][0], self.CH[x][1])
                self.player.note_on(self.OH[x][0], self.OH[x][1])
                time.sleep(sleeptime / 1000.)
                self.player.note_off(self.KICK[x][0], self.KICK[x][1])
                self.player.note_off(self.SNARE[x][0], self.SNARE[x][1])
                self.player.note_off(self.CLAP[x][0], self.CLAP[x][1])
                self.player.note_off(self.CH[x][0], self.CH[x][1])
                self.player.note_off(self.OH[x][0], self.OH[x][1])
                time.sleep(sleeptime / 1000.)
        print "Done playing!"

    # Triggers the algorithm that fills the instrument lists with the given intensity
    def generateButton(self) :
        print "Generated new drum pattern"
        self.INTENSITY = self.slider.get()
        # Generate Kick
        whileVar1 = 0
        while whileVar1 == 0 :
            self.KICK[0] = self.notechance(100, 100, 0.1)
            self.KICK[4] = self.notechance(80, 90, 0.12)
            self.KICK[8] = self.notechance(90, 100, 0.1)
            self.KICK[12] = self.notechance(80, 100, 0.13)

            if self.KICK[4] == [0,0] :
                self.KICK[1] = self.notechance(20, 25, 0.8)
                self.KICK[2] = self.notechance(10, 50, 0.3)
                self.KICK[3] = self.notechance(60, 75, 0.5)
                self.KICK[5] = self.notechance(60, 75, 0.5)
            else :
                self.KICK[1] = self.notechance(20, 25, 0.8)
                self.KICK[2] = self.notechance(60, 50, 0.4)
                self.KICK[3] = self.notechance(30, 50, 0.2)
                self.KICK[5] = self.notechance(10, 20, 0.75)

            if self.KICK[8] == [0,0] :
                if self.KICK[5] == [0,0] :
                    self.KICK[5] = self.notechance(35, 25, 0.8)
                self.KICK[6] = self.notechance(10, 50, 0.3)
                self.KICK[7] = self.notechance(60, 75, 0.5)
                self.KICK[9] = self.notechance(60, 75, 0.5)
            else :
                if self.KICK[5] == [0,0] :
                    self.KICK[5] = self.notechance(20, 25, 0.8)
                self.KICK[6] = self.notechance(50, 50, 0.4)
                self.KICK[7] = self.notechance(30, 50, 0.2)
                self.KICK[9] = self.notechance(10, 50, 0.75)

            if self.KICK[12] == [0,0] :
                if self.KICK[9] == [0,0] :
                    self.KICK[9] = self.notechance(35, 25, 0.8)
                self.KICK[10] = self.notechance(10, 50, 0.3)
                self.KICK[11] = self.notechance(60, 75, 0.5)
                self.KICK[13] = self.notechance(60, 75, 0.5)
            else :
                if self.KICK[9] == [0,0] :
                    self.KICK[9] = self.notechance(20, 25, 0.8)
                self.KICK[10] = self.notechance(50, 50, 0.4)
                self.KICK[11] = self.notechance(30, 50, 0.2)
                self.KICK[13] = self.notechance(10, 50, 0.75)

            if self.KICK[13] == [0,0] :
                self.KICK[14] = self.notechance(60, 50, 0.5)
                if self.KICK[1] == [0,0] :
                    self.KICK[15] = self.notechance(20, 50, 0.2)
                else :
                    self.KICK[15] = self.notechance(10, 50, 0.2)
            else :
                self.KICK[14] = self.notechance(60, 50, 0.5)
                if self.KICK[1] == [0,0] :
                    self.KICK[15] = self.notechance(50, 50, 0.2)
                else :
                    self.KICK[15] = self.notechance(30, 50, 0.2)

            if self.countList(self.KICK) > 0 :
                whileVar1 = 1

        # Generate snare
        whileVar2 = 0
        while whileVar2 == 0 :
            if self.R100() < 50 :
                self.SNARE[4] = self.notechance(90, 100, 0.1)
                self.SNARE[12] = self.notechance(90, 100, 0.1)
            else :
                self.SNARE[8] = self.notechance(95, 100, 0.1)

            if self.SNARE[4] != [0,0] :
                self.KICK[4] = [0,0]
            if self.SNARE[8] != [0,0] :
                self.KICK[8] = [0,0]
            if self.SNARE[12] != [0,0] :
                self.KICK[12] = [0,0]

            if self.countList(self.KICK) >= 8 :
                self.SNARE[1] = self.notechance(20, 50, 0.2)

                if self.SNARE[1] == [0,0] :
                    self.SNARE[2] = self.notechance(25, 50, 0.1)
                else :
                    self.SNARE[2] = self.notechance(10, 20, 0.2)

                if self.SNARE[4] == [0,0] :
                    self.SNARE[4] = self.notechance(10, 70, 0.5)

                if self.SNARE[4] == [0,0] :
                    self.SNARE[3] = self.notechance(25, 60, 0.2)
                    self.SNARE[5] = self.notechance(20, 40, 0.5)
                else :
                    self.SNARE[3] = self.notechance(5, 20, 0.5)
                    self.SNARE[5] = self.notechance(5, 20, 0.5)

                if self.SNARE[5] == [0,0] :
                    self.SNARE[5] = self.notechance(10, 50, 0.2)

                if self.SNARE[5] == [0,0] :
                    self.SNARE[6] = self.notechance(25, 50, 0.1)
                else :
                    self.SNARE[6] = self.notechance(10, 20, 0.2)

                if self.SNARE[8] == [0,0] :
                    self.SNARE[8] = self.notechance(10, 70, 0.5)

                if self.SNARE[8] == [0,0] :
                    self.SNARE[7] = self.notechance(25, 60, 0.2)
                    self.SNARE[9] = self.notechance(20, 40, 0.5)
                else :
                    self.SNARE[7] = self.notechance(5, 20, 0.5)
                    self.SNARE[9] = self.notechance(5, 20, 0.5)

                if self.SNARE[9] == [0,0] :
                    self.SNARE[9] = self.notechance(10, 50, 0.2)

                if self.SNARE[9] == [0,0] :
                    self.SNARE[10] = self.notechance(25, 50, 0.1)
                else :
                    self.SNARE[10] = self.notechance(10, 20, 0.2)

                if self.SNARE[12] == [0,0] :
                    self.SNARE[12] = self.notechance(10, 70, 0.5)

                if self.SNARE[12] == [0,0] :
                    self.SNARE[11] = self.notechance(25, 60, 0.2)
                    self.SNARE[13] = self.notechance(20, 40, 0.5)
                else :
                    self.SNARE[11] = self.notechance(5, 20, 0.5)
                    self.SNARE[13] = self.notechance(5, 20, 0.5)

                if self.SNARE[13] == [0,0] :
                    self.SNARE[14] = self.notechance(20, 30, 0.5)
                else :
                    self.SNARE[14] = self.notechance(5, 30, 0.5)

                if self.SNARE[1] == [0,0] :
                    self.SNARE[15] = self.notechance(20, 30, 0.5)
                else :
                    self.SNARE[15] = self.notechance(5, 30, 0.5)

            else :
                self.SNARE[1] = self.notechance(40, 50, 0.2)

                if self.SNARE[1] == [0,0] :
                    self.SNARE[2] = self.notechance(50, 50, 0.1)
                else :
                    self.SNARE[2] = self.notechance(20, 20, 0.2)

                if self.SNARE[4] == [0,0] :
                    self.SNARE[4] = self.notechance(20, 70, 0.5)

                if self.SNARE[4] == [0,0] :
                    self.SNARE[3] = self.notechance(50, 60, 0.2)
                    self.SNARE[5] = self.notechance(40, 40, 0.5)
                else :
                    self.SNARE[3] = self.notechance(10, 20, 0.5)
                    self.SNARE[5] = self.notechance(10, 20, 0.5)

                if self.SNARE[5] == [0,0] :
                    self.SNARE[5] = self.notechance(20, 50, 0.2)

                if self.SNARE[5] == [0,0] :
                    self.SNARE[6] = self.notechance(50, 50, 0.1)
                else :
                    self.SNARE[6] = self.notechance(20, 20, 0.2)

                if self.SNARE[8] == [0,0] :
                    self.SNARE[8] = self.notechance(20, 70, 0.5)

                if self.SNARE[8] == [0,0] :
                    self.SNARE[7] = self.notechance(50, 60, 0.2)
                    self.SNARE[9] = self.notechance(40, 40, 0.5)
                else :
                    self.SNARE[7] = self.notechance(10, 20, 0.5)
                    self.SNARE[9] = self.notechance(10, 20, 0.5)

                if self.SNARE[9] == [0,0] :
                    self.SNARE[9] = self.notechance(20, 50, 0.2)

                if self.SNARE[9] == [0,0] :
                    self.SNARE[10] = self.notechance(50, 50, 0.1)
                else :
                    self.SNARE[10] = self.notechance(20, 20, 0.2)

                if self.SNARE[12] == [0,0] :
                    self.SNARE[12] = self.notechance(20, 70, 0.5)

                if self.SNARE[12] == [0,0] :
                    self.SNARE[11] = self.notechance(50, 60, 0.2)
                    self.SNARE[13] = self.notechance(40, 40, 0.5)
                else :
                    self.SNARE[11] = self.notechance(10, 20, 0.5)
                    self.SNARE[13] = self.notechance(10, 20, 0.5)

                if self.SNARE[13] == [0,0] :
                    self.SNARE[14] = self.notechance(40, 30, 0.5)
                else :
                    self.SNARE[14] = self.notechance(10, 30, 0.5)

                if self.SNARE[1] == [0,0] :
                    self.SNARE[15] = self.notechance(40, 30, 0.5)
                else :
                    self.SNARE[15] = self.notechance(10, 30, 0.5)

            if self.countList(self.SNARE) > 0 :
                    whileVar2 = 1

        # Generate clap
        whileVar3 = 0
        while whileVar3 == 0 :
            if self.countList(self.SNARE) >= 5 :
                self.CLAP[0] = self.notechance(5, 60, 0.99)
                self.CLAP[1] = self.notechance(5, 60, 0.99)
                self.CLAP[2] = self.notechance(5, 60, 0.99)
                self.CLAP[3] = self.notechance(5, 60, 0.99)

                if self.SNARE[4] == [0,0] :
                    self.CLAP[4] = self.notechance(50, 60, 0.99)
                else :
                    self.CLAP[4] = self.notechance(5, 60, 0.99)

                self.CLAP[5] = self.notechance(5, 60, 0.99)
                self.CLAP[6] = self.notechance(5, 60, 0.99)
                self.CLAP[7] = self.notechance(5, 60, 0.99)

                if self.SNARE[8] == [0,0] :
                    self.CLAP[8] = self.notechance(50, 60, 0.99)
                else :
                    self.CLAP[8] = self.notechance(5, 60, 0.99)

                self.CLAP[9] = self.notechance(5, 60, 0.99)
                self.CLAP[10] = self.notechance(5, 60, 0.99)
                self.CLAP[11] = self.notechance(5, 60, 0.99)

                if self.SNARE[12] == [0,0] :
                    self.CLAP[12] = self.notechance(50, 60, 0.99)
                else :
                    self.CLAP[12] = self.notechance(5, 60, 0.99)

                self.CLAP[13] = self.notechance(5, 60, 0.99)
                self.CLAP[14] = self.notechance(5, 60, 0.99)
                self.CLAP[15] = self.notechance(5, 60, 0.99)

            else :
                self.CLAP[0] = self.notechance(10, 60, 0.99)
                self.CLAP[1] = self.notechance(10, 60, 0.99)
                self.CLAP[2] = self.notechance(10, 60, 0.99)
                self.CLAP[3] = self.notechance(10, 60, 0.99)

                if self.SNARE[4] == [0,0] :
                    self.CLAP[4] = self.notechance(70, 60, 0.99)
                else :
                    self.CLAP[4] = self.notechance(10, 60, 0.99)

                self.CLAP[5] = self.notechance(10, 60, 0.99)
                self.CLAP[6] = self.notechance(10, 60, 0.99)
                self.CLAP[7] = self.notechance(10, 60, 0.99)

                if self.SNARE[8] == [0,0] :
                    self.CLAP[8] = self.notechance(70, 60, 0.99)
                else :
                    self.CLAP[8] = self.notechance(10, 60, 0.99)

                self.CLAP[9] = self.notechance(10, 60, 0.99)
                self.CLAP[10] = self.notechance(10, 60, 0.99)
                self.CLAP[11] = self.notechance(10, 60, 0.99)

                if self.SNARE[12] == [0,0] :
                    self.CLAP[12] = self.notechance(70, 60, 0.99)
                else :
                    self.CLAP[12] = self.notechance(10, 60, 0.99)

                self.CLAP[13] = self.notechance(10, 60, 0.99)
                self.CLAP[14] = self.notechance(10, 60, 0.99)
                self.CLAP[15] = self.notechance(10, 60, 0.99)

            if self.countList(self.CLAP) > 0 :
                whileVar3 = 1

        # Generate closed hi-hat
        whileVar4 = 0
        while whileVar4 == 0 :
            self.CH[0] = self.notechance(50, 100, 0.2)
            self.CH[2] = self.notechance(50, 50, 0.99)
            self.CH[4] = self.notechance(50, 80, 0.2)
            self.CH[6] = self.notechance(50, 50, 0.99)
            self.CH[8] = self.notechance(50, 100, 0.2)
            self.CH[10] = self.notechance(50, 50, 0.99)
            self.CH[12] = self.notechance(50, 80, 0.2)
            self.CH[14] = self.notechance(50, 50, 0.99)

            if self.countList(self.CH) <= 5 :
                self.CH[1] = self.notechance(30, 50, 0.2)
                self.CH[3] = self.notechance(30, 50, 0.2)
                self.CH[5] = self.notechance(30, 50, 0.2)
                self.CH[7] = self.notechance(30, 50, 0.2)
                self.CH[9] = self.notechance(30, 50, 0.2)
                self.CH[11] = self.notechance(30, 50, 0.2)
                self.CH[13] = self.notechance(30, 50, 0.2)
                self.CH[15] = self.notechance(30, 50, 0.2)
            else :
                self.CH[1] = self.notechance(10, 50, 0.2)
                self.CH[3] = self.notechance(10, 50, 0.2)
                self.CH[5] = self.notechance(10, 50, 0.2)
                self.CH[7] = self.notechance(10, 50, 0.2)
                self.CH[9] = self.notechance(10, 50, 0.2)
                self.CH[11] = self.notechance(10, 50, 0.2)
                self.CH[13] = self.notechance(10, 50, 0.2)
                self.CH[15] = self.notechance(10, 50, 0.2)

            if self.countList(self.CH) > 0 :
                whileVar4 = 1

        # Generate open hi-hat
        whileVar5 = 0
        while whileVar5 == 0 :
            if self.countList(self.CH) <= 5 :
                self.OH[0] = self.notechance(20, 50, 0.75)
                self.OH[1] = self.notechance(30, 80, 0.5)
                self.OH[2] = self.notechance(20, 50, 0.75)
                self.OH[3] = self.notechance(30, 80, 0.5)
                self.OH[4] = self.notechance(20, 50, 0.75)
                self.OH[5] = self.notechance(30, 80, 0.5)
                self.OH[6] = self.notechance(20, 50, 0.75)
                self.OH[7] = self.notechance(30, 80, 0.5)
                self.OH[8] = self.notechance(20, 50, 0.75)
                self.OH[9] = self.notechance(30, 80, 0.5)
                self.OH[10] = self.notechance(20, 50, 0.75)
                self.OH[11] = self.notechance(30, 80, 0.5)
                self.OH[12] = self.notechance(20, 50, 0.75)
                self.OH[13] = self.notechance(30, 80, 0.5)
                self.OH[14] = self.notechance(20, 50, 0.75)
                self.OH[15] = self.notechance(30, 80, 0.5)
            else :
                self.OH[0] = self.notechance(10, 50, 0.75)
                self.OH[1] = self.notechance(15, 80, 0.5)
                self.OH[2] = self.notechance(10, 50, 0.75)
                self.OH[3] = self.notechance(15, 80, 0.5)
                self.OH[4] = self.notechance(10, 50, 0.75)
                self.OH[5] = self.notechance(15, 80, 0.5)
                self.OH[6] = self.notechance(10, 50, 0.75)
                self.OH[7] = self.notechance(15, 80, 0.5)
                self.OH[8] = self.notechance(10, 50, 0.75)
                self.OH[9] = self.notechance(15, 80, 0.5)
                self.OH[10] = self.notechance(10, 50, 0.75)
                self.OH[11] = self.notechance(15, 80, 0.5)
                self.OH[12] = self.notechance(10, 50, 0.75)
                self.OH[13] = self.notechance(15, 80, 0.5)
                self.OH[14] = self.notechance(10, 50, 0.75)
                self.OH[15] = self.notechance(15, 80, 0.5)

            for x in range(0,16) :
                if self.OH[x] != [0,0] :
                    self.CH[x] = [0,0]

            if self.countList(self.OH) > 0 :
                whileVar5 = 1

            # Converts the 1 in pattern lists to midi notes
            for x in range(0, 16) :
                if self.KICK[x][0] == 1 :
                    self.KICK[x][0] = self.MIDIKICK
                if self.SNARE[x][0] == 1 :
                    self.SNARE[x][0] = self.MIDISNARE
                if self.CLAP[x][0] == 1 :
                    self.CLAP[x][0] = self.MIDICLAP
                if self.CH[x][0] == 1 :
                    self.CH[x][0] = self.MIDICH
                if self.OH[x][0] == 1 :
                    self.OH[x][0] = self.MIDIOH

# Runs program
app = DrumGenerator()
app.master.mainloop()
