import unittest

from server.app.storage.cloud import CloudStorageRepository, _trim_s3_path


class TestCloudStorageRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_trim_s3_path_should_remove_first_slash(self):
        # Arrange
        # Acts
        result = _trim_s3_path('/datasets/dataset=hello')
        # Assert
        self.assertEqual('datasets/dataset=hello', result)

    def test_trim_s3_path_should_remove_last_slash(self):
        # Arrange
        # Acts
        result = _trim_s3_path('datasets/dataset=hello/')
        # Assert
        self.assertEqual('datasets/dataset=hello', result)


if __name__ == '__main__':
    unittest.main()
