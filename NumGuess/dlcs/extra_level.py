import random

def extra_level_game():

    min_num = int(input('Choose Your minimal number'))
    max_num = int(input('Choose Your maximum number'))
    attempt = int(input('How many attempt do You want have?'))

    random_num = random.randint(min_num, max_num)

    for x in range(0, attempt):
        guess = input('Guess Number!')
        guess = int(guess)

        if(guess == random_num):
            print('Bravo, this is number which You had to guess!')
            break
        elif(guess > random_num):
            print('To much')
        else:
            print('Not enough!')

        if(x == 3):
            print('This is Your last chance!')      