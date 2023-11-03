import random


def play_game(file):
    # Open file reader
    with open(file, 'r') as reader:
        text = reader.read()
    # create a list and lowercase it and pick a random word as an answer
    word_list = text.lower().split()
    answer = random.choice(word_list)
    print(f"The answer is: ", answer)
    guesses = []
    display = ["_" for character in answer]
    print(display)
    remaining_guesses = 8
    # get player input and begin loop:
    while remaining_guesses > 0:
        guess = input("Guess a letter: ")
        if len(guess) > 1 or not guess.isalpha():
            print('Guess only one letter and NO numbers!')
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





# Based on results of compare letters function: if true, letter will appear in answer. if false, count goes down. This prints to the print line. If answer has not been guessed and count is greater than 0, the user will be asked for another input. If the answer has been guessed, message appears saying the player has won. If count is 0, you loose message appears.
def compare_answers():
    if count > 0:
        pass

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
