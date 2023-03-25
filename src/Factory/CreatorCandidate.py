import datetime

from src.Models.CandidateModel import CandidateModel
from src.Factory.Creator import Creator

#TODO rework this method and this test like CreatorDistrict 
class CreatorCandidate(Creator) : 
    def __init__(self, parties) -> None:
        self.is_candidate_first_name_simple = True
        self.datas = []
        self.can = CandidateModel()
        self.parties = parties
        
        
    def factory_method(self, candidate_data) :         
        self.datas = candidate_data
        self.can.last_name = self.datas[7]
        self.can.sexe =  self.datas[6]
        self.__set_candidate_first_name()
        self.__set_candidate_birth_date()
        self.__set_candidate_party()
        self.__set_candidate_jobs()
        if self.datas[12] == 'Oui' :
           self.can.is_sorting = True
        
        return self.can
    
    def __set_candidate_birth_date(self) : 
        birthdate = ''
        if  self.is_candidate_first_name_simple == False :
            birthdate = self.datas[10]
        else : 
            birthdate = self.datas[9]
        birthdate = birthdate.replace('datetime.datetime(', '')
        birthdate = birthdate.replace(', 0, 0)','')
        birthdate = birthdate.replace(')','')
        birthdate_elements = birthdate.split(',')
        year = int(birthdate_elements[0])
        month = int(birthdate_elements[1])
        day = int(birthdate_elements[2])
        self.can.birth_date = datetime.datetime(year, month, day)
    
    
    def __set_candidate_first_name(self) :  
        if str.isalpha(self.datas[9]) : 
            self.is_candidate_first_name_simple = False
            self.can.first_name = self.datas[8]+" "+self.datas[9]
        else :
            self.can.first_name = self.datas[8]
            
            
    def __set_candidate_party(self) : 
        party_shortname = ''
        if  self.is_candidate_first_name_simple :
           party_shortname = self.datas[10]
        else :
           party_shortname = self.datas[11]
        for party in self.parties : 
            if party.short_name == party_shortname : 
                self.can.party_id = party.id
                break
            
            
    def __set_candidate_jobs(self) : 
         if  self.is_candidate_first_name_simple :
            self.can.job = self.datas[11]
         else :
            self.can.job = self.datas[12]
        