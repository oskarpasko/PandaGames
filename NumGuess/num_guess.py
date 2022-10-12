import game, rules

print(' ----- Welcome in NumGuess ----- \n\n')

print('Choose Your option')
print('1. Play\n2. Rules\n3. Exit\n4. Rules\n5. Exit')

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
