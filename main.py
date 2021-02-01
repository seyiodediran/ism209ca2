from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__) # create a flask app named app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:seyi@localhost:5439/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'g\x0b\xaa\xaf0\xd6\n\x88\x1aI9o\x7f\xa5\n\xa4%Ek\xc5\x93\xa6\xa6\n'

db = SQLAlchemy(app)


@app.route("/")
def home():
    # return ''' My name is Seyi Odediran. This is my CA2 work. My GitHub URL is https://github.com/seyiodediran/ism209ca2 '''
    # In the return statement above, Use your own name and GitHub URL


    return render_template('index.html')


@app.route("/process-signup/", methods=['POST'])
def process_signup():

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['dob']
        Residential = request.form['residential']
        Nationality = request.form['nationality']
        nin = request.form['nin']

        # write to database
        try:

            user = models.User(firstname=firstname, lastname=lastname, dob=dob, Residential=Residential, Nationality=Nationality, nin=nin )


            db.session.add(user)
            db.session.commit()

        except Exception as e:
            error = "There was an error in the sign up process. The error is {}".format(e.__cause__)
            return render_template('index.html', information=error, css="is-danger")

        return render_template('index.html', information="Sign up was successful", css="is-success")


@app.route("/users")
def users():

    users = models.User.query.all()

    return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(port=5005)