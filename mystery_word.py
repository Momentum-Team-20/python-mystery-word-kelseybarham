import random


def play_game(file):
    # Open file reader
    with open(file, 'r') as reader:
        text = reader.read()

    word_list = text.lower().split()
    answer = random.choice(word_list)
    print(answer)

# get player's input 
def get_player_input():
    user_input = (input("Please enter a single letter: "))
    return user_input


# check to see if player's input is in answer, which will return true or false
def compare_letters():
    pass



# Based on results of compare letters function: if true, letter will appear in answer. if false, count goes down. This prints to the print line. If answer has not been guessed and count is greater than 0, the user will be asked for another input. If the answer has been guessed, message appears saying the player has won. If count is 0, you loose message appears.
def compare_answers():
    if count > 0:
        pass



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
