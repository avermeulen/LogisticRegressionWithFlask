from flask import Flask
from flask import render_template, request
from obesity import obesity_score;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/obesity", methods=['POST'])
def obesity():
	
	weight = request.form['weight']
	height = request.form['height']

	score = 0

	if len(weight) > 0 and len(height) > 0:
		score = obesity_score(int(weight), int(height))
	return render_template('index.html', weight=weight, height=height, score=score)
	# return redirect('/')	


