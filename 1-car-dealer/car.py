from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.is_running = False

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
