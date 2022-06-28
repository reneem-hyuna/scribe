from classes.Event import Event
class RT_Terminals_OTC_Event(Event):
    
    def get_required(self):
        return ["event_type"]
    
    def get_date_fields(self):
        return [("Posting_Date","%m/%d/%Y %H:%M:%S")]
    
    def get_date(self):
        return "date_code"
    
    def get_payload_definition(self):
        payload_definition = {
            'event_type':"RT_Terminals_ATM",
            'account_class':0,
            'bank':0,
            'account':'',
            'account_class':'',
            'teller_number':0,
            'transaction_class':'',
            'transaction_type':'',
            'branch_num':0,
            'posting_date':'0000-00-00',
            'date_code':'',
            'currency':'',
            'customer_present':'No',
            'transaction_status':0,
            'original_transaction_amount':0.00,
            'original_cash_amount':0.00,
            'original_cheque_amount':0.00,
            'time_received':'0000-00-00 00:00:00',
            'time_of_response':'0000-00-00 00:00:00',
            'receipt_account': 'xxx',
            'transaction_source':'ATM',
            'num_occurences': 1
            
            
        }
        return payload_definition