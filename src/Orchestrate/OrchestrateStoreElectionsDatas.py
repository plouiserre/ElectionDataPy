import pandas as pd
from src.Adapter.CandidateAdapter import CandidateAdapter

class OrchestrateStoreElectionsDatas :
    def __init__(self, dependency) :
        self.dependency = dependency
        self.deparment_service = self.dependency.get_dependency("deparmentservices")
        self.district_service = self.dependency.get_dependency("districtservices")
        self.candidate_service = self.dependency.get_dependency("candidateservices")
        self.deputy_service = self.dependency.get_dependency("deputyservices")
        
        
    def store_elections_datas(self) :
        candidates = self.__get_elections_datas_from_adapters()
        self.deparment_service.store_departments(candidates, self.dependency)
        self.district_service.store_districts(candidates, self.deparment_service.departments, self.dependency)
        self.candidate_service.store_candidates(candidates, self.district_service.districts,self.dependency)
        self.deputy_service.store_deputies(candidates, self.candidate_service.candidates, self.dependency)
        
        
    def __get_elections_datas_from_adapters(self) : 
        candidates = [] 
        candidate_adapter = self.__get_init_candidate_adapter()
        adapters = []
        adapters.append(candidate_adapter)
        for adapter in adapters : 
            adapter.get_datas_needed()
            candidates = adapter.extracts_datas_from_files()
        return candidates
    
    
    def __get_init_candidate_adapter(self) :        
        excel_manager = self.dependency.get_dependency("excel")
        party_service = self.dependency.get_dependency("partyservices")
        party_repository = self.dependency.get_dependency("partyrepository")
        candidate_adapter = CandidateAdapter(pd,excel_manager,party_service, party_repository)
        return candidate_adapter
        