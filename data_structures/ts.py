class TS:
    def __init__(self):
        self.content = {}

    def get_length(self):
        return len(self.content)

    def set(self, key, value):
        self.content[key] = value

    def get_value(self, key):
        return self.content.get(key)

    def get_items(self):
        return self.content.items()

    def get_keys(self):
        return self.content.keys()