# building url dynamically

from flask import Flask,redirect,url_for

app =Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome My Friend Welcome'

@app.route('/sucess/<int:score>') #appending integer value
def sucess(score):
    return f'The person has pssed and scored {score}'

@app.route('/fail/<int:score>')
def fail(score):
    return f'The person has failed and scored {score}'


@app.route('/result/<int:marks>')
def result(marks):
    result =""
    if marks<33:
        result = "fail"
    else:
        result = "sucess"
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)