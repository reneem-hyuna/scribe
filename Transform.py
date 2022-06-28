from classes.Error import FieldIsMissing, FieldIsNotInPayload, RequiredFieldMissing, exception
from hashlib import md5
#from classes.Event import Event
import datetime
from pytz import timezone
import re

class Transform:

    def __init__(self, data, event):
           self.event = event
           self._data = dict(data)
           self._payload = dict(self.event.get_payload_definition())

    def get_data(self):
           return self._data

    def field_exist(self, field):
           return field in self._data

    def get_field_value(self, field):
        if self.field_exist(field):
            return self._data[field]
        return None
    
    def get_hash(self, value):
        return md5(value.encode('utf-8')).hexdigest()
    
    def add_hash_key(self, field):
        value = self.get_field_value(field)
        hash_value = self.get_hash(value) 
        self._payload["hash_key"] = hash_value
    
    def transform_event_metric(self):
        event = self.get_field_value("event_type")
        
    def transform_event_properties(self):
        for x,y in self.get_data().items():
            transform_field = str(x.replace(" ", "_").lower())
            #print(y)
            if transform_field in self._payload:
                self._payload[transform_field] = y
               
    
    @exception
    def execute(self):
        #self.check_required()
        #self.add_hash_key("session_id")
        #self.transform_event_metric()
        #self.transform_field_names()
        self.transform_event_properties()
        self.transform_date_fields()
        #self.transform_experiment_code()
    
    def transform_date_fields(self):
        date_fields = self.event.get_date_fields()
        for date_field in date_fields:
            self.transform_date_field(date_field)
    
    def transform_date_field(self,transform_date_field):
        #date_field = .date_field[0]
        #transform_date_field = Event.date_field[1]
        date_value = self.get_field_value(transform_date_field[0])
        str_datetime = datetime.datetime.strptime(date_value, transform_date_field[1])
        str_datetime_utc = str_datetime.replace(tzinfo=timezone('UTC'))
        self._payload[transform_date_field[0]] = str_datetime_utc.strftime('%Y-%m-%d %H:%M:%S')
       
 
    def get_payload(self):
        return self._payload
    
    def check_required(self):
        required = False
        for x in self.event.get_required():
            required = x in self._data and self._data[x]
        # required =  list(set(Event.required) & set(self._data))
        # if len(required) != len(Event.required):
        #     raise RequiredFieldMissing
        # return True 
        if not required:
            raise RequiredFieldMissing
    
   
    