from datetime import datetime
class transaction:
    def __init__(self,t_type,amount):
        self.type=t_type
        self.amount=amount
        self.date=datetime.now()
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type} | {self.amount}"