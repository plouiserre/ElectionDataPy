import datetime

class CreatorPerson : 
    def __init__(self) :
        pass
        
    def determined_birthdate(self, birthdate_data) : 
        birthdate = birthdate_data
        birthdate = birthdate.replace(' 00:00:00','')
        birthdate = birthdate.replace('-',',')
        birthdate = birthdate.replace(')','')
        birthdate_elements = birthdate.split(',')
        year = int(birthdate_elements[0])
        month = int(birthdate_elements[1])
        day = int(birthdate_elements[2])
        return datetime.datetime(year, month, day)
    
    def factory_method(self) : 
        pass 
        
    