import random

def game(min_num, max_num, attempt):
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

        if(x == (attempt - 2)):
            print('This is Your last chance!')
        