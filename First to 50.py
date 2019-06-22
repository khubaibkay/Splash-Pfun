




































































































































#No peeking Mr/Mrs






























































import random
def getAmountToAdd(currentTotal):
    if currentTotal%7==1:
        return random.randint(1,6)
    else:
        return (8-(currentTotal%7))%7
    









playerTurn=False
computerTurn=False
WhoGoesFirst=int(input("Do you want to do the turn first. If so press 1 and enter. Else press 0 and enter.\n"))
if WhoGoesFirst==1:
    playerTurn=True
else:
    computerTurn=True
total=0
while total <50:
    print("The total amount of money in the pot is currently %s" % total)
    if playerTurn==True:
        wantToAdd=int(input("Enter any amount from 1-6 that you would like to add:"))
        if wantToAdd>6:
            total+=6
        elif wantToAdd<1:
            total+=1
        else:
            total+=wantToAdd
        playerTurn=False
        computerTurn=True
    elif computerTurn==True:
        wantToAdd=getAmountToAdd(total)
        print("Computer added %s" % wantToAdd)
        total+=wantToAdd
        playerTurn=True
        computerTurn=False
if total>50:
    print("You failed to reach 50.")
elif total==50:
    if playerTurn==False:
        print("You won.")
    else:
        print("Computer wins")
