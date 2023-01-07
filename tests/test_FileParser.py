import logging
import unittest

from database.biobank_record import BiobankRecord
from parser.file_parser import FileParser

log = logging.getLogger(__name__)


class FileParserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._fileParser = FileParser()

    def test_ClassInit(self):
        self.assertIsInstance(self._fileParser, FileParser)

    def test_FoundFiles(self):
        self.assertTrue(self._fileParser.foundValidFiles())

    def test_ParseXMLFiles(self):
        for biobankRecord in self._fileParser.parseXMLFilesInDir():
            self.assertIsInstance(biobankRecord, BiobankRecord)
