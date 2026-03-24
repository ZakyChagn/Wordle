from models.game import Game
from models.letter import Letter

game = Game()
#print(game.getNumberOfLetters())
#print(game.pickRandomWord())

#letter1 = Letter("A")
#letter2 = Letter("B")
#print(letter1.state)

#game.printAllLettersState()
newWord = game.pickRandomWord()
print(newWord)

#for l in newWord.letters:
#    print(l)

#print(game.returnLetterInstance("d"))
#print(game.returnLetterInstance("e"))
#print(game.returnLetterInstance("ff"))

game.startNewGame()
game.guessTheWord("focal")

#for i in range(5):
#    print(i)