from pathlib import Path

from storage.stubs import URI, Html
from storage.choices import DataType
from storage.stubs import Identifier, SuccessMessage


class IRepository:
    def __init__(self, context: URI | Path, data_type: DataType):
        self.context = context
        self.data_type = data_type.value

    def prepare(self) -> SuccessMessage: ...

    def get_one(self, identifier: Identifier) -> Html | None: ...

    def get_many(self) -> list[Html]: ...

    def create(self, data: Html) -> Identifier: ...





