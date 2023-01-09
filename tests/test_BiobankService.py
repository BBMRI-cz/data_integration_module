import unittest
from unittest import mock

from testcontainers.postgres import PostgresContainer

from biobank.biobank_service import BiobankService
from database.biobank_record_repository import BiobankRecordRepository
from database.database import Database


class TestBiobankService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = cls._postgresContainer.get_connection_url().split("+")[1].replace("psycopg2", "postgresql")
        Database.connectionUrl = url
        cls._biobankService = BiobankService()
        cls._biobankRepository = BiobankRecordRepository()

    def test_saveFilesIntoDBInJson(self):
        for cursor in self._biobankService.saveFilesIntoDBInJson():
            self.assertEquals(cursor.statusmessage, "INSERT 0 1")
        self.assertEquals(len(self._biobankService.getAllRecords()), 2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()