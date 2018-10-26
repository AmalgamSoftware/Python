import random
import math



def runTowerTest(modifier,height, breakSpot,marbles):
    TowerHeight = height
    if breakSpot == -1:
        breakSpot = random.randint(1,TowerHeight)
    if marbles == -1:
        marbles = 9999999

    found = False
    currentStart = 0
    currentEnd = TowerHeight
    count = 0
    breakSpotPrevFound = False
    breakSpotFound = False

    if breakSpot == 1 or breakSpot == 0:
        breakSpotPrevFound = True
    if breakSpot == TowerHeight:
        breakSpotFound = True
    while breakSpotFound == False or breakSpotPrevFound == False:
        if marbles > 1:
            chosenPoint = round(currentStart + (currentEnd - currentStart) * modifier)
            if chosenPoint >= breakSpot:  #At this case, I'd want to start 
                currentEnd = chosenPoint - 1
                marbles -= 1
                if chosenPoint == breakSpot:
                    breakSpotFound = True
            elif chosenPoint < breakSpot:  
                currentStart = chosenPoint + 1
                if chosenPoint == (breakSpot - 1):
                    breakSpotPrevFound = True
            count += 1
        elif marbles == 1:
            chosenPoint = currentStart
            if chosenPoint == breakSpot:
                breakSpotFound = True
            elif chosenPoint == (breakSpot - 1):
                breakSpotPrevFound = True
            currentStart += 1
            count += 1
    return count

def runTowerTestXMarbles(modifier,height, breakSpot):
    print("hey")

def FullDataXMarbles():
    marbles = int(input("Enter the number of marbles per test: "))
    
    towerHeight = int(input("Enter the tower height: "))

    increment = 0.033333


    print("\nShowing each of ",increment," through 1 modifiers for ",towerHeight," iterations through a tower of ",towerHeight," height...")
    print("------------------------------------------------------")
    #while loop through % choice modifiers.
    i = increment

    bestMod = 0
    bestModSteps = 9999999
    while i < 0.98:
        numberOfTests = 0
        totalSteps = 0
        #loop through towerHeight, with the breakpoint at each spot
        for j in range (towerHeight):
            totalSteps += runTowerTest(i,towerHeight,j,marbles)
            numberOfTests += 1
        avg=totalSteps/numberOfTests
        print("Modifier ", round(i,3),":\n                  Average step: ", avg)
        if avg < bestModSteps:
            bestMod = i
            bestModSteps = avg
        i += increment
    print("\n-----------------------------------------")
    print("\nThe best modifier was: ",round(bestMod,3))
    


def FullData():
    towerHeight = 10000

    increment = 0.033333


    print("\nShowing each of ",increment," through 1 modifiers for ",towerHeight," iterations through a tower of ",towerHeight," height...")
    print("------------------------------------------------------")
    #while loop through % choice modifiers.
    i = increment
    while i < 0.98:
        numberOfTests = 0
        totalSteps = 0
        #loop through towerHeight, with the breakpoint at each spot
        for j in range (towerHeight):
            totalSteps += runTowerTest(i,towerHeight,j,-1)
            numberOfTests += 1
        avg=totalSteps/numberOfTests
        print("Modifier ", round(i,3),":\n                  Average step: ", round(avg,4))
        i += increment

def RandomDistribution():

    inputHeight = int(input("Enter the max height of the tower: "))
    inputIter = int(input("Enter the number of iterations to test: "))

    thirdWins = 0
    halfWins = 0
    ties = 0
    for i in range (inputIter):
        loopHeight = random.randint(2,inputHeight)
        thirdCount = runTowerTest(0.33333,loopHeight,-1,-1)
        halfCount = runTowerTest(0.5,loopHeight,-1,-1)
        if thirdCount > halfCount:
            thirdWins += 1
        elif thirdCount < halfCount:
            halfWins += 1
        else:
            ties += 1
            
    print("The 0.333 modifier has won ", thirdWins," or ", thirdWins / inputIter * 100,"% of the time.")
    print("The 0.5 modifier has won ", halfWins, " or ", halfWins / inputIter * 100, "% of the time.")
    print(ties, " or ", round(ties / inputIter * 100,4), "% of the tests were ties.")

def DebugFunc():
    print("\nDebug Function enabled")
    dMod = float(input("Give mod: "))
    dHeight = int(input("Give height: "))
    dBreak = int(input("Give break: "))
    print(runTowerTest(dMod,dHeight,dBreak))
    
#MAIN LOOP
    

humanInput=""
while humanInput != "x":
    humanInput = input("\n(x) to exit, (r) for random distribution race,\n(f) for full data on infinite marbles\n(fn) for full data on specified marbles\n")
    if humanInput == "f":
        FullData()
    elif humanInput == "r":
        RandomDistribution()
    elif humanInput == "d":
        DebugFunc()
    elif humanInput == "fn":
        FullDataXMarbles()
        
        
