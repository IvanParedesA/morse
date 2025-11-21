from fastapi import FastAPI
from pydantic import BaseModel
from antlr4 import *
from MorseLexer import MorseLexer
from MorseParser import MorseParser
from MorseListener import MorseListener
from MorseToPythonString import MorseToPythonString

app = FastAPI()

class MorseRequest(BaseModel):
    text: str

@app.post("/parse")
def parse_morse(req: MorseRequest):
    try:
        # Crear lexer y parser a partir del texto
        lexer = MorseLexer(InputStream(req.text))
        
        stream = CommonTokenStream(lexer)
        parser = MorseParser(stream)

        # Obtener árbol
        tree = parser.morse_code()

        # Listener personalizado
        listener = MorseToPythonString()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Resultado producido por tu listener
        result = listener.result if hasattr(listener, "result") else None

        return {
            "input": req.text,
            "result": result,
            "status": "ok"
        }

    except Exception as e:
        return {
            "error": str(e),
            "status": "error"
        }