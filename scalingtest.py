import random

"""WERKT!"""

AMOUNT = 50

kick=[]
for I in range(0,8) :
    kick.append([0,0])

def percentage(x) :
    result = 0.0004 * x
    return result

def R100() :
    x =  random.randint(1, 100)
    return x

def Rvel(x, y) :
    if y < 0 :
        Y = 0
    if y > 1:
        Y = 1
    min = int(x * (1 - y))
    max = int(x * (1 + y))
    if min < 1 :
        min = 1
    if max > 127 :
        max = 127
    result = random.randint(min, max)
    return result

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

def notechance(x, p1, y, p2) :
    list = [0, 0]
    if R100() < chance(x, p1) :
        list = [1, Rvel(y, p2)]
    return list

kick[0]=notechance(AMOUNT, percentage(100), 100, 0.1)
kick[1]=notechance(AMOUNT, percentage(20), 30, 0.5)
kick[2]=notechance(AMOUNT, percentage(40), 50, 0.1)
kick[3]=notechance(AMOUNT, percentage(60), 80, 0.25)
kick[4]=notechance(AMOUNT, percentage(70), 100, 0.1)
kick[5]=notechance(AMOUNT, percentage(10), 30, 0.2)
kick[6]=notechance(AMOUNT, percentage(50), 20, 0.5)
kick[7]=notechance(AMOUNT, percentage(40), 60, 0.2)

print kick
