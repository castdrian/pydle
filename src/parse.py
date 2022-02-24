from random import randrange

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