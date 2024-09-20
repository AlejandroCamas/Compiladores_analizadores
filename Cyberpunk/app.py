#CARLOS ALEJANDRO MORENO CAMAS .

#AQUI SE COLOCA TODA NUESTRA PARTE LOGICA DE NUESTRO ANALIZADOR

#no olvidar importar la libreria flask sino no podremos haceruso de la misma.
from flask import Flask, request, render_template
import re

#import ply.lex as lex de esta manera es como llamamos a nuestra libreria,

app2 = Flask(__name__)

def lexico(text):
    # Encontrar todos los tokens (palabras y números)
    tokens = re.findall(r'\b\w+\b', text)
    line_info = []

    # Palabras clave a identificar
    #recordar que aqui nosotros indicamos las palabras que estaran reservadas y saldra el aviso de "palabra reservada."
    keywords = {'for': 'identificador'} 
 
    
    
    for i, token in enumerate(tokens):
        tipo = keywords.get(token, 'Palabra Libre')
        line_info.append((i + 1, tipo))
    
    return tokens, line_info

@app2.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        tokens, line_info = lexico(text)
        return render_template('index.html', tokens=tokens, text=text, line_info=line_info)
    
    return render_template('index.html', tokens=None, text=None, line_info=None)

if __name__ == '__main__':
    app2.run(debug=True)
