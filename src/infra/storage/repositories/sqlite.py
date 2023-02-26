import sqlite3
from typing import Generator


from infra.storage.stubs import SuccessMessage
from ...stubs import Html
from infra.storage.structs import Identifier

from .base import IRepository


class SqliteRepository(IRepository):
    def prepare(self):
        with self._database_context() as cursor:
            cursor.execute(
                f"""
                    CREATE TABLE IF NOT EXISTS {self.data_type} (
                        id VARCHAR PRIMARY KEY,
                        data TEXT NOT NULL, 
                        created_at DATETIME NOT NULL

                """
            )
        return SuccessMessage(f'Table {self.data_type} was created successfully!')

    def _database_context(self) -> Generator[sqlite3.Cursor, None, None]:
        connection = sqlite3.connect(self.context)

        cursor = connection.cursor()
        yield cursor
        cursor.close()

    def get_one(self, identifier: Identifier) -> Html: ...

    def get_many(self) -> list[Html]: ...

    def create(self, data: str) -> Identifier:  ...
