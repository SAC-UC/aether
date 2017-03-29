from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

@application.route('/style.css')
def style():
    return application.send_static_file('style.css')


if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)
