import random

def pvp_game():
    print(' ----- PvP! -----')

    # players names
    player1 = input('First player name: ')
    player2 = input('Second player name: ')

    min_num = int(input('Choose Your minimal number: '))
    max_num = int(input('Choose Your maximum number: '))

    random_num = random.randint(min_num, max_num)

    while(True):
        player1_guess = int(input(f"{player1} choose number: "))
        player2_guess = int(input(f"{player2} choose number: "))


        # check who is the winner
        if(player1_guess == random_num):
            print(f"Congrats {player1}, You've guessed that!")
            break
        if(player2_guess == random_num):
            print(f"Congrats {player2}, You've guess that!")
            break
        if(player1_guess == random_num and player2_guess == random_num):
            print(f"Congrats! You both have guessed that!")

pvp_game()