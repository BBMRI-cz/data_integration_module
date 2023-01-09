import json

from psycopg.errors import UniqueViolation

from database.biobank_record_dto import BiobankRecordDTO
from database.database import Database


class BiobankRecordRepository:

    def __init__(self):
        self._db = Database()

    def getAll(self):
        return self._db.query("SELECT * FROM biobank_record")

    def insert(self, biobank_record_dto: BiobankRecordDTO):
        try:
            return self._db.execute(insert_record, (biobank_record_dto.id,
                                                    json.dumps(biobank_record_dto.record),
                                                    biobank_record_dto.bims_export_time))
        except UniqueViolation as e:
            raise e

    def deleteAll(self):
        self._db.execute(delete_all_rows)


insert_record = "INSERT INTO public.biobank_record VALUES (%s, %s, %s);"
delete_all_rows = 'DELETE FROM biobank_record'
