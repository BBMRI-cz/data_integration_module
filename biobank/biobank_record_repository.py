import json

from psycopg.errors import UniqueViolation

from biobank.biobank_record_dto import BiobankRecordDTO
from database.database import Database
from util.logger import getCustomLogger

log = getCustomLogger(__name__)


class BiobankRecordRepository:

    def __init__(self, database: Database):
        self._db = database

    def getAll(self):
        return self._db.query("SELECT * FROM biobank_record")

    def insert(self, biobank_record_dto: BiobankRecordDTO):
        try:
            return self._db.execute(insert_record, (biobank_record_dto.id,
                                                    json.dumps(biobank_record_dto.record),
                                                    biobank_record_dto.bims_export_time))
        except UniqueViolation:
            log.warning("Record with ID: {id} is already present in the database".format(id=biobank_record_dto.id))

    def deleteAll(self):
        self._db.execute(delete_all_rows)


insert_record = "INSERT INTO public.biobank_record VALUES (%s, %s, %s);"
delete_all_rows = 'DELETE FROM biobank_record'
