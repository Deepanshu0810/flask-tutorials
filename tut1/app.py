from flask import Flask
app = Flask(__name__) #it is the wsgi app which interacts with the web server

@app.route('/') #decorator
def welcome():
    return 'Welcome to my App'

@app.route('/admin')
def adminFunc():
    return 'This is a restricted page'

#starting point of the app
if __name__=='__main__':
    app.run(debug=True) #to update the changes without restarting 