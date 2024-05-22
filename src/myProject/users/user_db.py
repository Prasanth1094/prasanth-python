from src.myProject.database.db import connect

def get_users():
    rows=None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pms.user ORDER BY id ASC")
        rows = cur.fetchall()  
    except Exception as e:
        print(e)
    finally:
        if conn:
           conn.close()
        return rows
def add_user():
    try:
      conn = connect()
      cur = conn.cursor()
      cur.execute('''INSERT INTO pms.user (id,name,email,age) VALUES (4,'Prasanth','prasanth@gmail.com',29)''')
      conn.commit()
    except Exception as e:
        print(e)
    finally:
        if conn:
           conn.close()