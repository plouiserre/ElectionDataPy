from src.Models.CandidateModel import CandidateModel


class CandidateServices :
    def __init__(self ) :
        self.candidates = []    
    
    def manage_candidates(self, candidates_data_model, candidate_repository, districts) : 
        for candidate_data_model in candidates_data_model : 
            candidate = candidate_data_model
            for district in districts : 
                if district.department.name == candidate.department.name and district.name == candidate.district.name and district.number == candidate.district.number :
                    candidate.candidate.district_id = district.id
            self.candidates.append(candidate.candidate)
        candidate_repository.save_candidates(self.candidates)