#TODO rework this method because of line 12
class CandidateServices :
    def __init__(self ) :
        self.candidates = []    
    
    def store_candidates(self, candidates_data_model, districts, dependency) : 
        candidate_repository = dependency.get_dependency("candidaterepository")
        for candidate_data_model in candidates_data_model : 
            for candidate in  candidate_data_model.candidates : 
                for district in districts : 
                    if district.department.name == candidate_data_model.department.name and district.name == candidate_data_model.district.name and district.number == candidate_data_model.district.number :
                        candidate.district_id = district.id
                self.candidates.append(candidate)
        candidate_repository.save_candidates(self.candidates)