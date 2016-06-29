from vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self):
        super().__init__()
        self.carry_limit = 0
        self.current_carriage_weight = None

    def has_carriage(self):
        return self.current_carriage_weight is not None

    def detach_carriage(self):
        self.current_carriage_weight = None

    def attach_carriage(self, weight):
        if weight <= self.carry_limit:
            self.current_carriage_weight = weight
        return self.has_carriage()
