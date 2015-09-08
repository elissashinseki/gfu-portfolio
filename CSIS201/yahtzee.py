import random

#*******************************************************************************
# MODULE : displayScoreboard
# INPUTS : menuList
# OUTPUTS : badList
# DEF : Displays the menu to the user, returns the list of categories
#       that can no longer be played
#********************************************************************************

def displayScoreboard(menuList):
    print()
    
    badList = []
    
    for i in range(len(menuList)):
        if menuList[i][2] == -1:
            print(menuList[i][0], '\t', menuList[i][1])
        else:
            if menuList[i][2] == 1:
                print(menuList[i][0], '\t', menuList[i][1], \
                      format(menuList[i][2], '2.0f'), "point")
            else:
                print(menuList[i][0], '\t', menuList[i][1], \
                      format(menuList[i][2], '2.0f'), "points")
            badList.append(menuList[i][0])

    return badList

#********************************************************************************
# MODULE : rollDice
# INPUTS : none
# OUTPUTS : roll
# DEF : Executes the dice rolling aspect of the game. Allows the user to
#       roll any combination of five dice up to three times to collect five
#       values in a list to be sent into a scoring module.
#********************************************************************************

def rollDice():
    # FIRST ROLL
    roll = []

    for i in range(5):
        roll.append(random.randint(1, 6))
        
    roll.sort()

    print()
    print("First roll: ", roll)

    rollAgain = input("Roll again? (Y/N): ")

    while rollAgain not in "YyNn":
        print("ERROR: Must enter Y or N")
        rollAgain = input("Roll again? (Y/N): ")

    # SECOND ROLL
    if rollAgain in "Yy":
        removeDice(roll)
        
        # Roll again
        roll2 = []
        for i in range(5 - len(roll)):
            roll2.append(random.randint(1, 6))

        roll = roll + roll2
        roll.sort()

        print()
        print("Second roll: ", roll)

        rollAgain = input("Roll again? (Y/N): ")

        while rollAgain not in "YyNn":
            print("ERROR: Must enter Y or N")
            rollAgain = input("Roll again? (Y/N): ")
            
        # THIRD ROLL
        if rollAgain in "Yy":
            removeDice(roll)
                
            # Roll again
            roll3 = []
            for i in range(5 - len(roll)):
                roll3.append(random.randint(1, 6))

            roll = roll + roll3
            roll.sort()
            
            print()          
            print("Third roll: ", roll)

    return roll

#********************************************************************************
# MODULE : removeDice
# INPUTS : roll
# OUTPUTS : none
# DEF : Asks user for which dice to reroll, checks to see if dice are present,
#       removes dice to reroll from "roll"
#********************************************************************************

def removeDice(roll):
    clear = False
    while clear == False:
        rollCopy = roll[:]

        # Ask user which numbers to reroll, error trapping for input
        # that is not separated by spaces.

        allNum = False
        while allNum == False:
            
            hold = input("What numbers will you reroll? ")
            hold = hold.split()
            
            notNum = 0
            for i in hold:
                if not i.isdigit():
                    notNum += 1

            if notNum == 0:
                allNum = True
            else:
                print("ERROR: Numbers must be separated by spaces")

        intHold = []
        for i in hold:
            num = int(i)
            intHold.append(num)
        
        # Check to see if potential rerolls are in the roll
        notThere = 0
        for i in intHold:
            if i in rollCopy:
                rollCopy.remove(i)
            else:
                notThere += 1

        if notThere == 0:
            clear = True
        else:
            print("ERROR: Value(s) not in roll!")
            
    for i in intHold:
        roll.remove(i)


#********************************************************************************
# MODULE : makeChoice
# INPUTS : badList
# OUTPUTS : choice
# DEF : Asks user to pick a scoring category that has not already been chosen
#       to send the values of dice to be scored
#********************************************************************************

def makeChoice(badList):
    choice = int(input("Select scoring category -> "))

    while(choice < 1) or (choice > 13) or (choice in badList):
        print("This category has already been scored or is nonexistent!" + \
              " Try again.")
        choice = int(input("Select dice scoring category -> "))
    
    return choice

#********************************************************************************
# MODULE : calcSum
# INPUTS : roll
# OUTPUTS : sum
# DEF : Calculates and returns the sum of values in a list.
#********************************************************************************

def calcSum(roll):
    sum = 0

    for i in roll:
        sum += i

    return sum

#********************************************************************************
# MODULE : upperSection
# INPUTS : roll, num
# OUTPUTS : points
# DEF : Iterates through the roll to determine the number of times a number
#       "num" appears in the array. Returns the product of the count and the
#        numeric value of "num" as points.
#********************************************************************************

def upperSection(roll, num):
    count = 0
    
    for i in roll:
        if i == num:
            count += 1

    points = count * num

    return points


#********************************************************************************
# MODULE : threeOfKind
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks to see if conditions for 3 of a kind are met.
#       Returns sum of dice if met, 0 points if not met.
#*********************************************************************************

def threeOfKind(roll):
    points = 0
    
    if roll[0] == roll[1] == roll[2] or roll[1] == roll[2] == roll[3] or\
       roll[2] == roll[3] == roll[4]:
        points = calcSum(roll)

    return points

#********************************************************************************
# MODULE : fourOfKind
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks to see if conditions for 4 of a kind are met.
#       Returns sum of dice if met, 0 points if not met.
#********************************************************************************

def fourOfKind(roll):
    points = 0
    
    if roll[0] == roll[1] == roll[2] == roll[3] or roll[1] == roll[2] == \
       roll[3] == roll[4]:
        points = calcSum(roll)

    return points

#********************************************************************************
# MODULE : fullHouse
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks whether conditions for a full house are met.
#       Returns 25 points if met, 0 points if not met.
#********************************************************************************

def fullHouse(roll):
    points = 0
    
    if (roll[0] == roll[1] == roll[2] and roll[3] == roll[4])\
       or (roll[0] == roll[1] and roll[2] == roll[3] == roll[4]):
        points = 25
    
    return points

#********************************************************************************
# MODULE : smStraight
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks whether conditions for a small straight are met.
#       Returns 30 points if met, 0 points if not met.
#********************************************************************************

def smStraight(roll):
    
    # Removes all duplicate numbers from the roll, saves rest in "search"
    search = [roll[0]]
    
    for i in range(1, len(roll)):
        if roll[i] != roll[i - 1]:
            search.append(roll[i])

    # Adds zeros to the list to keep it 5 values long
    if len(search) < 5:
        for i in range(5-len(search)):
            search.append(0)
        
    # Assigns 30 points if a straight is found in "search"
    points = 0

    if (search[0] + 1 == search[1] and search[1] + 1 == search[2] \
        and search[2] + 1 == search[3]):
        points = 30
        
    elif(search[1] + 1 == search[2] and search[2] + 1 == search[3] \
         and search[3] + 1 == search[4]):
        points = 30
    
    return points

#********************************************************************************
# MODULE : lgStraight
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks whether conditions for a large straight are met.
#       Returns 40 points if met, 0 points if not met.
#********************************************************************************

def lgStraight(roll):
    points = 0
    
    if roll[0] + 1 == roll[1] and roll[1] + 1 == roll[2] and \
       roll[2] + 1 == roll[3] and roll[3] + 1 == roll[4]:
        points = 40
    
    return points

#********************************************************************************
# MODULE : yahtzee
# INPUTS : roll
# OUTPUTS : points
# DEF : Checks whether conditions for Yahtzee are met.
#       Returns 50 points if met, 0 points if not met.
#********************************************************************************

def yahtzee(roll):
    points = 0
    
    if roll[0] == roll[1] == roll[2] == roll[3] == roll[4]:
        points = 50

    return points

#********************************************************************************
# MODULE : chance
# INPUTS : roll
# OUTPUTS : points
# DEF : Calculates the sum of all dice and is returned as "points".
#********************************************************************************

def chance(roll):
    points = calcSum(roll)

    return points

#********************************************************************************
# MODULE : finalScores
# INPUTS : menuList
# OUTPUTS : finalScore
# DEF : Prints final scoreboard; calculates, prints, and returns final score.
#********************************************************************************

def finalScores(menuList):
    # Display ending scoreboard
    for i in range(len(menuList)):
        if menuList[i][2] == -1:
            print(menuList[i][0], '\t', menuList[i][1])
        else:
            print(menuList[i][0], '\t', menuList[i][1], \
                  format(menuList[i][2], '2.0f'), "points")
            
    print("-------------------------------------------")

    # Calculate score for upper section
    upperScore = 0
    for i in range(0, 6):
        upperScore += menuList[i][2]
    if upperScore >= 63:
        upperScore += 35
    print("UPPER SECTION: ", format(upperScore, '3'))

    # Calculate score for lower section
    lowerScore = 0
    for i in range(6, 13):
        lowerScore += menuList[i][2]
    print("LOWER SECTION: ", format(lowerScore, '3'))

    # Calculate final socre
    finalScore = upperScore + lowerScore
    print("GRAND TOTAL:   ", format(finalScore, '3'))

    return finalScore

#********************************************************************************
# MODULE : highScores
# INPUTS : finalScore
# OUTPUTS : none
# DEF : Updates high scores in the text file if new score is high enough.
#********************************************************************************

def highScores(finalScore):
    inFile = open("highscores.txt", 'r')
    highScores = inFile.read()
    inFile.close
    
    score = highScores.split()
    
    if finalScore >= int(score[0]):
        score = str(finalScore) + ' ' + score[0] + ' ' + score[1]
        print("NEW HIGH SCORE!\n")
    elif finalScore >= int(score[1]):
        score = score[0] + ' ' +  str(finalScore) + ' ' + score[1]
    elif finalScore >= int(score[2]):
        score = score[0] + ' ' + score[1] + ' ' + str(finalScore)
    else:
        score = score[0] + ' ' + score[1] + ' ' + score[2]
    
    outFile = open("highscores.txt", 'w')
    outFile.write(score)
    outFile.close

#********************************************************************************
# MODULE : playGame
# INPUTS: none
# OUTPUTS: none
# DEF : Menu option number 1 - Runs the Yahtzee game
#********************************************************************************

def playGame():
    menuList = [[1, 'Ones            ', -1],
                [2, 'Twos            ', -1],
                [3, 'Threes          ', -1],
                [4, 'Fours           ', -1],
                [5, 'Five            ', -1],
                [6, 'Sixes           ', -1],
                [7, '3 of a Kind     ', -1],
                [8, '4 of a Kind     ', -1],
                [9, 'Full House      ', -1],
                [10, 'Small Straight  ', -1],
                [11, 'Large Straight  ', -1],
                [12, 'YAHTZEE         ', -1],
                [13, 'Chance          ', -1]]

    gameOver = False 
    while gameOver == False:
        badList = displayScoreboard(menuList)
        roll = rollDice()
        
        print()
        
        choice = makeChoice(badList)

        if choice in [1,2,3,4,5,6]:
            points = upperSection(roll, choice)
        elif choice == 7:
            points = threeOfKind(roll)
        elif choice == 8:
            points = fourOfKind(roll)
        elif choice == 9:
            points = fullHouse(roll)
        elif choice == 10:
            points = smStraight(roll)
        elif choice == 11:
            points = lgStraight(roll)
        elif choice == 12:
            points = yahtzee(roll)
        elif choice == 13:
            points = chance(roll)

        menuList[choice - 1][2] = points

        validity = []
        for i in range(len(menuList)):
            validity.append(menuList[i][2])
        if -1 in validity:
            gameOver = False
        else:
            gameOver = True

    finalScore = finalScores(menuList)

    highScores(finalScore)

    print()

#********************************************************************************
# MODULE : showHighScores()
# INPUTS : none
# OUTPUTS : none
# DEF : Menu option number 2 - Displays high scores to the user
#********************************************************************************

def showHighScores():
    inFile = open("highscores.txt", 'r')
    highScores = inFile.read()
    inFile.close

    scores = highScores.split()

    print("\nHIGH SCORES: ")
    
    for i in range(1, len(scores) + 1):
        print(i, ":", scores[i-1])

    print()

#********************************************************************************
# MODULE : topMenu
# INPUT: none
# OUTPUT: selection
# DEF : Displays the top menu to the user and returns selection
#********************************************************************************

def topMenu():
    print("1 - PLAY YAHTZEE")
    print("2 - SHOW HIGH SCORES")
    print("3 - QUIT")
    selection = input("Selection: ")

    # Error trap
    while selection not in "123":
        print("ERROR: Must choose 1, 2, or 3!")
        selection = input("Selection: ")

    selection = int(selection)
    
    return selection

#********************************************************************************
# MODULE : main
# DEF : Executes the Yahtzee program.
#********************************************************************************

def main():
    # variable declaration
    
    # main algorithm
    print("Welcome to Yahtzee!")

    selection = topMenu()
    
    while selection != 3:

        if selection == 1:
            playGame()
        if selection == 2:
            showHighScores()

        selection = topMenu()
    
main()
