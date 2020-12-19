import psycopg2
from os import getenv
from datetime import datetime
import json


def connect():
    conn = None
    try:
        HOST = getenv('POSTGRES_HOST')
        PORT = getenv('POSTGRES_PORT')
        USER = getenv('POSTGRES_USER')
        PASS = getenv('POSTGRES_PASS')
        conn = psycopg2.connect(user=USER, password=PASS, host=HOST, port=PORT, database="hedvig")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        print(error)


def insert_report(report_dict: dict) -> str:
    userid = getenv('USERID')
    reponame = getenv('PROJECT')
    commit = getenv('COMMITID')

    query = """INSERT INTO SCANNER (user_id, project_name, commit_id ,report, timestamp ) VALUES ( '{0}','{1}','{2}',{3},{4} ) 
            ON CONFLICT (user_id,project_name) DO UPDATE SET commit_id = '{2}', report= {3} RETURNING commit_id ;""".format(
        userid, reponame, commit, "'" + json.dumps(report_dict) + "'", "TIMESTAMP '" + str(datetime.now()) + "'")
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        commit = cur.fetchone()[0]
        print('{} processed'.format(commit))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return commit
