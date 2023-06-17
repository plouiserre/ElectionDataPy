import copy

from src.Models.ElectionDataModel import ElectionDataModel
from src.Factory.CreatorDepartment import CreatorDepartment
from src.Factory.CreatorDistrict import CreatorDistrict
from src.Factory.CreatorResult import CreatorResult
from src.Factory.CreatorCandidates import CreatorCandidates

class CreatorElectionData() : 
    def __init__(self, parties) :
        self.election_data = ElectionDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        self.last_election_data_created = ElectionDataModel()
        self.is_new_election_data_model_created = False
        
        
    def _get_department_election_datas(self) : 
        dep_creator = CreatorDepartment()
        self.election_data.department = dep_creator.factory_method(self.datas)
            
            
    def _get_district_election_datas(self) : 
        dis_creator = CreatorDistrict()
        self.election_data.district = dis_creator.factory_method(self.datas)
        self.election_data.district.department = self.election_data.department
        
        
    def _get_result_model(self) : 
        pass
        
    #TODO delete round_number
    def _get_candidates_model(self, round_number) : 
        creator_candidates = CreatorCandidates()
        self.election_data.candidates = creator_candidates.factory_method(self.datas)
        
        
    def _get_datas_cleaned_rounds(self, data) : 
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