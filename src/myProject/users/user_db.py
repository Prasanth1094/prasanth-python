
from src.myProject.database.db import get_db_cursor
import pandas as pd
import matplotlib.pyplot as plt

def get_users():
    rows=None
    try:
        with get_db_cursor() as cur:
            cur.execute("SELECT * FROM pms.user ORDER BY id ASC")
            rows = cur.fetchall()  
    except Exception as e:
        print(e)    
    return rows

def get_user_by_id(id):
    row=[]
    try:
        with get_db_cursor() as cur:
            cur.execute("SELECT * FROM pms.user WHERE id = %s ORDER BY id ASC",(id,))
            row=cur.fetchone()  
    except Exception as e:
        print(e)   
    return row

def add_user(result):
    try:
      with get_db_cursor() as cur:
        cur.execute( '''INSERT INTO pms.user (name, email, age) VALUES (%s, %s, %s)''',
            (result.json['name'], result.json['email'], result.json['age']))
    except Exception as e:
        print(e)
        raise  
    
def update_user(id,result):
    try:
      with get_db_cursor() as cur:
        cur.execute('''UPDATE pms.user SET name=%s, email=%s, age=%s WHERE id=%s''',(result.json['name'], result.json['email'], result.json['age'],id))
    except Exception as e:
        print(e)
        raise   

def delete_user(id):
    try:
      with get_db_cursor() as cur:
        cur.execute( '''DELETE FROM pms.user WHERE id=%s''',(id,))
    except Exception as e:
        print(e)
        raise   
def get_users_reports():
    data=get_users()
    df = pd.DataFrame(data)
    report = df.describe()
    return report.to_csv('report.csv')
    