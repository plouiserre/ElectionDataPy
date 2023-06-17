from src.Factory.CreatorCandidateFirstRound import CreatorCandidateFirstRound
from src.Factory.CreatorCandidates import CreatorCandidates
from src.Models.CandidateModel import CandidateModel

class CreatorCandidatesFirstRound(CreatorCandidates) :
    def __init__(self):
        super().__init__()
        
    def factory_method(self, candidates_data):
        candidates = super().factory_method(candidates_data)
        return candidates
    
    #TODO try factorise with second round method
    def _get_candidate_model(self, candidates_data, index) : 
        candidate = CandidateModel()
        index_candidate = index*9+ self.start_index_candidates
        election_data = candidates_data[index_candidate:index_candidate+9]
        creator = CreatorCandidateFirstRound(None)
        candidate = creator.factory_method(election_data)
        return candidate              
    
    
    def _get_candidates_number(self) :
        last_data = ''
        candidates_number = 0
        for index in range(self.start_index_candidates, len(self.candidates_data)) : 
            data = self.candidates_data[index]
            if last_data == 'nan' and data == 'nan' :
                break
            elif data == 'nan': 
                candidates_number += 1   
            last_data = data   
        return candidates_number   