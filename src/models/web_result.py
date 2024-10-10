

class WebResultVO:
    def __init__(self, status, data):
        self.status = status
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "data": self.data,
        }


class WebFailResultVO:
    def __init__(self, status, data):
        self.status = 00000
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "data": self.data,
        }
