


#A lot of blank space so no one cheats

































































































































#No peeking Mr/Mrs






























































import random #To randomly choose a number
def getAmountToAdd(currentTotal):
    remainder = currentTotal % 7
    if remainder == 1:
        return random.randint(1,6) #generate integer between 1 and 6
    else:
        return (1-remainder) %7 #Decide the number to choose to win. Look below for explanation
    
'''
The strategy to win is to make the remainder of currentTotal divided by 7: 1 after your turn is complete.
Remainder    Amount to Add
0            1
1            0 (Not possible)
2            6
3            5
4            4
5            3
6            2

% always gives positive remainder. // is floor division(quotient)
if we divide -5 by 3. To make remainder positive, quotient will be -2 and remainder will be 1

'''


playerTurn = False
computerTurn = False
#User chooses who plays first. Him or AI
WhoGoesFirst = int(input("Do you want to do the turn first. If so press 1 and enter. Else press 0 and enter.\n")) 
if WhoGoesFirst == 1:
    playerTurn = True
else:
    computerTurn = True

total = 0 #Initialize total to 0
while total < 50: #Game is playing till the score is 50
    print("The total amount of money in the pot is currently %s" % total) #Displays the total
    if playerTurn == True: #If Player's turn
        wantToAdd = int(input("Enter any amount from 1-6 that you would like to add:")) #User enters how much he wants to add
        #Adding amount to total with checks
        if wantToAdd > 6:
            total += 6
        elif wantToAdd < 1:
            total += 1
        else:
            total += wantToAdd
        playerTurn = False #Since Player played his turn
        computerTurn = True #Now Computer's turn
    elif computerTurn == True: #If computer's turn
        wantToAdd = getAmountToAdd(total) #get amount to add
        print ("Computer added %s" % wantToAdd) #Tell user amount we will add
        total += wantToAdd #add the amount
        playerTurn = True #Next is Player's turn
        computerTurn = False #Since computer's turn happened
if total> 50: #if total is not equal to 50 
    print ("You failed to reach 50.")
elif total == 50: #if total is 50
    if playerTurn == False: #Meaning last turn was player and he won
        print ("You won.")
    else: #else computer won
        print ("Computer wins")
