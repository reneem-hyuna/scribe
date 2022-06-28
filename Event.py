from abc import ABC, abstractclassmethod

class Event(ABC):
    
    @abstractclassmethod
    def get_required(self):
        pass
    
    @abstractclassmethod
    def get_date_fields(self):
        pass
    
    @abstractclassmethod
    def get_date(self):
        pass
    
    @abstractclassmethod
    def get_payload_definition(self):
        pass
