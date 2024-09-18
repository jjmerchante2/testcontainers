import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                info TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_data(self, info):
        self.cursor.execute('''
            INSERT INTO data (info) VALUES (?)
        ''', (info,))
        self.connection.commit()

    def read_data(self):
        self.cursor.execute('SELECT * FROM data')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    db = DatabaseManager('example.db')
    db.insert_data('Sample data')
    data = db.read_data()
    print(data)
    db.close()
