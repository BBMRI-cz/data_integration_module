import datetime
import unittest

import pytest
from psycopg.errors import UniqueViolation
from testcontainers.postgres import PostgresContainer

from biobank.biobank_record_dto import BiobankRecordDTO
from biobank.biobank_record_repository import BiobankRecordRepository
from database.database import Database

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
        url = cls._postgresContainer.get_connection_url().split("+")[1].replace("psycopg2", "postgresql")
        Database.connectionUrl = url
        cls._biobankRecordRepository = BiobankRecordRepository()

    @pytest.fixture(autouse=True)
    def runBeforeAndAfterEachTest(self):
        yield
        self._biobankRecordRepository.deleteAll()

    def test_insertOneRow(self):
        result = self._biobankRecordRepository.insert(biobankRecord)
        self.assertTrue(result)

    def test_insertSameDTOTwiceRaisesError(self):
        self._biobankRecordRepository.insert(biobankRecord)
        self.assertRaises(UniqueViolation, lambda: self._biobankRecordRepository.insert(biobankRecord))

    def test_getAllOnEmptyTable(self):
        self.assertEquals(self._biobankRecordRepository.getAll(), [])

    def test_getAllWithOneRow(self):
        self._biobankRecordRepository.insert(biobankRecord)
        self.assertEquals(len(self._biobankRecordRepository.getAll()), 1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._postgresContainer.stop()
