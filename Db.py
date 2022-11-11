import sqlite3
from datetime import datetime


class Db:
    def __init__(self, result, message):
        self.connection = sqlite3.connect('council.db')
        self.cursor = self.connection.cursor()

        sql = """CREATE TABLE IF NOT EXISTS logs(id INTEGER AUTO_INCREMENT PRIMARY KEY, 
        result INTEGER, message TEXT, created_at TEXT)"""

        self.cursor.execute(sql)

        self.result = str(result)
        self.message = message
        self.dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def log(self):
        self.cursor.execute("INSERT INTO logs (result, message, created_at) VALUES (?,?,?)",
                            [self.result, self.message, self.dt])
        self.connection.commit()
