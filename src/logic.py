from colorama import Fore

def game_logic(word: str, guess_list: list[str], amt: int):
    current_guess = guess_list[len(guess_list) - 1]

    if current_guess == word:
        print(f'You won! {6 - amt}/6')
        exit()

def apply_colors(word: str, guess: str) -> list[str]:
    word_chars = [char for char in word]
    guess_chars = [char for char in guess]
    colored_chars = []

    for idx, val in enumerate(guess_chars):
        if val == word_chars[idx]: colored_chars.append(f'{Fore.GREEN}{val}{Fore.RESET}')
        else:
            if val in word_chars: colored_chars.append(f'{Fore.YELLOW}{val}{Fore.RESET}')
            else: colored_chars.append(val)

    return colored_chars
