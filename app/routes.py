from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/horoscope', methods=['GET','POST'])
@app.route('/horoscope.html', methods=['GET','POST'])
def horoscope():
    sign = request.form.to_dict()['sign']
    prediction = model.horoscope(sign)
    return render_template('horoscope.html',sign=sign,prediction=prediction)
    
