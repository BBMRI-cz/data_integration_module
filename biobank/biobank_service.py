from psycopg import Cursor

from biobank.biobank_record_repository import BiobankRecordRepository
from parser.file_parser import FileParser
from util.logger import getCustomLogger

log = getCustomLogger(__name__)


class BiobankService:

    def __init__(self, biobank_repository: BiobankRecordRepository):
        self._biobankRecordRepository = biobank_repository

    def saveFilesContentIntoDBInJson(self, file_parser: FileParser) -> Cursor:
        for record in file_parser.parseXMLFilesInDir():
            yield self._biobankRecordRepository.insert(record)

    def getAllRecords(self):
        return self._biobankRecordRepository.getAll()
