from src.Factory.CreatorCandidatesSecondRound import CreatorCandidatesSecondRound
from src.Factory.CreatorElectionData import CreatorElectionData
from src.Factory.CreatorResultSecondRound import CreatorResultSecondRound
from src.Models.ElectionDataModel import ElectionDataModel

#TODO factorize the constructor
class CreatorElectionDataSecondRound(CreatorElectionData) : 
    def __init__(self, parties, last_election_data_created) :
        self.election_data = ElectionDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        self.last_election_data_created = last_election_data_created
        self.is_new_election_data_model_created = False
        self.last_element_created = ElectionDataModel()
        self.all_last_elements_created = {}
        
        
    def factory_method(self, data) :
        self.datas = self._get_datas_cleaned_rounds(data)
        self.__delete_city_datas()
        self._get_department_election_datas()
        self._get_district_election_datas()
        self.__validate_or_clear_out_last_election_data_created()
        self._get_result_model()
        self._get_candidates_model()
        self.__get_last_element_created()
        
        return self.election_data
    
    
    #TODO update UT because last_election_data_created cannot be None
    #TODO study if this method is useful or not if it is not kill it and update code
    def __validate_or_clear_out_last_election_data_created(self) : 
        if len(self.last_election_data_created) > 0 :
            index = len(self.last_election_data_created) - 1
            is_same_department = False
            is_same_district = False
            if self.last_election_data_created[index].department.name == self.election_data.department.name and self.last_election_data_created[0].department.number == self.election_data.department.number :
                is_same_department = True
            if self.last_election_data_created[index].district.name == self.election_data.district.name and self.last_election_data_created[0].district.number == self.election_data.district.number :
                is_same_district = True
            if is_same_department == False or is_same_district == False :
                self.last_election_data_created = []
    
    
    def _get_result_model(self) : 
        creator_result = CreatorResultSecondRound(self.last_election_data_created)
        self.election_data.result = creator_result.factory_method(self.datas)
        self.all_last_elements_created["result"] = creator_result.last_element_created
    
    
    def _get_candidates_model(self) : 
        creator_candidates = CreatorCandidatesSecondRound(self.last_election_data_created)
        self.election_data.candidates = creator_candidates.factory_method(self.datas)
        self.all_last_elements_created["first_candidate"] = creator_candidates.last_elements_created[0]
        self.all_last_elements_created["second_candidate"] = creator_candidates.last_elements_created[1]
    
    
    def __delete_city_datas(self) : 
        del self.datas[4]
        del self.datas[4]
        
        
    def __get_last_element_created(self) : 
        self.last_element_created.department = self.election_data.department
        self.last_element_created.district = self.election_data.district
        self.last_element_created.result = self.all_last_elements_created["result"]
        self.last_element_created.candidates.append(self.all_last_elements_created["first_candidate"])
        self.last_element_created.candidates.append(self.all_last_elements_created["second_candidate"])