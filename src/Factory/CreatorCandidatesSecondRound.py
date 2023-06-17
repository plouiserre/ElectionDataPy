from src.Factory.CreatorCandidates import CreatorCandidates
from src.Factory.CreatorCandidateSecondRound import CreatorCandidateSecondRound
from src.Models.CandidateModel import CandidateModel


class CreatorCandidatesSecondRound(CreatorCandidates) : 
    def __init__(self, last_election_data):
        super().__init__()
        #TODO comprendre pk c'est 18 et pas 21
        self.start_index_candidates = 18
        self.last_election_data = last_election_data
        
    
    def factory_method(self, candidates_data):
        candidates = super().factory_method(candidates_data)
        return candidates
    
    
    #TODO try factorise with second round method
    def _get_candidate_model(self, candidates_data, index) : 
        candidate = CandidateModel()
        index_candidate = index * 8 + self.start_index_candidates
        election_data = candidates_data[index_candidate:index_candidate+9]
        if self.last_election_data == None :
            creator = CreatorCandidateSecondRound(None, None)
            candidate = creator.factory_method(election_data)
        else : 
            creator = CreatorCandidateSecondRound(None, self.last_election_data)
            candidate = creator.factory_method(election_data)
        return candidate   
    
    
    def _get_candidates_number(self) :
        j = 0
        candidates_number = 0
        for index in range(self.start_index_candidates, len(self.candidates_data)) : 
            if self.candidates_data[index] == 'nan' :
                break
            else : 
                j += 1
        candidates_number = j // 8
        return candidates_number