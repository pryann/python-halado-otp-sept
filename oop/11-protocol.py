from typing import Protocol


class Database(Protocol):
    def connect(self): ...

    def close(self): ...

    def run_query(self): ...


class SQLDatabase(Database):
    def connect(self):
        print("connect sql")

    def close(self):
        print("close sql connection")

    def run_query(self):
        print("run sql query")


class NoSQLDatabase(Database):
    def connect(self):
        print("connect nosql")

    def close(self):
        print("close nosql connection")

    def run_query(self):
        print("run nosql query")


def connection(database: Database) -> None:
    database.connect()


connection(SQLDatabase())
connection(NoSQLDatabase())
