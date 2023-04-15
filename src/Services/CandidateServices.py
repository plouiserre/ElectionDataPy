class CandidateServices :
    def __init__(self ) :
        self.candidates = []    
    
    def store_candidates(self, candidates_data_model, districts, dependency) : 
        candidate_repository = dependency.get_dependency("candidaterepository")
        for candidate_data_model in candidates_data_model : 
            candidate = candidate_data_model
            for district in districts : 
                if district.department.name == candidate.department.name and district.name == candidate.district.name and district.number == candidate.district.number :
                    candidate.candidate.district_id = district.id
            self.candidates.append(candidate.candidate)
        candidate_repository.save_candidates(self.candidates)