import datetime
import logging
import os
import unittest
from datetime import datetime

import pytest

from biobank.biobank_record_dto import BiobankRecordDTO
from parser.file_parser import FileParser
from util.logger import getCustomLogger

log = getCustomLogger(__name__)


class FileParserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._fileParser = None

    @pytest.fixture(autouse=True)
    def runBeforeAndAfterEachTest(self):
        dir_path = os.path.dirname(__file__) + "/dummy_files"
        self._fileParser = FileParser(dir_path=dir_path)
        # Execute test
        yield
        self._fileParser = None

    def test_ClassInit(self):
        self.assertIsInstance(self._fileParser, FileParser)

    def test_FoundFilesInDummyDataDir(self):
        self.assertTrue(self._fileParser.foundValidFiles())

    def test_FoundNoFilesInEmptyDir(self):
        emptyDirPath = os.path.dirname(__file__) + "/dummy_files/empty_dir"
        self._fileParser = FileParser(emptyDirPath)
        self.assertFalse(self._fileParser.foundValidFiles())

    def test_logOnParsingEmptyDir(self):
        emptyDirPath = os.path.dirname(__file__) + "/dummy_files/empty_dir"
        self._fileParser = FileParser(emptyDirPath)
        with self.assertLogs(logging.getLogger(), level='INFO') as cm:
            for _ in self._fileParser.parseXMLFilesInDir():
                pass
            self.assertIn('Found no valid files', cm.output[1])

    def test_ParseXMLFiles(self):
        for biobankRecord in self._fileParser.parseXMLFilesInDir():
            self.assertIsInstance(biobankRecord, BiobankRecordDTO)

    def test_FileCreationTimeStamp(self):
        for biobankRecord in self._fileParser.parseXMLFilesInDir():
            self.assertIsInstance(biobankRecord.bims_export_time, datetime)
