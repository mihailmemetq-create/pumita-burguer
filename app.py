import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza la página principal de Pumita
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)