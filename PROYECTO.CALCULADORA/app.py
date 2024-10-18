from flask import Flask, render_template, request
from lexer import prueba as run_lexer
from parser import parse_syntax, count_tokens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = None
    tokens = []
    syntax_result = {}
    token_counts = {
        "total": 0,
        "reserved_words": 0,
        "identifiers": 0,
        "variables": 0,
        "numbers": 0,
        "symbols": 0
    }
    tree_data = ""

    if request.method == "POST":
        expression = request.form["expression"]
        try:
            # Evaluar la expresión matemática
            result = eval(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
        
        # Realizar análisis léxico
        tokens = run_lexer(expression)
        token_counts = count_tokens(tokens)
        syntax_result = parse_syntax(expression)
        
        # Generar el árbol (simplificado como string)
        tree_data = f"Operación: {expression} = {result}"

    return render_template(
        "index.html", 
        expression=expression, 
        result=result, 
        tokens=tokens, 
        token_counts=token_counts, 
        syntax_result=syntax_result,
        tree_data=tree_data
    )

if __name__ == "__main__":
    app.run(debug=True)
