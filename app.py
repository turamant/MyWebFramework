from api import API


app = API()

def home(request, response):
    response.text = "Hello frrom the Home page"

def about(request, response):
    response.text = "Hello from the about page"