import datetime

class AlarmState:
    def __init__(self, time: datetime.time, enabled: bool):
        self.time = time
        self.enabled = enabled

    @classmethod
    def default(cls):
        return cls(datetime.time(8, 0, 0), False)
