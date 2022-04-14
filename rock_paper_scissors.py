import random
def is_win(userInput,comInput):
    if (userInput == 'r' and comInput == 's') or (userInput == 's' and comInput == 'p') or (userInput == 'p' and comInput == 'r'):
        return True
    else:
        return False
def play():
    userInput=input("Whats Your Choice! Press 'r' for rock, 'p for paper 's' for scissors : ")
    compInput=random.choice(['r','p','s'])
    if userInput==compInput:
        return "Tie"
    if is_win(userInput,compInput):
        return "Congrates ! You Won"
    return 'You Lost'


print(play())

