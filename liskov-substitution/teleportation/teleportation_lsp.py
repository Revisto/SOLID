from abc import ABC, abstractmethod

class TransporationDevice(ABC):
    @abstractmethod
    def start(self):
        """Steps to start the vehicle"""

class TransporationDeviceWithoutEngine(ABC):
    pass

class TransporationDeviceWithEngine(ABC):        
    @abstractmethod
    def start_engine(self):
        """Process to start the engine"""

class Car(TransporationDeviceWithEngine):

        def start(self):
            # First start engine
            self.start_engine()
            # Do other steps here

        def start_engine(self):
           print("Starting Engine...")

class Bike(TransporationDeviceWithEngine):
        def start(self):
            # First start the engine
            self.start_engine()
            # Do other steps here

        def start_engine(self):
           print("Starting Engine...")


class Cycle(TransporationDeviceWithoutEngine):
        def start(self):
            print("Hit pedals....")