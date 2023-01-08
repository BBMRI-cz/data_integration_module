import datetime
import logging
import os
import unittest
from datetime import datetime

from database.biobank_record_dto import BiobankRecordDTO
from parser.file_parser import FileParser

log = logging.getLogger(__name__)


class FileParserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        dir_path = os.path.dirname(__file__) + "/dummy_files"
        cls._fileParser = FileParser(dir_path)

    def test_ClassInit(self):
        self.assertIsInstance(self._fileParser, FileParser)

    def test_FoundFiles(self):
        self.assertTrue(self._fileParser.foundValidFiles())

    def test_ParseXMLFiles(self):
        for biobankRecord in self._fileParser.parseXMLFilesInDir():
            self.assertIsInstance(biobankRecord, BiobankRecordDTO)

    def test_FileCreationTimeStamp(self):
        for biobankRecord in self._fileParser.parseXMLFilesInDir():
            self.assertIsInstance(biobankRecord.bims_export_time, datetime)
