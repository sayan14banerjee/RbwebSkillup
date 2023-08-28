import random 
#initialize plaayers score
player_1_Score=0
player_2_Score =0
#repeate the game for unlimitade 
c=True
while (c==True):
    #3 round game
    for i in range (3):
        #random dice score
        player_1_value= random.randint(1,6)
        player_2_value= random.randint(1,6)

        #score the player
        if player_1_value> player_2_value:
            player_1_Score +=1

        elif player_2_value> player_1_value:
            player_2_Score+=1
        else :
            continue
        print("Player one Score:",player_1_Score," Player two Score",player_2_Score)
    #check winers
    if player_1_Score> player_2_Score:
        print('Player 1 wins ') 
    else:
        print("Player 2 wins")
    y=input("Press y or enter key to continue to continue or preess any other key to exit")
    if y =="y" or "Y":
        c=True
    else:
        c=False  
