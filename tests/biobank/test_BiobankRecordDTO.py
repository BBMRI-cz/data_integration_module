import datetime
import unittest

from biobank.biobank_record_dto import BiobankRecordDTO


class TestBiobankRecord(unittest.TestCase):
    def test_ErrorOnEmptyBiobankRecordInit(self):
        self.assertRaises(TypeError, lambda: BiobankRecordDTO())
        self.assertRaises(ValueError, lambda: BiobankRecordDTO("empty", {}, datetime.datetime.now()))

    def test_CorrectBiobankRecordInit(self):
        self.assertIsInstance(BiobankRecordDTO("test1", {"a": "b"}, datetime.datetime.now()), BiobankRecordDTO)
