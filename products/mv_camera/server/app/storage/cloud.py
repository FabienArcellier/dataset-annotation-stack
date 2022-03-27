import os
from abc import abstractmethod
from io import BytesIO
from urllib.parse import urlparse

import boto3


class CloudStorageRepository:

    def __init__(self):
        url = os.getenv('CLOUD_STORAGE', None)
        if url is None:
            raise OSError("CLOUD_STORAGE environment variable has to be setup : s3://xxxxxxxxxxxxx/{path}")

        endpoint = urlparse(url)
        if endpoint.scheme != "s3":
            raise NotImplementedError(f"support for {endpoint.scheme} is not implemented")

        self.bucket_name = endpoint.hostname
        self.object_prefix = _trim_s3_path(endpoint.path)

    @abstractmethod
    def upload(self, file: BytesIO, path: str) -> None:
        s3 = boto3.client('s3')
        s3.upload_fileobj(file, self.bucket_name, self.object_prefix + "/" + path)


def _trim_s3_path(path: str) -> str:
    """
    aws s3 interprets all first slash as root folder
    and double / as 2 nested folders.:
    """
    return path.lstrip('/').rstrip('/')

