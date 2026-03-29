import pytest
from models.game import Game
from models.letter import Letter, LetterState
from models.word import Word

@pytest.fixture(scope="session")
def create_game():
    game = Game()
    yield game 
    
@pytest.fixture(autouse=True)
def setup(create_game):
    create_game.startNewGame()
    return create_game 
    

def test_guess_word_all_good(setup):
    setup.wordToGuess = Word("cried")
    setup.guessTheWord("cried")

    for l in setup.wordToGuess.word:
        letter = setup.returnLetterInstance(l)
        assert letter.state == LetterState.Valid

def test_guess_word_1_good(setup):
    setup.wordToGuess = Word("cried")
    setup.guessTheWord("canal")

    letter = setup.returnLetterInstance("c")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("a")
    assert letter.state == LetterState.Invalid

    letter = setup.returnLetterInstance("n")
    assert letter.state == LetterState.Invalid

    letter = setup.returnLetterInstance("l")
    assert letter.state == LetterState.Invalid

    letter = setup.returnLetterInstance("r")
    assert letter.state == LetterState.Unknown

    letter = setup.returnLetterInstance("i")
    assert letter.state == LetterState.Unknown

    letter = setup.returnLetterInstance("e")
    assert letter.state == LetterState.Unknown

    letter = setup.returnLetterInstance("d")
    assert letter.state == LetterState.Unknown

def test_guess_word_4_good(setup):
    setup.wordToGuess = Word("daddy")
    setup.guessTheWord("caddy")

    letter = setup.returnLetterInstance("a")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("d")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("y")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("c")
    assert letter.state == LetterState.Invalid

def test_guess_word_3_good(setup):
    setup.wordToGuess = Word("canny")
    setup.guessTheWord("carry")

    letter = setup.returnLetterInstance("c")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("a")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("r")
    assert letter.state == LetterState.Invalid

    letter = setup.returnLetterInstance("y")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("n")
    assert letter.state == LetterState.Unknown

def test_guess_word_2_good_2_wrong_place(setup):
    setup.wordToGuess = Word("cheat")
    setup.guessTheWord("chase")

    letter = setup.returnLetterInstance("c")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("h")
    assert letter.state == LetterState.Valid

    letter = setup.returnLetterInstance("a")
    assert letter.state == LetterState.WrongPlace

    letter = setup.returnLetterInstance("s")
    assert letter.state == LetterState.Invalid

    letter = setup.returnLetterInstance("e")
    assert letter.state == LetterState.WrongPlace

    letter = setup.returnLetterInstance("t")
    assert letter.state == LetterState.Unknown

def test_change_letter_state(setup):
    #Unknown -> Valid
    letterInstanceA = Letter("a")
    setup.changeLetterState(letterInstanceA, LetterState.Valid)
    assert letterInstanceA.state == LetterState.Valid

    #Unknown -> Invalid
    letterInstanceA = Letter("a")
    setup.changeLetterState(letterInstanceA, LetterState.Invalid)
    assert letterInstanceA.state == LetterState.Invalid

    #Unknown -> WrongPlace
    letterInstanceA = Letter("a")
    setup.changeLetterState(letterInstanceA, LetterState.WrongPlace)
    assert letterInstanceA.state == LetterState.WrongPlace

    #WrongPlace -> Unknown
    letterInstanceB = Letter("b")
    setup.changeLetterState(letterInstanceB, LetterState.WrongPlace)
    setup.changeLetterState(letterInstanceB, LetterState.Unknown)
    assert letterInstanceB.state == LetterState.WrongPlace

    #WrongPlace -> Invalid
    letterInstanceB = Letter("b")
    setup.changeLetterState(letterInstanceB, LetterState.WrongPlace)
    setup.changeLetterState(letterInstanceB, LetterState.Invalid)
    assert letterInstanceB.state == LetterState.WrongPlace

    #WrongPlace -> Valid
    letterInstanceB = Letter("b")
    setup.changeLetterState(letterInstanceB, LetterState.WrongPlace)
    setup.changeLetterState(letterInstanceB, LetterState.Valid)
    assert letterInstanceB.state == LetterState.Valid

    #invalid -> Valid
    letterInstanceC = Letter("c")
    setup.changeLetterState(letterInstanceC, LetterState.Invalid)
    setup.changeLetterState(letterInstanceC, LetterState.Valid)
    assert letterInstanceC.state == LetterState.Invalid

    #invalid -> WrongPlace
    letterInstanceC = Letter("c")
    setup.changeLetterState(letterInstanceC, LetterState.Invalid)
    setup.changeLetterState(letterInstanceC, LetterState.WrongPlace)
    assert letterInstanceC.state == LetterState.Invalid

    #Valid -> WrongPlace
    letterInstanceD = Letter("d")
    setup.changeLetterState(letterInstanceD, LetterState.Valid)
    setup.changeLetterState(letterInstanceD, LetterState.WrongPlace)
    assert letterInstanceD.state == LetterState.Valid

    #Valid -> Invalid
    letterInstanceD = Letter("d")
    setup.changeLetterState(letterInstanceD, LetterState.Valid)
    setup.changeLetterState(letterInstanceD, LetterState.Invalid)
    assert letterInstanceD.state == LetterState.Valid