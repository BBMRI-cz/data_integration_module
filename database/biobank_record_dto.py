import datetime


class BiobankRecordDTO:
    def __init__(self, record: dict, bims_export_time: datetime.datetime):
        if record == {}:
            raise ValueError("Record is empty")
        self._record = record
        self.bims_export_time = bims_export_time

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, value):
        if value == {}:
            raise ValueError("Record is empty")
        self._record = value
