

def add_user(username, emal, password):
    
    conn = sqlite3.connect('gallery.db')
    cursor = con.cursor()
    sql = "INSERT INTO user (username, email, password) VALUES(?, ?, ?)"
    cursor.execute(sql(username, email, password))
    conn.commit()
    conn.close()