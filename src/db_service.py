import sqlite3
import configparser


class DbService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def add(self, action: int, code: str):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO  {} (action, code)
            VALUES (?, ?)
            """.format(
                self.name
            ),
            (action, code),
        )

        conn.commit()
        conn.close()

    def delete(self, code: str):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM {self.name} WHERE code = {code}
        """.format(
                self.name, code
            )
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM {n}
        """.format(
                n=self.name
            )
        )
        result = cursor.fetchall()
        conn.close()
        return result

    def get_by_code(self, code: str):
        conn = sqlite3.connect(self.db_address)
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM {table_name} WHERE code = ?
            """.format(
                    table_name=self.name
                ),
                (code,),
            )
            result = cursor.fetchone()
            conn.close()
        except:
            result = None
            return Exception("Error in db_service get_by_code() function")
        return result

    def get_by_action(self, action: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM {table_name} WHERE action = ?
        """.format(
                table_name=self.name
            ),
            (action,),
        )
        result = cursor.fetchall()
        conn.close()
        return result
