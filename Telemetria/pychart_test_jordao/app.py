from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route("/")
def chart():
	temp_file = open('temp.txt', 'r')
	time_file = open('time.txt', 'r')
	temp = []
	time = []
	for line_1 in temp_file:
		temp = line_1.split()

	for line_2 in time_file:
		time = line_2.split()

	temp_file.close()
	time_file.close()

	return render_template('chart.html', values=temp, labels=time)
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001)
