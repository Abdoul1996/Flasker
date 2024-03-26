from flask import Flask, render_template, flash
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "Djibouti"   # store in the app 


# Create a Form Class 
#csrf( it creates a screte key on the form)
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


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
def page500(e):
    return render_template("500.html"), 500



# Create name page 
@app.route('/name', methods=['GET', 'POST'])

def name():
    name = None
    form = NamerForm()
    # Validate form 
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successful")
    return render_template("name.html", 
                           name = name,
                           form = form)


