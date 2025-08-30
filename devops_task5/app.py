from flask import Flask, request, render_template_string
import sqlite3
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

# Get encryption key from environment variable
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")
fernet = Fernet(ENCRYPTION_KEY)

DB_PATH = "/data/passwords.db"

# Create DB if not exists
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    site TEXT,
                    username TEXT,
                    password TEXT
                )""")
    conn.commit()
    conn.close()

init_db()

HTML_PAGE = """
<h2>Local Password Manager</h2>
<form method="POST" action="/add">
    Site: <input type="text" name="site" required><br>
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <button type="submit">Save</button>
</form>
<hr>
<h3>Saved Passwords</h3>
<ul>
{% for row in passwords %}
<li>{{ row[1] }} - {{ row[2] }} - {{ row[3] }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    rows = [(r[0], r[1], r[2], fernet.decrypt(r[3].encode()).decode()) for r in c.fetchall()]
    conn.close()
    return render_template_string(HTML_PAGE, passwords=rows)

@app.route("/add", methods=["POST"])
def add():
    site = request.form["site"]
    username = request.form["username"]
    password = request.form["password"]

    encrypted_pw = fernet.encrypt(password.encode()).decode()

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
              (site, username, encrypted_pw))
    conn.commit()
    conn.close()

    return "Password saved! <a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

