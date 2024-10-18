def parse_syntax(expression):
    # Función ficticia para mostrar el análisis sintáctico
    return {"parsed": expression}

def count_tokens(tokens):
    # Contar los tipos de tokens
    token_counts = {
        "total": len(tokens),
        "numbers": sum(1 for t in tokens if t[0] == 'NUMERO'),
        "symbols": sum(1 for t in tokens if t[0] in ['SUMA', 'RESTA', 'MULT', 'DIV']),
    }
    return token_counts
