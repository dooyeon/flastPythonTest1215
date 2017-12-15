from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from datetime import datetime
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        'main.html',
        title='Login Page',
        #year=datetime.now().year,
    )

@app.route('/go_board', methods=['GET', 'POST'])
def go_board():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('login_success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('login_success', name=user))

@app.route('/login_success/<name>')
def login_success(name):
    """Renders the home page."""
    return render_template(
        'index.html',
        title=name,
        year=datetime.now().year,
    )

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'main.html', name=name)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/board/list')
def list():
    """Renders the about page."""
    return render_template(
        '/board/list.html'
    )

if __name__ == '__main__':
    app.debug = True
    app.run()



################################################################################################
################################################################################################
################################################################################################
################################################################################################





################################################################################################
################################################################################################
################################################################################################
################################################################################################