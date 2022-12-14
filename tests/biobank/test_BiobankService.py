import logging
import os
import unittest

from testcontainers.postgres import PostgresContainer

from biobank.biobank_record_repository import BiobankRecordRepository
from biobank.biobank_service import BiobankService
from database.database import Database
from parser.file_parser import FileParser
from tests.util_for_tests import parseTestContainerUrlForPsycopg


class TestBiobankService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = parseTestContainerUrlForPsycopg(cls._postgresContainer.get_connection_url())
        db = Database(url)
        biobankRepository = BiobankRecordRepository(db)
        cls._biobankService = BiobankService(biobankRepository)

    def test_saveFilesIntoDBInJson(self):
        file_parser = FileParser(os.path.dirname(__file__) + "/../dummy_files")
        with self.assertLogs(logging.getLogger(), level='INFO') as cm:
            self._biobankService.saveFilesContentIntoDBInJson(file_parser)
            self.assertTrue(cm.output)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()