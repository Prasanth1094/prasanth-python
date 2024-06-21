import os
import psycopg2
from contextlib import contextmanager
from psycopg2.extras import DictCursor


@contextmanager
def get_db_cursor():
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor(cursor_factory=DictCursor)
        yield cur
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            host=os.getenv('DB_HOST'),
            password=os.getenv('DB_PASSWORD')
        )
        print("Connected to the PostgreSQL database...")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn
