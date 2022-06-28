from classes.Event import Event
from abc import ABC, abstractclassmethod
from classes.RT_Terminals_OTC_Event import RT_Terminals_OTC_Event
class EventFactory(ABC):
    
    @abstractclassmethod
    def create_event(self):
        pass
    
class RT_Terminals_OTC_Factory(EventFactory):
    def create_event(self):
        return RT_Terminals_OTC_Event()
    
class EventCreator:
    def get_event(self, event):
        event_type = event["event_type"]
        if event_type == "RT_Terminals_OTC":
            factory = RT_Terminals_OTC_Factory()
        event = factory.create_event()
        return event
        