# integrate html with flask (jinja2 integration)
# HTTP verb and GET post

from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# @app.route('/sucess/<int:score>') #appending integer value
# def sucess(score):
#     return f'The person has pssed and scored {score} %'

# @app.route('/fail/<int:score>')
# def fail(score):
#     return f'The person has failed and scored {score} %'

@app.route('/result/<int:score>')
def result(score):
    if score<40:
        res='FAIL'
    else:
        res='PASS'
    return render_template('result.html',result=res,per=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        english=float(request.form['english'])
        hindi=float(request.form['hindi'])
        total=(science+math+english+hindi)/4
        return redirect(url_for('result',score=total))


if(__name__)=='__main__':
    app.run(debug=True)