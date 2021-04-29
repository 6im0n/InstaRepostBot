import psycopg2
from config import *


def create_tables():

    #""" create tables in the PostgreSQL database"""
    commands = (

        """
        CREATE TABLE photos_instagram (
                id VARCHAR(20) ,
                path VARCHAR(50),
                status VARCHAR(15),
                owner VARCHAR(50)
        )
        """)
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
			database=databaseName, user=db_user, password=passwordDataBase, host='127.0.0.1', port= '5432'
		)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
