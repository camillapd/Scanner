from tokentype import TokenType

class Token():

    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self):
        literal_str = repr(self.literal) if self.literal is not None else "None"
        return f"{self.type.value} {self.lexeme} {literal_str}"
    