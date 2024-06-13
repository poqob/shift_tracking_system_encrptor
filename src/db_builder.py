import sqlite3
import configparser


class DbBuilder:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def create_database(self):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()

        # actions table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(15)
            )
        """
        )

        # actions table
        cursor.execute(
            f"""
             insert into actions (name) values ('default')
        """
        )

        # qrcode table
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                action INTEGER ,
                code VARCHAR(10),
                FOREIGN KEY (action) REFERENCES actions(id)

            )
        """
        )
        conn.commit()
        conn.close()