import random
from words import word_list
from DisplayHangman import display_hangman


def get_word():
    """Selects and returns a random word from the word list."""
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """Handles the logic of playing the game of Hangman."""
    word_completion = "_" * len(word)  # The word display with underscores for unguessed letters
    guessed = False  # Flag to check if the word has been guessed
    guessed_letters = []  # List to track guessed letters
    guessed_words = []  # List to track guessed words
    tries = 6  # Number of tries before the game ends
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():  # Single letter guess
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():  # Word guess
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
                
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def main():
    """Main function to run the Hangman game."""
    wins = 0
    losses = 0
    play_again = "Y"
    
    while play_again == "Y":
        word = get_word()
        play(word)
        play_again = input("Play Again? (Y/N) ").upper()
        
        if play_again == "Y":
            print("\nStarting a new game...\n")
        elif play_again == "N":
            print("\nThanks for playing Hangman!")
        else:
            print("\nInvalid input. Exiting the game.")
    
    print(f"Final Score: Wins: {wins}, Losses: {losses}")


if __name__ == "__main__":
    main()
