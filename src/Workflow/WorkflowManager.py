class WorkflowManager :
    def __init__(self, dependency) :
        self.dependency = dependency
        self.deparment_service = self.dependency.get_dependency("deparmentservices")
        self.district_service = self.dependency.get_dependency("districtservices")
        self.candidate_service = self.dependency.get_dependency("candidateservices")
        self.deputy_service = self.dependency.get_dependency("deputyservices")
        
        
    def store_datas(self) :
        candidates = self.__get_datas_from_adapters()
        self.deparment_service.manage_departments(candidates, self.dependency)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, self.dependency)
        self.candidate_service.manage_candidates(candidates, self.district_service.districts,self.dependency)
        self.deputy_service.manage_deputies(candidates, self.candidate_service.candidates, self.dependency)
        
        
    def __get_datas_from_adapters(self) : 
        candidates = [] 
        adapters = self.dependency.get_dependency("adapters")
        for adapter in adapters : 
            adapter.get_datas_needed()
            candidates = adapter.extracts_datas_from_files()
        return candidates