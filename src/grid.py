import os
from colorama import Back, Style

def draw_blank_grid(word: str):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')
    
    for i in range(6):
        print('\u2B1C' * len(word))
    print('\n')

def update_grid(word: str, guess_list: list[str], amt: int):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')

    if len(guess_list) == 1:
        guess = ' '.join(guess_list[0])
        print(f' {guess}')
        
        for i in range(5):
            print('\u2B1C' * len(word))