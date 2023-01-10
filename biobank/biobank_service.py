from psycopg import Cursor

from biobank.biobank_record_repository import BiobankRecordRepository
from parser.file_parser import FileParser
from util.logger import getCustomLogger

log = getCustomLogger(__name__)


class BiobankService:

    def __init__(self, biobank_repository: BiobankRecordRepository):
        self._biobankRecordRepository = biobank_repository

    def saveFilesContentIntoDBInJson(self, file_parser: FileParser):
        for record in file_parser.parseXMLFilesInDir():
            cursor = self._biobankRecordRepository.insert(record)
            log.debug(record.record)
            try:
                log.info("Record: {id} inserted with status: {status}".format(id=record.id, status=cursor.statusmessage))
            except AttributeError:
                log.info(
                    "Record: {id} not inserted".format(id=record.id))

    def getAllRecords(self):
        return self._biobankRecordRepository.getAll()
