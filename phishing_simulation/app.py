from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

DATABASE = 'phishing_simulation.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_emails', methods=['POST'])
def send_emails():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    subject = "Important Security Update"
    sender_email = "your_email@gmail.com"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_username = 'no-reply@gmail.com'
    smtp_password = 'your_password'

    for user in users:
        receiver_email = user['email']

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        body = render_template('phishing_email.html', user=user)
        message.attach(MIMEText(body, "html"))

        try:
            # Connect to the server
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(smtp_username, smtp_password)
                # Send email
                server.sendmail(sender_email, receiver_email, message.as_string())
                print(f"Email sent to {receiver_email}")

        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")

    return redirect(url_for('index'))


@app.route('/phish/<user_id>')
def phish(user_id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET clicked = clicked + 1 WHERE id = ?', (user_id,))
    conn.execute('INSERT INTO interactions (user_id, action) VALUES (?, ?)', (user_id, 'clicked'))
    conn.commit()
    conn.close()
    return render_template('training.html', user_id=user_id)


@app.route('/submit/<user_id>', methods=['POST'])
def submit(user_id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET submitted = submitted + 1 WHERE id = ?', (user_id,))
    conn.execute('INSERT INTO interactions (user_id, action) VALUES (?, ?)', (user_id, 'submitted'))
    conn.commit()
    conn.close()
    return "Submission received!"


@app.route('/results')
def results():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    interactions = conn.execute('SELECT * FROM interactions').fetchall()
    conn.close()
    return render_template('results.html', users=users, interactions=interactions)


if __name__ == '__main__':
    app.run(debug=True)