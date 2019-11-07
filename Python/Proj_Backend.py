from flask import Flask, render_template
##from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
##app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///test.db'
##db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cats')
def cats():
    return render_template('cats.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs.html')

if __name__ == '__main__':
    app.run(debug=True)

