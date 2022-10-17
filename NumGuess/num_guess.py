import game, rules
import os.path


extra_level_path = os.path.exists('dlc/extra_level.py')

print(' ----- Welcome in NumGuess ----- \n\n')

while(True):

    if(extra_level_path == False):
        print('Choose Your option')
        print('1. Play(Easy)\n2. Play(Medium)\n3. Play(Hard)\n4. Rules\n5. Exit')

        choice = input()

        match(choice):
            case '1':
                game.game(0, 10, 5)
            case '2':
                game.game(0, 100, 10)
            case '3':
                game.game(0, 1000, 20)
            case '4':
                rules.rules()
            case '5':
                exit()
            case _:
                print("Error 890!")
    else:

        from dlc import extra_level
        print('Choose Your option')
        print('1. Play(Easy)\n2. Play(MEdium)\n3. Play(Hard)\n4. Play(Custom)\n5. Rules\n6. Exit')

        choice = input()

        match(choice):
            case '1':
                game.game(0, 10, 5)
            case '2':
                game.game(0, 100, 10)
            case '3':
                game.game(0, 1000, 20)
            case '4':
                extra_level.extra_level_game()
            case '5':
                rules.rules()
            case '6':
                exit()
            case _:
                print("Error 890!")