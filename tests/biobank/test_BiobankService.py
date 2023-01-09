import os
import unittest

from testcontainers.postgres import PostgresContainer

from biobank.biobank_record_repository import BiobankRecordRepository
from biobank.biobank_service import BiobankService
from database.database import Database
from parser.file_parser import FileParser


class TestBiobankService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = cls._postgresContainer.get_connection_url().split("+")[1].replace("psycopg2", "postgresql")
        Database.connectionUrl = url
        biobankRepository = BiobankRecordRepository(Database())
        cls._biobankService = BiobankService(biobankRepository)

    def test_saveFilesIntoDBInJson(self):
        file_parser = FileParser(os.path.dirname(__file__) + "/../dummy_files")
        for cursor in self._biobankService.saveFilesContentIntoDBInJson(file_parser):
            self.assertEquals(cursor.statusmessage, "INSERT 0 1")
        self.assertEquals(len(self._biobankService.getAllRecords()), 2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()
