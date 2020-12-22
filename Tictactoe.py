def display(row):
    print("    {} | {} | {}     ".format(row[0],row[1],row[2]))
    print("--------------------")
    print("    {} | {} | {}     ".format(row[3],row[4],row[5]))
    print("--------------------")
    print("    {} | {} | {}     ".format(row[6],row[7],row[8]))
    
def player1turn(row,choice,position,available_position):
    while position not in available_position:
        position = input("\n Which position does Player 1 choose :\n")
        if position.isdigit():
            position = int(position)
        if position not in available_position:
            print("\n Please choose a valid position : \n")
    available_position.pop(available_position.index(position))
    row[position-1] = choice
    return row   

def player2turn(row,choice,position,available_position):
    while position not in available_position:
        position = input("\n Which position does Player 2 choose : \n")
        if position.isdigit():
            position = int(position)
        if position not in available_position:
            print("\nPlease choose a valid position : \n")
    available_position.pop(available_position.index(position))
    row[position-1] = choice
    return row   


def isgameover(row,choice,alt_choice):
    winset = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i,j,k in winset:
        if row[i]==row[j] and row[j]==row[k]:
            if row[i] == choice:
                print("\nPlayer 1 wins :) \n")
                return False
            elif row[i] == alt_choice:
                print("\nPlayer 2 wins :) \n")
                return False
            
    for i in row:
        if i == ' ':
            return True
    print("\nDraw :( \n")
    return False
    
    
def main():
    play_again = "Y"
    
    while play_again == "Y": 
        available_position = list(range(1,10))
        position = "random"
        ava_choice =['X','O']
        choice = 0
        row = []
        for i in range(0,9):
            row.append(' ')
        gameon = True

        print("Welcome to tic tac toe\n\n")
        while choice not in ava_choice:
                choice = input("\nWould player 1 choose X or O \n")
        ava_choice.pop(ava_choice.index(choice))
        alt_choice = ava_choice[0]

        while gameon:
            print("The current list is\n")
            display(row)
            row = player1turn(row,choice,position,available_position)
            gameon = isgameover(row,choice,alt_choice)
            if gameon==False:
                break
            print("The current list is\n")
            display(row)
            row = player2turn(row,alt_choice,position,available_position)
            gameon = isgameover(row,choice,alt_choice)

        play_again = input("\nDo you want to play again? Y or N \n")
        
main()