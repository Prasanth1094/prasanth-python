import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect("dbname='prasanth_db' user='postgres' host='localhost' password='prasanth'")
        print('Connected to the PostgreSQL database...')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn