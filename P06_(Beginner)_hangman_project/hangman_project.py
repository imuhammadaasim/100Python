import random
from hangman_art import *
from hangman_words import *

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
# for _ in range(word_length):
#     display += "_"

for num in range(word_length):
    display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed: {guess}")

    for index, letter in enumerate(chosen_word):
        # print(f"Current position: {index}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[index] = letter

    # Check guessed letter
    # for position in range(word_length):
    #     letter = chosen_word[position]
    #     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    #     if letter == guess:
    #         display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not the correct word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Loose")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if chosen_word == "".join(display):
        game = True
        print("You Win")

    # if "_" not in display:
    #     end_of_game = True
    #     print("You Win")

    print(stages[lives])