from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        expression = request.form.get('expression')
        try:
            result = eval(expression)  # No es recomendable usar eval en producción por razones de seguridad.
            tokens = tokenize_expression(expression)
            token_counts = count_tokens(tokens)
            tree_data = expression  # Enviar la expresión cruda a la página para construir el árbol.
        except Exception as e:
            result = f"Error: {e}"
            tokens = []
            token_counts = {'total': 0, 'numbers': 0, 'symbols': 0}
            tree_data = ''
        return render_template('calculadora.html', expression=expression, result=result, tokens=tokens, token_counts=token_counts, tree_data=tree_data)
    return render_template('calculadora.html', expression='', result=None, tokens=[], token_counts={}, tree_data='')

@app.route('/tree')
def tree():
    return render_template('tree.html')

def tokenize_expression(expression):
    import re
    tokens = re.findall(r'\d+|[-+*/()]', expression)
    return [(token, 'Number' if token.isdigit() else 'Operator') for token in tokens]

def count_tokens(tokens):
    numbers = sum(1 for token, token_type in tokens if token_type == 'Number')
    symbols = sum(1 for token, token_type in tokens if token_type == 'Operator')
    return {'total': len(tokens), 'numbers': numbers, 'symbols': symbols}

if __name__ == '__main__':
    app.run(debug=True)
