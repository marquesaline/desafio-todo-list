import sqlite3

class Database:

    def connect_db():
        connection = sqlite3.connect('database.db')

        return connection

    def create_table():
        db = Database.connect_db()
        cursor = db.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')

        