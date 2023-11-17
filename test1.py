from flask import Flask, redirect , url_for , render_template , request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'testovkliuch'
app.permanent_session_lifetime = timedelta(days=5)

user_pass = {'ivan': 'vanko1'}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home_page_login.html', username=session['username'])
    else:
        return render_template('home_page_login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        if username in user_pass and pwd == user_pass[username]:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error = 'Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user_pass[username] = pwd
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)


