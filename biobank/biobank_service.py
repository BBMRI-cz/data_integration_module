from psycopg import Cursor

from database.biobank_record_repository import BiobankRecordRepository
from parser.file_parser import FileParser
from util.logger import CustomLogger

log = CustomLogger(__name__)


class BiobankService:

    def __init__(self):
        self._biobankRecordRepository = BiobankRecordRepository()
        self._fileParser = FileParser("/home/tomasik/Projects/Data-Integration-Module/tests/dummy_files")

    def saveFilesIntoDBInJson(self) -> Cursor:
        for record in self._fileParser.parseXMLFilesInDir():
            yield self._biobankRecordRepository.insert(record)

    def getAllRecords(self):
        return self._biobankRecordRepository.getAll()
