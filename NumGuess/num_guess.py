print(' ----- Welcome in NumGuess ----- \n\n')

print('Choose Your option')
print('1. Play\n2. Rules\n3. Exit')

choice = input()

match(choice):
    case '1':
        print("Start playing")
    case '2':
        print("RULES!")
    case '3':
        print("Exit from game")
    case _:
        print("Error 890!")
