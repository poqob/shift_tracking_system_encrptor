from actions import Actions
import configparser
from typing import List
import sqlite3


class DbActionsService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def __init__(self, action: Actions = None):
        self.action = action

    def add(self, action: Actions):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO actions (name) VALUES ('{action.name}')")
        conn.commit()
        conn.close()

    def delete(self, id: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM actions WHERE id = {id}")
        conn.commit()
        conn.close()

    def update(self, action: Actions):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE actions SET name = '{action.name}' WHERE id = {action.id}"
        )
        conn.commit()
        conn.close()

    def get_by_id(self, id: int) -> Actions:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM actions WHERE id = {id}")
        row = cursor.fetchone()
        conn.close()
        return Actions().parse(row)

    def get_all(self) -> List[Actions]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actions")
        rows = cursor.fetchall()
        conn.close()
        return [Actions().parse(row) for row in rows]
