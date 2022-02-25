def game_logic(word: str, guess_list: list[str], amt: int):
    current_guess = guess_list[len(guess_list) - 1]

    if current_guess == word:
        print(f'You won! {6 - amt}/6')
        exit()