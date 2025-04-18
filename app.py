from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from configure import create_app, mysql

app = create_app()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_auth WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        hashed_password = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_auth WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user:
            cursor.close()
            return 'Username already taken! Try another one.'

        cursor.execute("INSERT INTO user_auth (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
