from src.Models.CandidateModel import CandidateModel
from src.Factory.CreatorPerson import CreatorPerson

class CreatorCandidate(CreatorPerson) : 
    def __init__(self, parties) -> None:
        self.is_candidate_first_name_simple = True
        self.datas = []
        self.can = CandidateModel()
        self.parties = parties
        
        
    def factory_method(self, election_data) :         
        pass
        
    
    def _init_candidate_model(self, election_data) :
        candidate = CandidateModel()
        candidate.sexe = election_data[1]
        candidate.last_name = election_data[2]
        candidate.first_name = election_data[3]
        return candidate