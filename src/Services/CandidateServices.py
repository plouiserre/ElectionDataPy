#TODO rework this method because of line 12
class CandidateServices :
    def __init__(self ) :
        self.candidates = []    
    
    def store_candidates(self, election_datas_model, districts, dependency) : 
        candidate_repository = dependency.get_dependency("candidaterepository")
        for election_data_model in election_datas_model : 
            for candidate in  election_data_model.candidates : 
                for district in districts : 
                    if district.department.name == election_data_model.department.name and district.name == election_data_model.district.name and district.number == election_data_model.district.number :
                        candidate.district_id = district.id
                self.candidates.append(candidate)
        candidate_repository.save_candidates(self.candidates)