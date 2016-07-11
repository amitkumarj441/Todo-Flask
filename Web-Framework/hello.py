// Author: Amit Kumar Jaiswal

from flask import Flask, render_template, jsonify
app=Flask(_name_)

@app.route("/")
def hello():
	return "Hello World!"

#returns an HTML webpage

@app.route("/home/<username>")
def home(username):
	return render_template('profile.html',name=username)

#returns a piece of data in JSON Format
@app.route("/lotsofdata")
def people():
	my_people = {'Tessa Mero': 25,
				 'Alex Richardsson': 27
				 'Jon Archiebald': 27
				 'Michael Dziewonski': 38}
	return jsonify(my_people)

if _name_ == "_main_":
	app.run(debug=True)
