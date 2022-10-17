from dlcs import *
import os.path

# file_exists = os.path.exists('readme.txt')

def dlc():
    dlcs = ['extra_level.py', 'codeguess.py', 'pvp.py']
    existed_dlc = []

    for dlc in dlcs:
        if os.path.exists('dlcs/'+dlc):
            existed_dlc.append(dlc)

    print('\n ------------------------------- ')
    print(' ---------- Your DLC ----------- ')
    print(' ------------------------------- \n')

    for dlc in range(len(existed_dlc)):
        print(f"{dlc+1}. {_convert(existed_dlc[dlc])}")

    choice = input('\n Which one You wanna play?\n')





def _convert(dlc):
    match(dlc):
        case 'extra_level.py':
            return "Play (Custom)"
        case 'codeguess.py':
            return "CodeGuess"
        case 'pvp.py':
            return "PvP"
        case _:
            print("Error 400!")

dlc()