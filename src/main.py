import string

from models.game import Game, GameState
from models.letter import Letter


def ask_word():
    while True:
        word = input("Enter a 5-letter word: ").strip().lower()
        if len(word) == 5 and word.isalpha():
            return word
        print("Invalid word, try again.")


if __name__ == "__main__":
    game = Game()
    game.startNewGame()

    while(game.gameState == GameState.InProgress):
        while True:
            guess = ask_word()
            if game.isWordInWordList(guess):
                break
            else:
                print("Word not in list. Try another word")
            
        game.guessTheWord(guess)
        game.printAllLettersState()

    if game.gameState == GameState.Won:
        print("You won the game!")
    else:
        print("You lost the game!")
    print(f"The word was {str(game.wordToGuess)}")
    print(f"Number of guesses left : {str(game.numberOfGuessLeft)}")






