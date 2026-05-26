from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Esto funcionará en tu PC local, y Render lo gestionará automáticamente en la nube
    app.run(debug=True)