import random


def play_game(file):
    # Open file reader
    with open(file, 'r') as reader:
        text = reader.read()
    # create a list and lowercase it and pick a random word as an answer
    word_list = text.lower().split()
    answer = random.choice(word_list)
    print(f"The answer is: ", answer)
    print(f'There are {len(answer)} letters in the Mystery Word.')
    guesses = []
    display = ["_" for character in answer]
    # How the game will be won is by the number of underscores in display equaling 0 
    print(display)
    remaining_guesses = 8
    # get player input and begin loop:
    while remaining_guesses > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print('Guess only one letter and NO numbers!')
        elif guess in guesses:
            print('You already guessed that letter, try again')
        else:
            guesses.append(guess)
            if guess in answer:
                print('Correct')
            else:
                remaining_guesses = remaining_guesses-1
                print('Incorrect. You have ', f'{remaining_guesses} left')
            for index in range(len(answer)):
                if guess == answer[index]:
                    display[index] = guess
                    print(display)
            if answer == ''.join(display):
                print('Congratulations, you won the game!')
                break
    if remaining_guesses == 0:
        print('You lost! The Mystery Word was:', f'{answer}')

    reboot_game = input('Want to play the game again? Type Y/N: ').lower()
    if reboot_game == 'y':
        play_game(file)
    else:
        exit()


# The whole game needs to be in it's own loop to be able to play again

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Guess the mystery word')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
