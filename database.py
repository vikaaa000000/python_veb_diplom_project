
import sqlite3

def add_user(username, email, password):
    
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    sql = "INSERT INTO user (username, email, password) VALUES(?, ?, ?)"
    cursor.execute(sql(username, email, password))
    conn.commit()
    conn.close()