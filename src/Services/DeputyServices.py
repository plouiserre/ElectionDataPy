class DeputyServices : 
    def __init__(self) :
        self.deputies = []
        pass
    
    def store_deputies(self, elections_data_model, candidates, dependency) :
        deputy_repository = dependency.get_dependency("deputyrepository")
        for election_data_model in elections_data_model : 
            deputy = election_data_model.deputies[0]
            for candidate in candidates : 
                if candidate.last_name == election_data_model.candidates[0].last_name and candidate.first_name == election_data_model.candidates[0].first_name : 
                    deputy.candidate = candidate
                    break
            self.deputies.append(deputy)
        deputy_repository.save_deputies(self.deputies)
        