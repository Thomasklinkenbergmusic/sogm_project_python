import random

# Comment this when you DON'T want midi to play
# ------------------------------------------------------------------------------
import pygame
import time
import pygame.midi
pygame.midi.init()
player = pygame.midi.Output(1, 0)
player.set_instrument(0,1)
# ------------------------------------------------------------------------------

AMOUNT = 50

# Pattern lists
KICK=[]
SNARE=[]
CLAP=[]
CH=[]
OH=[]

# Midi notes
MIDIKICK = 60
MIDISNARE = 61
MIDICLAP = 62
MIDICH = 63
MIDIOH = 64

# Gives every pattern list 16 lists with [0, 0]
for I in range(0,16) :
    KICK.append([0,0])
    SNARE.append([0,0])
    CLAP.append([0,0])
    CH.append([0,0])
    OH.append([0,0])

# All Functions
# ------------------------------------------------------------------------------

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

# Converts the 1 in pattern lists to midi notes
for x in range(0, 16) :
    if KICK[x][0] == 1 :
        KICK[x][0] = MIDIKICK
    if SNARE[x][0] == 1 :
        SNARE[x][0] = MIDISNARE
    if CLAP[x][0] == 1 :
        CLAP[x][0] = MIDICLAP
    if CH[x][0] == 1 :
        CH[x][0] = MIDICH
    if OH[x][0] == 1 :
        OH[x][0] = MIDIOH


# Comment this when you DON'T want midi to play
# ------------------------------------------------------------------------------
for x in range(0, 2) :
    for x in range(0, 16) :
        player.note_on(KICK[x][0], KICK[x][1])
        player.note_on(SNARE[x][0], SNARE[x][1])
        player.note_on(CLAP[x][0], CLAP[x][1])
        player.note_on(CH[x][0], CH[x][1])
        player.note_on(OH[x][0], OH[x][1])
        time.sleep(0.08)
        player.note_off(KICK[x][0], KICK[x][1])
        player.note_off(SNARE[x][0], SNARE[x][1])
        player.note_off(CLAP[x][0], CLAP[x][1])
        player.note_off(CH[x][0], CH[x][1])
        player.note_off(OH[x][0], OH[x][1])
        time.sleep(0.08)
# ------------------------------------------------------------------------------
