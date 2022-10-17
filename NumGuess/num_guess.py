import game, rules, dlc
import os.path

def numguess_game():
    extra_level_path = os.path.exists('dlc/extra_level.py')

    print('\n ------------------------------- ')
    print(' ----- Welcome in NumGuess ----- ')
    print(' ------------------------------- \n\n')



    while(True):
        print('Choose Your option')
        print('1. Play(Easy)\n2. Play(MEdium)\n3. Play(Hard)\n4. DLCs\n5. Rules\n6. Exit')

        choice = input()

        match(choice):
            case '1':
                game.game(0, 10, 5)
            case '2':
                game.game(0, 100, 10)
            case '3':
                game.game(0, 1000, 20)
            case '4':
                dlc.dlc()
            case '5':
                rules.rules()
            case '6':
                exit()
            case _:
                print("Error 890!")

if __name__ == '__main__':
    numguess_game()