from datetime import datetime
from .jsons import *



class Deconstruct:
    def __init__(self,data):
        self.data=data
     
        
    def consign_address(self):
        
        consign=dict()
        
        for i in consign_add_key:
            consign.update({i:self.data[i]})
   
        consign.update({"type":"consign"})
        consign.update({'woso_no':self.data['woso_no']})
  
        return consign
 
    def buyer_addr(self):
        buyer=dict()
        
        
        for i in buyer_keys:
            buyer.update({i:self.data[i]})
   
        buyer.update({"type":"consign"})
        buyer.update({'woso_no':self.data['woso_no']})
  
        return buyer
    
    def marketing(self):
        mkt=dict()
       
        
        for i in mkt_keys:
            mkt.update({i:self.data[i]})
        
        
        format_data = "%y/%m/%d"
        for date in Dates:
            Date=mkt[date]
            mkt[date]=str(datetime.strptime(Date,format_data).date())
        
        return mkt
    
        
    
    def item_deconstruct(self):
        items=list()
        items=self.data["items"]
        
        return items
        
        