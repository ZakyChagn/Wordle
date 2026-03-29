from .letter import Letter, LetterState
from .word import Word
import json
import random
import string
import os
from enum import Enum

MAX_TRIES = 6

class GameState(Enum):
    InProgress = 1
    Won = 2
    Lost = 3

class Game():
    def __init__(self):
        self.words = []
        self.letters = { c:Letter(c) for c in string.ascii_lowercase}
        self.wordToGuess = None
        self.numberOfGuessLeft = MAX_TRIES
        self.gameState = GameState.InProgress

        # Get the directory where the current script is located
        script_dir = os.path.dirname(__file__)
        # Construct the path to the JSON file in the parent directory
        json_path = os.path.join(script_dir, '../..', 'wordles.json')
        with open(json_path, "r", encoding="utf-8") as f:
            self.words = json.load(f)

    def getNumberOfWords(self):
        return len(self.words)

    def pickRandomWord(self):
        index = random.randint(0, self.getNumberOfWords())
        return Word(self.words[index])
    
    def startNewGame(self):
        """Start a new game. Reset the state of the game"""
        self.wordToGuess = self.pickRandomWord()
        self.numberOfGuessLeft = MAX_TRIES
        self.gameState = GameState.InProgress
        self.player.reset()
        for letter in self.letters:
            self.letters[letter].reset()

    def printAllLettersState(self):
        for l in self.letters:
            print(self.letters[l])

    def guessTheWord(self, guess: str) -> list:
        #Validate if the lenght of the word is equal to 5 and if there is a guess left
        if (len(guess) != 5 and self.numberOfGuessLeft > 0):
            return []
        
        #Première boucle pour trouver les Valid
        indexLeftGuess = [i for i in range(5)] #[0, 1, 2, 3, 4]
        indexLeftWord = [i for i in range(5)] #[0, 1, 2, 3, 4]
        returnValues = []
        index = 0
        for i in guess:
            letterInstance = self.returnLetterInstance(i)
            if (self.wordToGuess.letters[index] == letterInstance.symbol):
                self.changeLetterState(letterInstance, LetterState.Valid)
                returnValues.append(letterInstance)
                indexLeftGuess.remove(index)
                indexLeftWord.remove(index)
            index += 1

        #Deuxième boucle pour trouver les WrongPlace et invalides
        index = 0
        for l in range(5):
            if (l not in indexLeftGuess):
               index += 1
               continue
            letterInstance = self.returnLetterInstance(guess[l])
            isLetterInWord = False
            indexToRemove = 0
            for i in range(5):
                if (i not in indexLeftWord):
                    continue
                if (letterInstance.symbol == self.wordToGuess.letters[i]):
                    self.changeLetterState(letterInstance, LetterState.WrongPlace)
                    isLetterInWord = True
                    indexToRemove = i
                    break

            if (isLetterInWord):
                indexLeftWord.remove(indexToRemove)
            else:
                self.changeLetterState(letterInstance, LetterState.Invalid)

            returnValues.append(letterInstance)
            index += 1

        self.numberOfGuessLeft -= 1
        self.checkGameState(returnValues)
        return returnValues

    def returnLetterInstance(self, letter: str) -> Letter:
        return self.letters.get(letter)
    
    def changeLetterState(self, letterInstance: Letter, state: LetterState):
        if letterInstance.state == LetterState.Valid or letterInstance.state == LetterState.Invalid or state == LetterState.Unknown:
            return
        elif state == LetterState.WrongPlace:
            letterInstance.state = state
        elif letterInstance.state == LetterState.WrongPlace:
            if state == LetterState.Valid:
                letterInstance.state = state  
        else:
            letterInstance.state = state
    
    def checkGameState(self, values: Letter):
        numberOfValidLetters = 0
        for l in values:
            if l.state == LetterState.Valid:
                numberOfValidLetters += 1
                
        if numberOfValidLetters == 5:
            self.gameState = GameState.Won
        elif self.numberOfGuessLeft <= 0:
            self.gameState = GameState.Lost
        else:
            self.gameState = GameState.InProgress
        
    def isWordInWordList(self, guess: str) -> bool:
        return guess in self.words
    