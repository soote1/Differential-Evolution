class Individual:

    def __init__(self):
        self.position = []

    def get_position(self):
        return self.position

    def set_position(self, p):
        self.position = p

    def set_position_in_dimension(self, p):
        self.position.append(p)
