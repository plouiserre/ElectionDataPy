class DeputyServices : 
    def __init__(self) :
        self.deputies = []
        pass
    
    def manage_deputies(self, candidates_data_model, candidates, dependency) :
        deputy_repository = dependency.get_dependency("deputyrepository")
        for candidate_data_model in candidates_data_model : 
            deputy = candidate_data_model.deputy
            for candidate in candidates : 
                if candidate.last_name == candidate_data_model.candidate.last_name and candidate.first_name == candidate_data_model.candidate.first_name : 
                    deputy.candidate = candidate
                    break
            self.deputies.append(deputy)
        deputy_repository.save_deputies(self.deputies)
        