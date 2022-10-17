from dlcs import extra_level, codeguess, pvp
import num_guess
import os.path

# file_exists = os.path.exists('readme.txt')

def dlc():
    print('\n ------------------------------- ')
    print(' ---------- Your DLC ----------- ')
    print(' ------------------------------- \n')

    while(True):
        print('1. Play(Custom)\n2. CodeGuess\n3. PvP\n4. Back')
        choice = input('What do You choose?\n')

        match(choice):
            case '1':
                if(os.path.exists('dlcs/extra_level.py')):
                    extra_level.extra_level_game()
                else:
                    print('Error 1')
            case '2':
                if(os.path.exists('dlcs/codeguess.py')):
                    codeguess.codeguess_game()
                else:
                    print('Error 1')
            case '3':
                if(os.path.exists('dlcs/pvp.py')):
                    pvp.pvp_game()
                else:
                    print('Error 1')
            case '4':
                num_guess.numguess_game()
            case _:
                print('Error 890')