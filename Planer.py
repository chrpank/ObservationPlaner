from Objects import Jupiter
from Objects import Mars
from Objects import Mercury
from Objects import Moon
from Objects import Neptune
from Objects import Pluto
from Objects import Saturn
from Objects import Uranus
from Objects import Venus


class ObservationPlaner:
    """Plans all object observations"""

    def __init__(self):
        self.version = "1"
        self.moon = Moon()
        self.mercury = Mercury()
        self.venus = Venus()
        self.mars = Mars()
        self.jupiter = Jupiter()
        self.saturn = Saturn()
        self.neptune = Neptune()
        self.uranus = Uranus()
        self.pluto = Pluto()

    # def calulateObservations(self):
