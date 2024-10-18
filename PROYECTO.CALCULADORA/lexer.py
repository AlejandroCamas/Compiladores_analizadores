import ply.lex as lex

# Tokens para operadores y números
tokens = [
    'SUMA', 'RESTA', 'MULT', 'DIV', 'NUMERO'
]

# Expresiones regulares para los tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejar errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def prueba(data):
    analizador = lex.lex()
    analizador.input(data)
    tokens = []
    while True:
        tok = analizador.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    return tokens
