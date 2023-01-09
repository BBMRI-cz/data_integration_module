from psycopg import Cursor

from biobank.biobank_record_repository import BiobankRecordRepository
from parser.file_parser import FileParser
from util.logger import CustomLogger

log = CustomLogger(__name__)


class BiobankService:
    dirPath = None

    def __init__(self):
        self._biobankRecordRepository = BiobankRecordRepository()
        self._fileParser = FileParser(dir_path=self.dirPath)

    def saveFilesIntoDBInJson(self) -> Cursor:
        self.__validateDirPath()
        for record in self._fileParser.parseXMLFilesInDir():
            yield self._biobankRecordRepository.insert(record)

    def getAllRecords(self):
        return self._biobankRecordRepository.getAll()

    def __validateDirPath(self):
        if self.dirPath is None:
            log.critical("Directory path for biobank records is not set!")
            raise ValueError
