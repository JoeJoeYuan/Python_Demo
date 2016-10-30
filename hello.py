from flask import Flask, url_for
from flask import request, make_response
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world(): 
    return 'Hello World! TRUE..'

@app.route('/')
def index(): 
	resp = make_response(render_template(...))
	resp.set_cookie('name', 'the username')
    #return 'Welcome index page!'
	return resp

@app.route('/login')
def user_login(): 
	username = request.cookies.get('name')
	return username
    #user = username
    #return 'Login Page, your name: <strong> %s </strong>!' % user

#with app.test_request_context():
#    print url_for('index')
#    print url_for('hello')
#    print url_for('login', username='jprf43')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
