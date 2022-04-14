import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess the Number Between 1 to {} :'.format(x)))
        if guess < 1 or guess > x:
            print('Please Guess the Number Between 1 to {}'.format(x))
        elif guess < random_number:
            print('Too Low')
        elif guess > random_number:
            print('Too High')
    print('Congrates You Guessed the number Correctly! which was {}'.format(
        random_number))


guess(5)
