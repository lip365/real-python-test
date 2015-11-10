#imported Flask class from the flask library
from flask import Flask
#creatin application object
app = Flask(__name__)
#using decorators to link function to url
@app.route("/")
@app.route("/hello")

#define view function
def hello_world():
	return "hello world"

#start dev server with run method
if __name__ == "__main__":
	app.run()

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query
	
