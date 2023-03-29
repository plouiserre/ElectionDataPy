from src.Models.CandidateModel import CandidateModel


class CandidateServices :
    def __init__(self ) :
        self.candidates = []
        pass    
    
    def manage_candidates(self, candidates_data_model, candidate_repository) : 
        for candidate_data_model in candidates_data_model : 
            self.candidates.append(candidate_data_model.candidate)
        candidate_repository.save_candidates(self.candidates)