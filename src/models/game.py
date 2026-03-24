from .player import Player
from .letter import Letter, LetterState
from .word import Word
import json
import random
import string


class Game():
    def __init__(self):
        self.player = Player()
        self.words = []
        self.letters = [Letter(c) for c in string.ascii_lowercase]
        self.wordToGuess = None
        with open("../wordles.json", "r", encoding="utf-8") as f:
            self.words = json.load(f)

    def getNumberOfWords(self):
        return len(self.words)

    def pickRandomWord(self):
        #index = random.randint(0, self.getNumberOfWords())
        #return Word(self.words[index])
        return Word("cried")
    
    def startNewGame(self):
        """Démarre une nouvelle partie. Reset l'état du jeu"""
        self.wordToGuess = self.pickRandomWord()
        self.player.reset()
        for letter in self.letters:
            letter.reset()

    def printAllLettersState(self):
        for l in self.letters:
            print(l)

    def guessTheWord(self, guess: str) -> bool:
        #Prévention si mot n'est pas de longueur 5
        if (len(guess) != 5):
            return False
        
        #Première boucle pour trouver les Valid
        indexLeftGuess = [i for i in range(5)] #[0, 1, 2, 3, 4]
        indexLeftWord = [i for i in range(5)] #[0, 1, 2, 3, 4]
        #print(indexLeftGuess)
        #print(indexLeftWord)
        index = 0
        for i in guess:
            letterInstance = self.returnLetterInstance(i)
            if (self.wordToGuess.letters[index] == letterInstance.symbol):
                letterInstance.state = LetterState.Valid
                print("lettre guess : " + letterInstance.symbol)
                print(letterInstance.state)
                indexLeftGuess.pop(index)
                indexLeftWord.pop(index)
            index += 1

        #Deuxième boucle pour trouver les WrongPlace et invalides
        index = 0
       
        for l in range(5):
            if (l not in indexLeftGuess):
               index += 1
               continue
            letterInstance = self.returnLetterInstance(guess[l])
           
            print("lettre guess : " + letterInstance.symbol)
            print("indexLeft", indexLeftWord)
            isLetterInWord = False
            indexToRemove = 0
            for i in range(5):
                if (i not in indexLeftWord):
                    continue
                if (letterInstance.symbol == self.wordToGuess.letters[i]):
                    letterInstance.state = LetterState.WrongPlace
                    isLetterInWord = True
                    indexToRemove = i
                    break
                    

            if (isLetterInWord):
                indexLeftWord.remove(indexToRemove)
            else:
                letterInstance.state = LetterState.Invalid
            
            print(letterInstance.state)
            index += 1

    def returnLetterInstance(self, letter: str) -> Letter:
        instance = None
        for l in self.letters:
            if l == letter:
                instance = l
                break
        return instance
    