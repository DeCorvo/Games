import random
from WordList import choice_words

def get_word():
    word = random.choice(choice_words)
    return word.upper()

def play(word):
    word_finished = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Parachute!")
    print(display_parachute(tries))
    print(word_finished)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that!")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_finished)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_finished = "".join(word_as_list)
                if "_" not in word_finished:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that!")
            elif guess != word:
                print("That's not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_finished = word
        else:
            print("Not a valid guess, try again.")
        print(display_parachute(tries))
        print(word_finished)
        print('\n')
    if guessed:
        print("WELL DONE! You guessed the word! You WIN!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_parachute(tries):
    stages = [ # final
        """
            ^^^^^
          ^^^^^^^^^
            |   |
            \ () /
             \|//
              ||
              /|
             / |
             
          ~~~~~~~~~   
        """,
        # 1 leg
        """
            ^^^^^
          ^^^^^^^^^
            |   |
            \ () /
             \|//
              ||
              /|
              
          ~~~~~~~~~
        """,
        # no legs
        """
            ^^^^^
          ^^^^^^^^^
            |   |
            \ () /
             \|//
             
          ~~~~~~~~~
        """,
        # no arms
        """
            ^^^^^
          ^^^^^^^^^
            |   |
            \ () /
            
          ~~~~~~~~~
        """,
        # no head
        """
            ^^^^^
          ^^^^^^^^^
            |   |
            
          ~~~~~~~~~
        """,
        # no strings
        """
            ^^^^^
          ^^^^^^^^^
          
          ~~~~~~~~~
        """,
        # Start - Sun
        """
                ☼
            
            ~~~~~~~~~
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()