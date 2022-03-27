from abc import abstractmethod
from io import BytesIO


class StorageRepository:

    @abstractmethod
    def upload(self, file: BytesIO, path: str) -> None:
        raise NotImplementedError

