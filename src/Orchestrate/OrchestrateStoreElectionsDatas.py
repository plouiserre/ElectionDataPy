class OrchestrateStoreElectionsDatas :
    def __init__(self, dependency, orchestrate_adapters) :
        self.dependency = dependency
        self.orchestrate_adapters = orchestrate_adapters
        self.deparment_service = self.dependency.get_dependency("deparmentservices")
        self.district_service = self.dependency.get_dependency("districtservices")
        self.candidate_service = self.dependency.get_dependency("candidateservices")
        self.deputy_service = self.dependency.get_dependency("deputyservices")
        
        
    def store_elections_datas(self) :
        elections_candidates_data = self.orchestrate_adapters.get_candidates_datas_from_adapters()
        self.deparment_service.store_departments(elections_candidates_data, self.dependency)
        self.district_service.store_districts(elections_candidates_data, self.deparment_service.departments, self.dependency)
        self.candidate_service.store_candidates(elections_candidates_data, self.district_service.districts,self.dependency)
        self.deputy_service.store_deputies(elections_candidates_data, self.candidate_service.candidates, self.dependency)
        