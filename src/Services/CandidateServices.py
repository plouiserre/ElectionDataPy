from src.Models.CandidateModel import CandidateModel


class CandidateServices :
    def __init__(self ) :
        pass    
    
    def manage_candidates(self, candidates_data_model, candidate_repository) : 
        candidates = []
        for candidate_data_model in candidates_data_model : 
            candidates.append(candidate_data_model.candidate)
        candidate_repository.save_candidates(candidates)