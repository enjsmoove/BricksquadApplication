#import the flask class. an instance of this class will be our bricksquad application
import flask, flask.views
from flask import render_template, url_for
import os
#Next we create an instance of this class.
#The first argument is the name of the application?s module or package
app = flask.Flask(__name__)
#Secret Key
app.secret_key = "bricksquad"

class View(flask.views.MethodView):
	#@app.route('/')
	def get(self):
		user = { 'nickname': 'Miguel' } # fake user
		return flask.render_template('index1.html', user = user)
	def post(self):
		result =  eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()