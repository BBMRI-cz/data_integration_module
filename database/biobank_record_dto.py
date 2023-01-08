import datetime


class BiobankRecordDTO:
    def __init__(self, record: dict, bims_export_time: datetime.datetime):
        self.record = record
        self.bims_export_time = bims_export_time

    @property
    def record(self):
        return self.record

    @record.setter
    def record(self, value):
        if value == {}:
            raise ValueError("idk")
        self._record = value
