from src.myProject.database.db import get_db_cursor


def upload_file(file):
    try:
        with get_db_cursor() as cur:                 
            cur.execute(
                "INSERT INTO pms.files (name, data) VALUES (%s, %s)",
                (file.filename, file.read()),
            )
            return "File has been uploaded successfully"
    except Exception as e:
        print(e)
        raise
   


def download_file(id):
    try:
        with get_db_cursor() as cur:
            cur.execute("SELECT * FROM pms.files WHERE id = %s", (id,))
            file_data = cur.fetchone()
    except Exception as e:
        print(e)
        raise
    return file_data
