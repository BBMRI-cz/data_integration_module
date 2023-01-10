import os

from biobank.biobank_record_repository import BiobankRecordRepository
from biobank.biobank_service import BiobankService
from database.database import Database
from parser.file_parser import FileParser

if __name__ == '__main__':
    db = Database(os.getenv("DB_URL"))
    biobankRepository = BiobankRecordRepository(db)
    biobankService = BiobankService(biobankRepository)
    file_parser = FileParser(os.getenv("RECORDS_DIR"))
    biobankService.saveFilesContentIntoDBInJson(file_parser)
