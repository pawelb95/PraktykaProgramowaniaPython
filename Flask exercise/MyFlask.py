from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
import sqlite3

app = Flask("FlaskApplication")
DATABASE = "myPersonalDatabase.db"


sess = Session()


@app.route('/create_database', methods=['GET'])
def create_database():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE users (username TEXT, password TEXT, admin INT)')
    conn.commit()
    conn.execute('INSERT INTO users (username,password,admin) VALUES (?,?,?)', ("admin", "admin", 1))
    conn.commit()
    conn.execute('INSERT INTO users (username,password,admin) VALUES (?,?,?)', ("Clint", "Eastwood", 0))
    conn.commit()
    conn.execute('CREATE TABLE books (title TEXT, author TEXT)')
    conn.commit()
    conn.execute('INSERT INTO books (title, author) VALUES (?,?)', ("Dune", "Frank Herbert"))
    conn.commit()
    conn.close()
    print("HELLO GIT")
    return index()


@app.route('/', methods=['GET'])
def index():
    if 'user' in session:
        admin_allowed = check_admin_privilage(session['user'])
        books = get_books()
        return render_template('mainPage.html', books=books, adminAllowed=admin_allowed)
    else:
        return render_template('loginPage.html')


@app.route('/login', methods=['POST'])
def login():
    req_form = request.form.to_dict()
    users = get_users()
    for user in users:
        if user[1] == req_form["login"]:
            if user[2] == req_form["password"]:
                session['user'] = req_form["login"]
                return "Sesja została utworzona <br> <a href='/'> Dalej </a> "
            else:
                return "Nie ten password <br> <a href='/'> Dalej </a>"
    return "Nie ma takiego użytkownika <br> <a href='/'> Dalej </a> "


@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user')
    else:
        redirect(url_for('index'))
    return "Wylogowano <br>  <a href='/'> Powrót </a>"


@app.route('/addbook', methods=['POST'])
def add_book():
    if 'user' in session:
        title = request.form['title']
        author = request.form['author']
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO books (title,author) VALUES (?,?)", (title, author))
        con.commit()
        con.close()
        return "The book has been added <br>" + index()
    else:
        return index()


@app.route('/users', methods=['GET'])
def show_users():
    if 'user' in session:
        admin_allowed = check_admin_privilage(session['user'])
        if admin_allowed == 1:
            users = get_users()
            return render_template('usersPage.html', users=users)
        else:
            return no_admin_privilage()
    else:
        return no_session()


@app.route('/addUser', methods=['POST'])
def add_user():
    if 'user' in session:
        admin_allowed = check_admin_privilage(session['user'])
        if admin_allowed == 1:
            username = request.form['login']
            password = request.form['password']
            admin = request.form.get('admin')
            if admin is None:
                is_admin = 0
            else:
                is_admin = 1
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, password, admin) VALUES (?,?,?)", (username, password, is_admin))
            con.commit()
            con.close()
            return "The User was added <br>" + show_users()
        else:
            return no_admin_privilage()
    else:
        return no_session()


@app.route('/user/<username>', methods=['GET'])
def show_user(username):
    if 'user' in session:
        admin_allowed = check_admin_privilage(session['user'])
        if admin_allowed == 1:
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            cur.execute("SELECT rowid,username,password,admin FROM users WHERE username like (?)", (username,))
            user = cur.fetchall()
            con.close()
            return render_template('userPage.html', users=user)
        else:
            return no_admin_privilage()
    else:
        return no_session()


def no_admin_privilage():
    return "No admin privilages <br>" + index()


def no_session():
    return "No Session <br>" + index()


def check_admin_privilage(name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    con.close()
    for user in users:
        if user[0] == name:
            if user[2] == 1:
                return 1
            else:
                return 0
    return False


def get_books():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from books")
    books = cur.fetchall()
    return books


def get_users():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select rowid, username, password, admin from users")
    users = cur.fetchall()
    con.close()
    return users


app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)
app.config.from_object(__name__)
app.debug = True
app.run()
