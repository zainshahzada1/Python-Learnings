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

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess=low
        feedback =input(f'Please Tell Is {guess} is High (H),Low(L) or Correct (C)')
        if feedback=='h': 
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Congrates Computer Guessed the Number Correctly! Which is {guess}')

computer_guess(100)
