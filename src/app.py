
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/v")
def version():
	return "0.0.1" 

if __name__ == "__main__":
	app.run()

	
