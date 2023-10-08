import sqlite3

from flask import g

db_file = "database/database.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(db_file)
        g.db.row_factory = sqlite3.Row
    return g.db
