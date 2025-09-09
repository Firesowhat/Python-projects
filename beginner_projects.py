import random
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
print(get_valid_word(words))

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()  # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died, sorry. The word was', words)
    else:
        print('YAY! You guessed the word', words, '!!')


