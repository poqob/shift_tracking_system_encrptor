class Actions:
    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def parse(self, data: dict):
        self.id = data["id"]
        self.name = data["name"]
        return self

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
