from MorseListener import MorseListener

class MorseToPythonString(MorseListener):

    TOKEN_MAP = {
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H",
        "I": "I",
        "J": "J",
        "K": "K",
        "L": "L",
        "M": "M",
        "N": "N",
        "O": "O",
        "P": "P",
        "Q": "Q",
        "R": "R",
        "S": "S",
        "T": "T",
        "U": "U",
        "V": "V",
        "W": "W",
        "X": "X",
        "Y": "Y",
        "Z": "Z",
        "ZERO": "0",
        "ONE": "1",
        "TWO": "2",
        "THREE": "3",
        "FOUR": "4",
        "FIVE": "5",
        "SIX": "6",
        "SEVEN": "7",
        "EIGHT": "8",
        "NINE": "9"
    }

    def __init__(self):
        self.output = []
        self.result = ""

    def exitLetter(self, ctx):
        token_name = ctx.getText()         # ejemplo '.-' → token A
        token_type = ctx.getChild(0).symbol.type
        token_str = ctx.parser.symbolicNames[token_type]
        self.output.append(self.TOKEN_MAP[token_str])

    def exitDigit(self, ctx):
        token_name = ctx.getText()
        token_type = ctx.getChild(0).symbol.type
        token_str = ctx.parser.symbolicNames[token_type]
        self.output.append(self.TOKEN_MAP[token_str])

    def exitMorse_code(self, ctx):
        self.result = "".join(self.output)