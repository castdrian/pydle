from random import randrange
from src.grid import draw_blank_grid, update_grid

def get_word() -> str:
    try:
        with open('words.txt', 'r') as file:
            words = file.readlines()

            if len(words) == 0:
                print('words.txt contains no words')
                exit()
            
            return words[randrange(len(words))]
    except OSError:
        print('Couldn\'t find words.txt')
        exit()

def await_input(word: str, guess_list: list[str]) -> str:
    guess = input().lower()

    while len(guess) != len(word):
        if len(guess_list) == 0: draw_blank_grid(word)
        else: update_grid(word, guess_list)
        guess = input().lower()

    return guess