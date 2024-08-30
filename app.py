from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="",  # replace with your MySQL password
        database="crud_db"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('read.html', users=users)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Server-side validation
        if not name or len(name) < 3:
            flash('Name is required and must be at least 3 characters long')
            return redirect(url_for('create'))
        
        if not email or '@' not in email:
            flash('A valid email is required')
            return redirect(url_for('create'))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cursor.fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Server-side validation
        if not name or len(name) < 3:
            flash('Name is required and must be at least 3 characters long')
            return redirect(url_for('update', id=id))
        
        if not email or '@' not in email:
            flash('A valid email is required')
            return redirect(url_for('update', id=id))

        cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('update.html', user=user)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
