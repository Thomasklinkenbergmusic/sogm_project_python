import random

"""WERKT!"""

AMOUNT = 80

def p(x) :
    result = 0.0004 * x
    return result
def R100() :
    x =  random.randint(1, 100)
    return x
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

print chance(AMOUNT, p(20))
print chance(AMOUNT, p(20))
print chance(AMOUNT, p(30))
print chance(AMOUNT, p(10))
