import copy

from src.Factory.CreatorCandidate import CreatorCandidate
from src.Factory.CreatorDeputy import CreatorDeputy
from src.Factory.CreatorElectionData import CreatorElectionData
from src.Models.ElectionDataModel import ElectionDataModel

class CreatorElectionDataCandidatesList(CreatorElectionData) : 
    def __init__(self, parties) :
        self.election_data = ElectionDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        self.last_election_data_created = ElectionDataModel()
        self.is_new_election_data_model_created = False
    
    def factory_method(self, data):
        self.is_new_election_data_model_created = False
        
        self.__get_datas_cleaned(data)
        
        super()._get_department_election_datas()    
        
        super()._get_district_election_datas()
        
        self.__get_is_new_election_data_model_created()
        
        self.__copy_candidates_deputies_data_from_last_model()
        
        self.__get_candidates_datas()
        
        self.__get_deputy_datas()
        
        self.last_election_data_created = copy.deepcopy(self.election_data)
       
        return self.election_data
    
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
        
        
    def __get_is_new_election_data_model_created(self) : 
        if self.election_data.department.name != self.last_election_data_created.department.name or self.election_data.department.number != self.last_election_data_created.department.number :
            self.is_new_election_data_model_created = True
        elif self.election_data.district.name != self.last_election_data_created.district.name or  self.election_data.district.number != self.last_election_data_created.district.number:
                self.is_new_election_data_model_created = True
                
                
    def __copy_candidates_deputies_data_from_last_model(self) : 
        self.election_data.candidates = self.last_election_data_created.candidates
        self.election_data.deputies = self.last_election_data_created.deputies
        
        
    def __get_candidates_datas(self) : 
       can_creator = CreatorCandidate(self.parties)
       candidate = can_creator.factory_method(self.datas)
       if self.is_new_election_data_model_created == True :
            self.election_data.candidates = [candidate]
       else :
            self.election_data.candidates.append(candidate)
       self.is_candidate_first_name_simple = can_creator.is_candidate_first_name_simple
    
    
    def __get_deputy_datas(self) : 
        is_complexe_creator_first_name = not self.is_candidate_first_name_simple
        dep_creator = CreatorDeputy(is_complexe_creator_first_name)
        deputy = dep_creator.factory_method(self.datas)
        if self.is_new_election_data_model_created == True :
            self.election_data.deputies = [deputy]
        else :
            self.election_data.deputies.append(deputy)
            