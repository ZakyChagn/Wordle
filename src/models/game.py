from .player import Player
from .letter import Letter, LetterState
from .word import Word
import json
import random
import string
import os


class Game():
    def __init__(self):
        self.player = Player()
        self.words = []
        self.letters = { c:Letter(c) for c in string.ascii_lowercase}
        self.wordToGuess = None

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
        """Démarre une nouvelle partie. Reset l'état du jeu"""
        self.wordToGuess = self.pickRandomWord()
        self.player.reset()
        for letter in self.letters:
            self.letters[letter].reset()

    def printAllLettersState(self):
        for l in self.letters:
            print(self.letters[l])

    def guessTheWord(self, guess: str) -> bool:
        #Prévention si mot n'est pas de longueur 5
        if (len(guess) != 5):
            return False
        
        #Première boucle pour trouver les Valid
        indexLeftGuess = [i for i in range(5)] #[0, 1, 2, 3, 4]
        indexLeftWord = [i for i in range(5)] #[0, 1, 2, 3, 4]
        index = 0
        for i in guess:
            letterInstance = self.returnLetterInstance(i)
            if (self.wordToGuess.letters[index] == letterInstance.symbol):
                self.changeLetterState(letterInstance, LetterState.Valid)
                print("lettre guess : " + letterInstance.symbol)
                print(letterInstance.state)
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

            
            print(letterInstance.state)
            index += 1

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
        
        
        
    