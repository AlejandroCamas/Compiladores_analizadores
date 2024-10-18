from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Definir los tokens y su tipo
def tokenize(expression):
    token_spec = [
        ('NUMBER',   r'\d+(\.\d*)?'),    # Números
        ('ADD',      r'\+'),             # Operador suma
        ('SUBTRACT', r'-'),              # Operador resta
        ('MULTIPLY', r'\*'),             # Operador multiplicación
        ('DIVIDE',   r'/'),              # Operador división
        ('LPAREN',   r'\('),             # Paréntesis izquierdo
        ('RPAREN',   r'\)'),             # Paréntesis derecho
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_spec)
    get_token = re.compile(token_regex).finditer
    tokens = [{'type': match.lastgroup, 'value': match.group()} for match in get_token(expression)]
    return tokens

# Evaluar la expresión aritmética
def eval_expr(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression', '')
    tokens = tokenize(expression)
    result = eval_expr(expression)
    return jsonify({'tokens': tokens, 'result': result})

@app.route('/history', methods=['POST'])
def history():
    data = request.json
    expression = data.get('expression', '')
    tokens = tokenize(expression)
    return jsonify({'tokens': tokens})

if __name__ == '__main__':
    app.run(debug=True)
