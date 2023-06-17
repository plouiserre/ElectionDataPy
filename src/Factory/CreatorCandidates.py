from src.Models.CandidateModel import CandidateModel
from src.Factory.CreatorCandidate import CreatorCandidate


class CreatorCandidates() : 
    def __init__(self) :
        self.start_index_candidates = 18
        self.candidates_data = []
        
    
    def factory_method(self, candidates_data) : 
        candidates = []
        self.candidates_data = candidates_data
        candidates_number = self._get_candidates_number()
        
        for index in range(0, candidates_number) : 
            candidate = self._get_candidate_model(candidates_data, index)
            candidates.append(candidate)      
        return candidates  