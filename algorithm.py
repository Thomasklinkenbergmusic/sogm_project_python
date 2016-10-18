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
PERC1=[]
PERC2=[]
RIDE=[]

# Gives every pattern list 16 lists with [0, 0]
for I in range(0,16) :
    KICK.append([0,0])
    SNARE.append([0,0])
    CLAP.append([0,0])
    CH.append([0,0])
    OH.append([0,0])
    PERC1.append([0,0])
    PERC2.append([0,0])
    RIDE.append([0,0])

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


# Generate Snare
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

# ------------------------------------------------------------------------------

# Converts the 1 in pattern lists to midi notes
# (Kick = 60 (C3), Snare = 61 (C#3), etc...)
for x in range(0, 16) :
    if KICK[x][0] == 1 :
        KICK[x][0] = 60
    if SNARE[x][0] == 1 :
        SNARE[x][0] = 61
    if CLAP[x][0] == 1 :
        CLAP[x][0] = 62
    if CH[x][0] == 1 :
        CH[x][0] = 63
    if OH[x][0] == 1 :
        OH[x][0] = 64
    if PERC1[x][0] == 1 :
        PERC1[x][0] = 65
    if PERC2[x][0] == 1 :
        PERC2[x][0] = 66
    if RIDE[x][0] == 1 :
        RIDE[x][0] = 67

# print KICK
# print SNARE
# print CLAP
# print CH
# print OH
# print PERC1
# print PERC2
# print RIDE

# Comment this when you DON'T want midi to play
# ------------------------------------------------------------------------------
for x in range(0, 2) :
    for x in range(0, 16) :
        player.note_on(KICK[x][0], KICK[x][1])
        player.note_on(SNARE[x][0], SNARE[x][1])
        player.note_on(CLAP[x][0], CLAP[x][1])
        player.note_on(CH[x][0], CH[x][1])
        player.note_on(OH[x][0], OH[x][1])
        player.note_on(PERC1[x][0], PERC1[x][1])
        player.note_on(PERC2[x][0], PERC2[x][1])
        player.note_on(RIDE[x][0], RIDE[x][1])
        time.sleep(0.08)
        player.note_off(KICK[x][0], KICK[x][1])
        player.note_off(SNARE[x][0], SNARE[x][1])
        player.note_off(CLAP[x][0], CLAP[x][1])
        player.note_off(CH[x][0], CH[x][1])
        player.note_off(OH[x][0], OH[x][1])
        player.note_off(PERC1[x][0], PERC1[x][1])
        player.note_off(PERC2[x][0], PERC2[x][1])
        player.note_off(RIDE[x][0], RIDE[x][1])
        time.sleep(0.08)
# ------------------------------------------------------------------------------
