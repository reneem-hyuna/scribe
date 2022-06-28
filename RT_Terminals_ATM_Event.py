from classes.Event import Event
class RT_Terminals_OTC_Event(Event):
    
    def get_required(self):
        return ["event_type"]
    
    def get_date_fields(self):
        return [("Load_Date","%m/%d/%Y %H:%M:%S")]
    
    def get_date(self):
        return "date_code"
    
    def get_payload_definition(self):
        payload_definition = {
             "Year": 2021,
    "event_type":"RT_Terminals_ATM",
    "Month": 10,
    "TXN_Date": "000-00-00 0:00:00",
    "TXN_Time": "03:44.0",
    "Load_Date": "00-00-00 0:00:00",
    "Date_Code": "20211001",
    "Bank_Prod": 50,
    "Local_Currency": "USD",
    "Merchant_ID": 0,
    "Terminal_ID": 0,
    "Device_ID": "",
    "Transaction_Type": "WITHDRAWAL - NO RECEIPT",
    "Account_Number": 0,
    "Encoded_Account": 0,
    "Transaction_Currency": "USD",
    "Total_Amount": 0,
    "Total_Amount_USD": 3200,
    "Recipient_Acccount": "",
    "Recipient_Bank_No": "",
    "Terminal_Country": "",
    "Merchant_Name": "",
    "Card_Indicator": "Our Bank's VISA Debit Card",
    "Type": "ATM"
  },     

        return payload_definition
