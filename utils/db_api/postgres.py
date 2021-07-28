import psycopg2
import datetime






class DB:

    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", port=5432, database="telegram", user="postgres", password="111111")
        self.cur = self.conn.cursor()
        print("Database opened successfully")

    def insert(self, user_id, username, name, lastname):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname = lastname
        now = datetime.datetime.now()
        query = "INSERT INTO main_client(user_id, username, name, lastname, created_at) VALUES (1,'dw','dddd','dwd','12-11-2020 09:11');"
        self.cur.execute(query)
        self.conn.commit()

    def select_info(self, slug):
        self.slug = slug
        return self.cur.execute("SELECT * FROM main_currency WHERE slug = ?", (self.slug,)).fetchall()

    def select(self):
        return self.cur.execute("SELECT * FROM main_client").fetchall()
