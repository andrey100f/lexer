class FIP:
    def __init__(self):
        self.content = []

    def add(self, key, value):
        self.content.append((key, value))

    def get_items(self):
        return self.content
