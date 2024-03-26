from flask import Flask, render_template 

app = Flask(__name__)

# Create a route decorator 
@app.route('/')


#Filters: 
    #.safe : 
    #.capitalize
    #.lower/upper
    #title
    #trim
    #strptags

def index():
    first_name = "Abdoulfatah"
    stuff = "This is <strong>Bold</strong> Text"
    favorite_pizza = ["cheeze", "pepperoni", 45]
    return render_template("index.html", first_name = first_name,
                           stuff = stuff,
                           favorite_pizza = favorite_pizza)

#http://127.0.0.1:5001/user/name
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)


# Create custom Error Pages 
# Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
        