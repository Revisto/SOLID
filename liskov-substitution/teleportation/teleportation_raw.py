from abc import ABC, abstractmethod

class TransporationDevice(ABC):
        @abstractmethod
        def start_engine(self):
            pass

class Car(TransporationDevice):
        def start_engine(self):
           print("Starting Engine...")

class Bike(TransporationDevice):
        def start_engine(self):
           print("Starting Engine...")

class Cycle(TransporationDevice):
        def start_engine(self):
          # Bicyles don't have engines
          raise NotImplementedError()