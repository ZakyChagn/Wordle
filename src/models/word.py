from .letter import Letter, LetterState

class Word:
    def __init__(self, word: str):
        """Construction d'un mot avec une chaine de caractères"""
        self.letters = [Letter(c) for c in word]
        self.word = word

    def validateLetter(self, letter: Letter, index: int):

        if (len(letter != 5)):
            return LetterState.Unknown
        isLetterInWord = letter in self.letters
        if (self.letters[index] == letter.symbol):
            letterState = LetterState.Valid
        elif (isLetterInWord):
            letterState = LetterState.WrongPlace
        else:
            letterState = LetterState.Invalid
        return letterState

    def __str__(self):
        return self.word

