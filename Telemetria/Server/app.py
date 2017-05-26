from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)
 

@app.route('/homepage.html')
def homepage():
	return render_template('homepage.html')	

@app.route("/temperature.html")
def temp():
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

	return render_template('temperature.html', values=temp, labels=time)

@app.route("/altitude.html")
def alt():
	alt_file = open('alt.txt', 'r')
	time_file = open('time.txt', 'r')
	alt = []
	time = []
	for line_1 in alt_file:
		alt = line_1.split()

	for line_2 in time_file:
		time = line_2.split()

	alt_file.close()
	time_file.close()

	return render_template('altitude.html', values=alt, labels=time)
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001)
