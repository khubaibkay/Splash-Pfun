
player1Turn=True
total=0
while total <50:
    if player1Turn==True:
        print("Player 1's turn")
    else:
        print ("Player 2's turn")
    print("The total amount of money in the pot is currently %s" % total)
    wantToAdd=int(input("Enter any amount from 1-6 that you would like to add:"))
    if wantToAdd>6:
        total+=6
    elif wantToAdd<1:
        total+=1
    else:
        total+=wantToAdd
    player1Turn=not player1Turn
if total>50:
    print("You guys need to learn how to play the game.")
elif total==50:
    if player1Turn==False:
        print("Player 1 won.")
    else:
        print("Player 2 wins")

