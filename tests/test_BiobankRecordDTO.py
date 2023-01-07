import datetime
import unittest

from database.biobank_record import BiobankRecord


class TestBiobankRecord(unittest.TestCase):
    def test_ErrorOnEmptyBiobankRecordInit(self):
        self.assertRaises(TypeError, lambda: BiobankRecord())
        self.assertRaises(ValueError, lambda: BiobankRecord({}, datetime.datetime.now()))

    def test_CorrectBiobankRecordInit(self):
        self.assertIsInstance(BiobankRecord({"a": "b"}, datetime.datetime.now()), BiobankRecord)
