class Actions:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def parse(self, data):
        self.id = data["id"]
        self.name = data["name"]
        return self
