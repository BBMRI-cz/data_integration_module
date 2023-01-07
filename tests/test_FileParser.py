import logging
import unittest

from parser.file_parser import FileParser

log = logging.getLogger(__name__)


class FileParserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._fileParser = FileParser()

    def test_ClassInit(self):
        self.assertIsInstance(self._fileParser, FileParser)

    def test_FoundXMLFiles(self):
        self.assertTrue(self._fileParser.foundValidFiles())
