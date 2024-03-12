import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOSTNAME = os.getenv("hostname")
DATABASE = os.getenv("database")
USERNAME = os.getenv("username")
PWD = os.getenv("pwd")
PORT_ID = os.getenv("port_id")

class Table():
    def __init__(self):
        super(Table, self).__init__()

    def create_info_table(self):
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS information_table(
            user_id BIGINT NOT NULL,
            message VARCHAR (100) NOT NULL,
            sent_time TIMESTAMP);
            """)

        conn.commit()
        cur.close()
        conn.close()

    def insert_into_info_table(self,user_id, message,time_sent):
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        insert_script = 'INSERT INTO information_table (user_id,message,sent_time) VALUES (%s,%s,%s)'
        cur.execute(insert_script, (user_id,message,time_sent))

        conn.commit()
        cur.close()
        conn.close()


    def create_user_table(self):
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS user_team_table(
            user_id BIGINT NOT NULL,
            team_name VARCHAR (50) NOT NULL);
            """)
        
        conn.commit()
        cur.close()
        conn.close()
    
    def insert_table(self,user_id, team):

        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )
        cur = conn.cursor()
        insert_script = 'INSERT INTO user_team_table (user_id,team_name) VALUES (%s,%s)'
        insert_value = (user_id,team)
        cur.execute(insert_script, insert_value)
        conn.commit()
        cur.close()
        conn.close()

    # Get all the teams that certain user subscribed
    def select_from_table(self,user_id):
        final_teams = []
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        select_script = 'SELECT team_name FROM user_team_table WHERE user_id = %s'
        select_value = user_id
        cur.execute(select_script, (select_value,))
        teams = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for i in range(len(teams)):
            team = teams[i][0]
            final_teams.append(team)
        return final_teams

    # Get all the users
    def select_distinct_user(self):
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        cur.execute('SELECT DISTINCT user_id FROM user_team_table')
        users = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        
        return users

    def delete_team(self,user_id,team):
        
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )

        cur = conn.cursor()

        delete_script = """
                        DELETE FROM user_team_table
                        WHERE user_id = %s AND team_name = %s;
                        """
        cur.execute(delete_script, (user_id, team))

        conn.commit()
        cur.close()
        conn.close()

    def delete_all(self,user_id):
        conn = psycopg2.connect(
            host = HOSTNAME,
            dbname = DATABASE,
            user = USERNAME,
            password = PWD,
            port = PORT_ID
        )
        cur = conn.cursor()

        delete_script = 'DELETE FROM user_team_table WHERE user_id = %s'
        cur.execute(delete_script, (user_id,))

        conn.commit()
        cur.close()
        conn.close()
