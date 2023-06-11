from src.Factory.CreatorElectionData import CreatorElectionData

from src.Models.ElectionDataModel import ElectionDataModel

class CreatorElectionDataSecondRound(CreatorElectionData) : 
    def __init__(self, parties) :
        self.election_data = ElectionDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        self.last_election_data_created = ElectionDataModel()
        self.is_new_election_data_model_created = False
        
    def factory_method(self, data) :
        self.datas = self._get_datas_cleaned_rounds(data)
        self.__delete_city_datas()
        self._get_department_election_datas()
        self._get_district_election_datas()
        self._get_result_model()
        self._get_candidates_model()
        
        return self.election_data
    
    def __delete_city_datas(self) : 
        del self.datas[4]
        del self.datas[4]