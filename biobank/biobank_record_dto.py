import datetime


class BiobankRecordDTO:
    def __init__(self, identifier: str, record: dict, bims_export_time: datetime.datetime):
        self._id = identifier
        if record == {}:
            raise ValueError("Record is empty")
        self._record = record
        self.bims_export_time = bims_export_time

    @property
    def record(self):
        return self._record

    @property
    def id(self):
        return self._id

    @record.setter
    def record(self, value):
        if value == {}:
            raise ValueError("Record is empty")
        self._record = value
