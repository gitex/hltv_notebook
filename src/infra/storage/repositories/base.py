from pathlib import Path
from typing import TypeVar

from infra.storage.stubs import SuccessMessage
from infra.stubs import URI
from infra.storage.choices import DataType
from infra.storage.structs import Identifier


T = TypeVar('T')


class IRepository:
    def __init__(self, context: URI | Path, data_type: DataType):
        """ Initializes the repository with a given context and data type.

        Args:
            context: A string or Path object that represents the repository context, such as a URI or filesystem path.
            data_type: The type of data stored in the repository.
        """

        self.context = context
        self.data_type = str(data_type.value)

    def prepare(self) -> SuccessMessage:
        """ Prepares the repository for use, performing any necessary setup or initialization.

        Returns:
            A success message indicating that the repository is ready for use.
        """
        ...

    def get_one(self, identifier: Identifier) -> T | None:
        """ Retrieves a single record from the repository, specified by a given identifier.

        Returns object if successful or None if the record is not found.
        """
        ...

    def get_many(self) -> list[T]:
        """ Retrieves multiple records from the repository.

        Returns a list of objects.
        """
        ...

    def create(self, data: T, page: str = None) -> Identifier:
        """ Creates a new record in the repository using the provided data.

        Returns an identifier that can be used to retrieve the record later.
        """
        ...
