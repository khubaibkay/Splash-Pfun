
player1Turn = True #This means it is currently player 1's turn
total = 0 #Initialize the total as 0
while total < 50: #Game continues till total is at least 50
    if player1Turn == True: 
        print ("Player 1's turn")
    else:
        print ("Player 2's turn")
    print ("The total amount of money in the pot is currently %s" % total) #How much money already in pot 
    wantToAdd = int(input("Enter any amount from 1-6 that you would like to add:")) #inputs the amount user wants to put
    if wantToAdd > 6: #if user decides to be oversmart and put >6.
        total += 6
    elif wantToAdd < 1:#if user decides to be oversmart and put <1.
        total += 1
    else:
        total += wantToAdd # Add to Total
    player1Turn = not player1Turn #Changes state. From Player 1's turn to Player 2's
if total > 50: # If both of them suck
    print("You guys need to learn how to play the game.")
elif total == 50: #if someone wins
    if player1Turn == False: #Game ended and it is supposed to be Player 2's turn so Player 1 wins
        print ("Player 1 won.")
    else: #If player 1 didn't win then player 2 did
        print ("Player 2 wins")
    print ("Loser, type some words for the winner")
    input()

