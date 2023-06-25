from src.Factory.CreatorCandidatesFirstRound import CreatorCandidatesFirstRound
from src.Factory.CreatorElectionData import CreatorElectionData
from src.Factory.CreatorResultFirstRound import CreatorResultFirstRound
from src.Models.ElectionDataModel import ElectionDataModel

#TODO factorize the constructor
class CreatorElectionDataFirstRound(CreatorElectionData) : 
    def __init__(self, parties) :
        super().__init__(parties)
        
    def factory_method(self, data):
        self.datas = self._get_datas_cleaned_rounds(data)
        self._get_department_election_datas()
        self._get_district_election_datas()
        self._get_result_model()
        self._get_candidates_model()
        
        return self.election_data
    
    
    def _get_result_model(self) : 
        creator_result = CreatorResultFirstRound()
        self.election_data.first_result = creator_result.factory_method(self.datas)
    
    
    def _get_candidates_model(self) : 
        creator_candidates = CreatorCandidatesFirstRound()
        self.election_data.candidates = creator_candidates.factory_method(self.datas)