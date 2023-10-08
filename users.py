from connection import get_db

def create_table():
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS users (
        "userId" integer primary key autoincrement,
        "username" Text,
        "password" Text
    ) ''')

def create_account(username, password):
    connection = get_db()
    sql = connection.cursor()
    result = sql.execute('SELECT * FROM users WHERE username = ?', [username])
    rows = result.fetchall()
    row_count = len(rows)
    if row_count > 0 :
        return "Can't create account, user already exists"
    else:
        sql.execute('''INSERT INTO users
        (username, password) VALUES
        (?, ?)''', [username, password])

        connection.commit()
        return "Account created, you can login now"

def check_account(username, password):
    connection = get_db()
    sql = connection.cursor()
    result = sql.execute('''SELECT * FROM users
                            WHERE username = ?''', [username])
    data = result.fetchone()
    if data:
        return data['userId']
    else:
        return False