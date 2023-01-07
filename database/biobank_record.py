import datetime


class BiobankRecord:
    def __init__(self, record: dict, parsing_time: datetime.datetime):
        self.record = record
        self.parsing_time = parsing_time

    @property
    def record(self):
        return self.record

    @record.setter
    def record(self, value):
        if value == {}:
            raise ValueError("idk")
        self._record = value
