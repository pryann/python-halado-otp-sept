from abc import ABC, abstractmethod

# https://jellis18.github.io/post/2022-01-11-abc-vs-protocol/


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run_query(self):
        pass


class SQLDatabase(Database):
    def connect(self):
        print("connect")

    def close(self):
        print("close connection")

    def run_query(self):
        print("run query")


class NoSQLDatabase(Database):
    def connect(self):
        print("connect")

    def close(self):
        print("close connection")

    def run_query(self):
        print("run query")


db = SQLDatabase()
nosql_db = NoSQLDatabase()
