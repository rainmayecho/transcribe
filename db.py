import sqlite3 as lite
import pickle

class DataManager(object):
    def __init__(self, name):
        self.conn = lite.connect(name)
        self._create_table()

    def _create_table(self):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS spectrograph(
                        name TEXT,
                        rate INTEGER,
                        chunk INTEGER,
                        spectrum BLOB)
                        ''')
    def _resume(self):
        pass
    
    def write_data(self, data):
        with self.conn as conn:
            cur = conn.cursor()
            s = '?,'*(len(data) - 1)
            cur.execute('INSERT INTO spectrograph VALUES (%s?)' %(s), data)

    def close(self):
        pass

    def read_data(self, name):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute('''SELECT * from spectrograph
                        WHERE name = ?''', [name])
            return cur.fetchone()
