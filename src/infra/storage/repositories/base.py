from pathlib import Path

from infra.storage.stubs import SuccessMessage
from infra.stubs import Html, URI
from infra.storage.choices import DataType
from infra.storage.structs import Identifier


class IRepository:
    def __init__(self, context: URI | Path, data_type: DataType):
        self.context = context
        self.data_type = str(data_type.value)

    def prepare(self) -> SuccessMessage: ...

    def get_one(self, identifier: Identifier) -> Html | None: ...

    def get_many(self) -> list[Html]: ...

    def create(self, data: Html, page: str = None) -> Identifier: ...
