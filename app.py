from flask import Flask, render_template

app = Flask(__name__)

# Définition de la route principale (la page d'accueil)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)