import datetime

from src.Models.DeputyModel import DeputyModel
from src.Factory.Creator import Creator

class CreatorDeputy(Creator):
    def __init__(self, is_candidate_two_first_name) :
        self.datas = []
        self.deputy = DeputyModel()
        self.is_candidate_two_first_name = is_candidate_two_first_name
        self.index_modify = 0
        
    def factory_method(self, deputy_data):
        self.datas = deputy_data
        if self.is_candidate_two_first_name :
            self.index_modify += 1
        self.deputy.sexe = self.datas[13 + self.index_modify]
        self.deputy.last_name = self.datas[14 + self.index_modify]
        self.__set_deputy_first_name()
        self.__set_deputy_birthdate()
        if  self.datas[17 + self.index_modify]  == 'Oui' :
            self.deputy.is_sorting = True
        return self.deputy
    
    
    def __set_deputy_first_name(self) : 
        if ('datetime' in self.datas[15 + self.index_modify + 1]) == False : 
            self.deputy.first_name = self.datas[15 + self.index_modify] +" "+ self.datas[15 + self.index_modify + 1]
            self.index_modify += 1
        else :     
            self.deputy.first_name = self.datas[15 + self.index_modify]
            
       
    
    #TODO factorize with birthdate from candidate
    def __set_deputy_birthdate(self) : 
        birthdate = self.datas[16 + self.index_modify]
        birthdate = birthdate.replace('datetime.datetime(', '')
        birthdate = birthdate.replace(', 0, 0)','')
        birthdate = birthdate.replace(')','')
        birthdate_elements = birthdate.split(',')
        year = int(birthdate_elements[0])
        month = int(birthdate_elements[1])
        day = int(birthdate_elements[2])
        self.deputy.birth_date = datetime.datetime(year, month, day)
    
    
    