import os

from biobank.biobank_record_repository import BiobankRecordRepository
from biobank.biobank_service import BiobankService
from database.database import Database
from parser.file_parser import FileParser

if __name__ == '__main__':
    db = Database("postgresql://localhost:5432/dim?user=dim&password=dim")
    biobankRepository = BiobankRecordRepository(db)
    biobankService = BiobankService(biobankRepository)
    file_parser = FileParser(os.path.dirname(__file__) + "/tests/dummy_files")
    biobankService.saveFilesContentIntoDBInJson(file_parser)
