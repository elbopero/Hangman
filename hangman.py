#Step 2

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

lives = 6
end_of_game = True

def run_game(display, end_of_game, stages, lives):
    while end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong. You have {lives} lives remaining.")
        else:
            i = 0
            for letter in chosen_word:
                if letter == guess:
                    display[i] = letter
                    print("Character is in the word.")
                i += 1
            
        print(stages[lives])
        
        for letter in display:
            print(letter, end="")

        print("\n\n")

        if lives == 0:
            print("You lose.")
            end_of_game = False
    

        if "_" not in display:
            print("You win!")
            end_of_game = False

run_game(display, end_of_game, stages, lives)