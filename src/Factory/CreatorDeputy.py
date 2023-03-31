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
        self.deputy.sexe = self.datas[12 + self.index_modify]
        self.deputy.last_name = self.datas[13 + self.index_modify]
        self.__set_deputy_first_name()
        self.__set_deputy_birthdate()
        if  'Oui' in self.datas[16 + self.index_modify] :
            self.deputy.is_sorting = True
        self.__set_candidate_deputy_identity()
        return self.deputy
    
    def __set_deputy_first_name(self) : 
        if ('00:00:00' in self.datas[14 + self.index_modify + 1]) == False : 
            self.deputy.first_name = self.datas[14 + self.index_modify] +" "+ self.datas[14 + self.index_modify + 1]
            self.index_modify += 1
        else :     
            self.deputy.first_name = self.datas[14 + self.index_modify]
       
    
    def __set_deputy_birthdate(self) : 
        birthdate = self.datas[15 + self.index_modify]
        birthdate = birthdate.replace(' 00:00:00','')
        birthdate = birthdate.replace('-',',')
        birthdate = birthdate.replace(')','')
        birthdate_elements = birthdate.split(',')
        year = int(birthdate_elements[0])
        month = int(birthdate_elements[1])
        day = int(birthdate_elements[2])
        self.deputy.birthdate = datetime.datetime(year, month, day)
        
        
    def __set_candidate_deputy_identity(self) : 
        if self.is_candidate_two_first_name :
            self.deputy.candidate.last_name = self.datas[6]
            self.deputy.candidate.first_name = self.datas[7] +" "+self.datas[8]
        else :
            self.deputy.candidate.last_name = self.datas[6]
            self.deputy.candidate.first_name = self.datas[7]
    
    
    