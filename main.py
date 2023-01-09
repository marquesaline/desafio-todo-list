from src.app import app
from src.database import Database

if __name__ == '__main__':
    Database.create_table()
    app.run(debug=True)