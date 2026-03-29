import string

from models.game import Game
from models.letter import Letter

game = Game()
#print(game.getNumberOfLetters())
#print(game.pickRandomWord())

#letter1 = Letter("A")
#letter2 = Letter("B")
#print(letter1.state)

#newWord = game.pickRandomWord()
#print(newWord)

#for l in newWord.letters:
#    print(l)

#print(game.returnLetterInstance("d"))
#print(game.returnLetterInstance("e"))
#print(game.returnLetterInstance("ff"))

game.startNewGame()
#game.guessTheWord("daddy")

game.guessTheWord("caddy")

game.printAllLettersState()

#game.guessTheWord("cried")
#game.printAllLettersState()

#for i in range(5):
#    print(i)



#Tester les dictionnaires
#d = { c:Letter(c) for c in string.ascii_lowercase}
# for l in d:
#     print(d[l]) 