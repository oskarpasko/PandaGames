import game, rules

print(' ----- Welcome in NumGuess ----- \n\n')

print('Choose Your option')
print('1. Play\n2. Rules\n3. Exit')

choice = input()

match(choice):
    case '1':
        game(0, 10, 5)
    case '2':
        game(0, 100, 10)
    case '3':
        game(0, 1000, 20)
    case '4':
        print("RULES!")
    case '5':
        print("Exit from game")
    case _:
        print("Error 890!")
