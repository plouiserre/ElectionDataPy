import datetime

from src.Models.CandidateDataModel import CandidateDataModel
from src.Factory.CreatorDepartment import CreatorDepartment
from src.Factory.CreatorDistrict import CreatorDistrict
from src.Factory.CreatorCandidate import CreatorCandidate
from src.Factory.CreatorDeputy import CreatorDeputy
from src.Factory.CreatorElection import CreatorElection
from src.Factory.CreatorCandidates import CreatorCandidates

class CreatorCandidateData() : 
    def __init__(self, parties) :
        self.candidate_data = CandidateDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        
        
    def factory_method(self, data):
        self.__get_datas_cleaned(data)
        
        self.__get_department_candidate_datas()    
        
        self.__get_district_candidate_datas()
        
        self.__get_candidate_datas()
        
        self.__get_deputy_datas()
               
        return self.candidate_data
    
        
    def __get_candidate_datas(self) : 
       can_creator = CreatorCandidate(self.parties)
       self.candidate_data.candidate = can_creator.factory_method(self.datas)
       self.is_candidate_first_name_simple = can_creator.is_candidate_first_name_simple
    
    
    def __get_deputy_datas(self) : 
        is_complexe_creator_first_name = not self.is_candidate_first_name_simple
        dep_creator = CreatorDeputy(is_complexe_creator_first_name)
        self.candidate_data.deputy = dep_creator.factory_method(self.datas)
        
         
    #This method cannot managed the separation of the datas between 
    #district name and candidate's sexe
    def __get_datas_cleaned(self, data) : 
        data = ' '.join(data.split())
        data = data.replace('\t',' ')
        data = data.replace('\n ',' ')
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')    
        to_delete = ''
        for i in range(0, len(data)):
            caracter = data[i]
            if i == len(data)-1 : 
                break
            elif caracter == '\'' and to_delete == '' and data[i+1] == ' ':
                to_delete += caracter
            elif to_delete !='' : 
                to_delete += caracter
                if data[i+1] == '\'' and to_delete != '':
                    data_cleaned = data_cleaned.replace(to_delete, '_')
                    to_delete = ''
            else : 
                continue
        self.datas = data.split('_') 
        
        
    def factory_method_first_round(self, data) : 
        self.datas = self.__get_datas_cleaned_first_round(data)
        self.__get_department_candidate_datas()
        self.__get_district_candidate_datas()
        self.__get_election_model()
        self.__get_candidates_model()
        
        return self.candidate_data
      
       
    def __get_department_candidate_datas(self) : 
        dep_creator = CreatorDepartment()
        self.candidate_data.department = dep_creator.factory_method(self.datas)
            
            
    def __get_district_candidate_datas(self) : 
        dis_creator = CreatorDistrict()
        self.candidate_data.district = dis_creator.factory_method(self.datas)
        self.candidate_data.district.department = self.candidate_data.department
        
        
    def __get_election_model(self) : 
        creator_election = CreatorElection()
        self.candidate_data.election = creator_election.factory_method(self.datas)
        
    
    def __get_candidates_model(self) : 
        creator_candidates = CreatorCandidates()
        self.candidate_data.candidates = creator_candidates.factory_method(self.datas)
        
        
    def __get_datas_cleaned_first_round(self, data) : 
        data = ' '.join(data.split())
        data = data.replace('\t',' ')
        data = data.replace('\n ',' ')
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')    
        to_delete = ''
        for i in range(0, len(data)):
            caracter = data[i]
            if i == len(data)-1 : 
                break
            elif caracter == '\'' and to_delete == '' and data[i+1] == ' ':
                to_delete += caracter
            elif to_delete !='' : 
                to_delete += caracter
                if data[i+1] == '\'' and to_delete != '':
                    data_cleaned = data_cleaned.replace(to_delete, '_')
                    to_delete = ''
            else : 
                continue
        return data.split('_') 