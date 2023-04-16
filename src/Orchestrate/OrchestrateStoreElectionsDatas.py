class OrchestrateStoreElectionsDatas :
    def __init__(self, dependency) :
        self.dependency = dependency
        self.deparment_service = self.dependency.get_dependency("deparmentservices")
        self.district_service = self.dependency.get_dependency("districtservices")
        self.candidate_service = self.dependency.get_dependency("candidateservices")
        self.deputy_service = self.dependency.get_dependency("deputyservices")
        
        
    def store_elections_datas(self) :
        candidates = self.__get_elections_datas_from_adapters()
        print("no save in database for the moment")
        # self.deparment_service.store_departments(candidates, self.dependency)
        # self.district_service.store_districts(candidates, self.deparment_service.departments, self.dependency)
        # self.candidate_service.store_candidates(candidates, self.district_service.districts,self.dependency)
        # self.deputy_service.store_deputies(candidates, self.candidate_service.candidates, self.dependency)
        
        
    def __get_elections_datas_from_adapters(self) : 
        candidates = [] 
        candidate_adapter = self.dependency.get_dependency("candidateadapter")
        first_round_adapter = self.dependency.get_dependency("firstroundadapter")
        adapters = []
        adapters.append(candidate_adapter)
        adapters.append(first_round_adapter)
        for adapter in adapters : 
            adapter.get_datas_needed()
            candidates_from_files = adapter.extracts_datas_from_files()
            if candidates_from_files != None : 
                for candidate in candidates_from_files : 
                    candidates.append(candidate)
        return candidates
        