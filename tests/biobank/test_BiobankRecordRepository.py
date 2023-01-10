import datetime
import logging
import unittest

import pytest
from psycopg.errors import UniqueViolation
from testcontainers.postgres import PostgresContainer

from biobank.biobank_record_dto import BiobankRecordDTO
from biobank.biobank_record_repository import BiobankRecordRepository
from database.database import Database
from tests.util_for_tests import parseTestContainerUrlForPsycopg

biobankRecord = BiobankRecordDTO(
    identifier="test1",
    record={"a": "b"},
    bims_export_time=datetime.datetime.now()
)


class TestBiobankRecordRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = parseTestContainerUrlForPsycopg(cls._postgresContainer.get_connection_url())
        db = Database(url)
        cls._biobankRecordRepository = BiobankRecordRepository(db)

    @pytest.fixture(autouse=True)
    def runBeforeAndAfterEachTest(self):
        yield
        self._biobankRecordRepository.deleteAll()

    def test_insertOneRow(self):
        result = self._biobankRecordRepository.insert(biobankRecord)
        self.assertTrue(result)

    def test_insertSameDTOTwiceRaisesError(self):
        self._biobankRecordRepository.insert(biobankRecord)
        with self.assertLogs(logging.getLogger(), level='WARNING') as cm:
            self._biobankRecordRepository.insert(biobankRecord)
            self.assertTrue(cm.output)

    def test_getAllOnEmptyTable(self):
        self.assertEquals(self._biobankRecordRepository.getAll(), [])

    def test_getAllWithOneRow(self):
        self._biobankRecordRepository.insert(biobankRecord)
        self.assertEquals(len(self._biobankRecordRepository.getAll()), 1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()
