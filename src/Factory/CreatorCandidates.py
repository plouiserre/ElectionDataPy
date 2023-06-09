from src.Models.CandidateModel import CandidateModel
from src.Factory.CreatorCandidate import CreatorCandidate

class CreatorCandidates() : 
    def __init__(self) :
        self.start_index_candidates = 18
        self.candidates_data = []
        
    
    def factory_method(self, candidates_data) : 
        candidates = []
        self.candidates_data = candidates_data
        candidates_number = self.__get_candidates_number()
        
        for index in range(0, candidates_number) : 
            candidate = self.__get_candidate_model(candidates_data, index)
            candidates.append(candidate)      
        return candidates
    
    
    def __get_candidate_model(self, candidates_data, index) : 
        candidate = CandidateModel()
        index_candidate = index*9+ self.start_index_candidates
        election_data = candidates_data[index_candidate:index_candidate+9]
        creator = CreatorCandidate(None)
        candidate = creator.factory_candidate_first_round_method(election_data)
        return candidate              
    
    
    def __get_candidates_number(self) :
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