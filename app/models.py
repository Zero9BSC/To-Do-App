import MysQLdb
import os

def get_db_connection():
    return MySQLdb.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME')
    )
