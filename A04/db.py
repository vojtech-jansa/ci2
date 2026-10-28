import csv
import os
import sqlite3
import sys


class Database:
    def __init__(self, arguments):
        self.arguments = arguments
        self.connection = sqlite3.connect("db.sqlite")
        self.cursor = self.connection.cursor()

    def table_exists(self, table_name):
        self.cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table' AND name = ?
            """,
            (table_name,)
        )

        return self.cursor.fetchone() is not None

    def import_csv(self, filename):
        table_name = os.path.splitext(os.path.basename(filename))[0]

        if self.table_exists(table_name):
            return

        with open(filename, newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")

            columns = next(reader)

            column_definition = ", ".join(
                f'"{column}" TEXT'
                for column in columns
            )

            self.cursor.execute(
                f'CREATE TABLE "{table_name}" ({column_definition})'
            )

            placeholders = ", ".join(
                "?" for column in columns
            )

            self.cursor.executemany(
                f'INSERT INTO "{table_name}" VALUES ({placeholders})',
                reader
            )

        self.connection.commit()

    def import_files(self):
        for filename in self.arguments:
            self.import_csv(filename)

    def answer_question(self):
        self.cursor.execute(
            """
            SELECT country.Name
            FROM country
            JOIN countrylanguage
                ON country.Code = countrylanguage.CountryCode
            WHERE countrylanguage.Language = ?
            ORDER BY country.Name
            """,
            ("Spanish",)
        )

        countries = self.cursor.fetchall()

        print("Question: In what countries is used the Spanish language?")
        print("Answer:")

        for country in countries:
            print(country[0])

    def run(self):
        self.import_files()
        self.answer_question()
        self.connection.close()


if __name__ == "__main__":
    app = Database(sys.argv[1:])
    app.run()