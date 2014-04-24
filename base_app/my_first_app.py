# This is whre you can start you python file for your week1 web app
# Name: Tyler Wallace

import flask, flask.views
import os
app = flask.Flask(__name__)

app.secret_key = "akdjfoab012382"

class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')
	def post(self):
		pass

class Remote(flask.views.MethodView):
	def get(self):
		return flask.render_template('remote.html')

	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()

app.add_url_rule('/',
	view_func=Main.as_view('index'),
	methods=['GET','POST'])
app.add_url_rule('/remote/', 
	view_func=Remote.as_view('remote'), 
	methods=['GET','POST'])

app.debug = True
app.run()
