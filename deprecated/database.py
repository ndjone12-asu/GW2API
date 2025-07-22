import sqlite3
import os

class DB:
    def __init__(self, path):
        self.path = path
        db_created = False if os.path.isfile(self.path) else True
        self.connection = sqlite3.connect(self.path)

        if db_created:
            cursor = self.connection.cursor()
            cursor.execute('CREATE TABLE account(name PRIMARY KEY, access_token)')
            cursor.close()

    def log_DB(self, accountInfo):
        cursor = self.connection.cursor()
        cursor.execute('INSERT OR REPLACE INTO account(name, access_token) VALUES (?,?)', (accountInfo['name'], accountInfo['API_access_token']))
        cursor.close()
        self.connection.commit()
        if cursor.rowcount > 0:
            pass
        else:
           print(f'Insert failed.')

    def get_access_token(self, name):
        cursor = self.connection.cursor()
        cursor.execute('SELECT access_token FROM account WHERE name = ?', (name))
        api_token = cursor.fetchone()
        return api_token