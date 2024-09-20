import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'RESERVADA',
    'LIBRE',
)

# Definición de la palabra reservada
reserved = {
    'fora': 'RESERVADA'
}

# Reglas de expresión regular para tokens simples
t_RESERVADA = r'fora'
t_LIBRE = r'[a-zA-Z_][a-zA-Z_0-9]*'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Definición de la gramática
def p_statement_reserved(p):
    'statement : RESERVADA'
    p[0] = ("RESERVADA", p[1])

def p_statement_free(p):
    'statement : LIBRE'
    p[0] = ("LIBRE", p[1])

def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()

# Función para analizar el texto
def analizar(texto):
    lexer.input(texto)
    resultado = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado.append(parser.parse(tok.value))
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    texto = "fora variable1 variable2"
    resultado = analizar(texto)
    for tipo, valor in resultado:
        print(f"{valor}: {tipo}")
