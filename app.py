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