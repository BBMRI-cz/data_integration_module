import logging
import os
import time
import unittest

import schedule
from testcontainers.postgres import PostgresContainer

from biobank.biobank_record_repository import BiobankRecordRepository
from biobank.biobank_service import BiobankService
from database.database import Database
from parser.file_parser import FileParser
from tests.util_for_tests import parseTestContainerUrlForPsycopg


class TestScheduler(unittest.TestCase):
    testingList = []

    def appendToList(self):
        self.testingList.append(1)

    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = parseTestContainerUrlForPsycopg(cls._postgresContainer.get_connection_url())
        db = Database(url)
        biobankRepository = BiobankRecordRepository(db)
        cls._biobankService = BiobankService(biobankRepository)

    def test_appendToListUntilNotEmpty(self):
        schedule.every().second.do(self.appendToList)
        while not self.testingList:
            schedule.run_pending()
            time.sleep(1)
        self.assertEquals(self.testingList, [1])

    def test_runSaveFileContentToDBOnce(self):
        file_parser = FileParser(os.path.dirname(__file__) + "/dummy_files")
        schedule.every().second.do(self._biobankService.saveFilesContentIntoDBInJson, file_parser=file_parser)
        schedule.run_all()
        self.assertTrue(self._biobankService.getAllRecords())


    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()