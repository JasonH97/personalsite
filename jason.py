from flask import Flask, render_template, url_for
# export FLASK_APP=flaskblog.py -> point flask to main file
# export FLASK_DEBUG=1 -> enable debug mode
app = Flask(__name__)


@app.route("/") # homepage
@app.route("/home") # homepage (alt path)
def home():
    html = render_template('home.html')
    return html

if __name__ == '__main__': # only true when running script directly
    app.run(debug=True)

