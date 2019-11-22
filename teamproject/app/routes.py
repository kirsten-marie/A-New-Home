from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    type = {'type': 'Cats'}
    return render_template('index.html', type=type)

@app.route('/test')
def test():
    type = {'type': 'Cats'}
    return render_template('test.html', type=type)

@app.route('/template')
def template():
    type = {'type': 'Cats'}
    cats = [
        {
            'shelterLogo':'static/img/YWACLogo.jpg',
            'image': 'static/img/cat1.png',
            'name': 'Ramen',
            'age': '7M',
            'gender': 'Male',
            'weight': '3.2 LB',
            'description': 'I am a little shy and will need some time to warm up, but I would still love a home.',
            'url': 'https://www.young-williams.org/adopt-a-pet/adopt-a-cat/#sl_embed&page=shelterluv_wrap_1527306539435%2Fpublish_animal%2FYWAC-A-165809%3Fspecies%3DCat%26intakeType%3D%26status%3D'
        },
        {
            'shelterLogo':'static/img/YWACLogo.jpg',
            'image': 'static/img/cat3.jpg',
            'name': 'Sarah',
            'age': '5Y 1M',
            'gender': 'Female',
            'weight': '7.3 LB',
            'description': 'I am a small grey and white adult cat with short hair. I have been spayed. I want to find my new home.',
            'url': 'https://www.petfinder.com/cat/sarah-46288612/tn/knoxville/humane-society-of-the-tennessee-valley-tn178/'
        }
    ]
    return render_template('template.html', type=type, animals=cats)