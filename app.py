from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '99950799b8ac042ab96c3ed548c2c33b'

posts = [
    {
        "author": "Souvik Guria",
        "content": "My First Post",
        "title": "Blog Post 1",
        "date_posted": "20th Apr, 2021"
    },
    {
        "author": "John Doe",
        "content": "My Second Post",
        "title": "Blog Post 2",
        "date_posted": "21 th Apr, 2021"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="about")


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
