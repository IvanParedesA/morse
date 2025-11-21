from antlr4 import *
from MorseLexer import MorseLexer
from MorseParser import MorseParser
from MorseListener import MorseListener

input_text = input('> ')
lexer = MorseLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = MorseParser(stream)
tree = parser.morse_code()
print(tree.toStringTree(recog=parser))