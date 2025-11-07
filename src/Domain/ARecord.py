class ARecord:
    def __init__(self, id: int, paris_date: str, temperature: float, humidity: float, pressure: int):
        self.id = id
        self.paris_date = paris_date
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def __repr__(self):
        return (f"ARecord(id={self.id}, paris_date={self.paris_date}, "
                f"temperature={self.temperature}, humidity={self.humidity}, "
                f"pressure={self.pressure})")
