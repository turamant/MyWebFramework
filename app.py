from api import API


app = API()

@app.route("/")
def index(request, response):
    response.text = "Hello index Page"

@app.route("/home")
def home(request, response):
    response.text = "Hello frrom the Home page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the about page"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"

@app.route("/tell/{age:d}")
def get_age(request, response, age):
    response.text = "Your age is %d" % age





