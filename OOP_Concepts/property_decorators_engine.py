class Engine:
    def __init__(self, initial_temp=0):
        self._temperature = initial_temp

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 0:
            raise ValueError("Temperature cannot be below 0°C")
        self._temperature = value

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        print(f"Car started. Engine temperature: {self.engine.temperature}")

