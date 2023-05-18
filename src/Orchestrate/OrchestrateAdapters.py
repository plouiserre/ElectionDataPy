class OrchestrateAdapters : 
    def __init__(self, dependency) : 
        self.dependency = dependency
        self.__candidates_with_all_datas = []
    
    def get_candidates_datas_from_adapters(self) : 
        candidates_by_adapter = {}  
        adapters = self.dependency.get_dependency("adapters")
        
        candidates_by_adapter = self.__get_candidates_from_adapters(adapters)
            
        for candidate in candidates_by_adapter[0] : 
            self.__candidates_with_all_datas.append(candidate)
        
        self.__orders_datas_to_get_candidates_with_all_datas(candidates_by_adapter[1])
                
        return self.__candidates_with_all_datas
    
    
    def __get_candidates_from_adapters(self, adapters) : 
        candidates_by_adapter = {} 
        index = 0
        for adapter in adapters : 
            adapter.get_datas_needed()
            candidates_from_files = adapter.extracts_datas_from_files()
            candidates_by_adapter[index] = candidates_from_files
            index = index +1 
        return candidates_by_adapter
    
    
    def __orders_datas_to_get_candidates_with_all_datas(self, candidates) : 
        for candidate in candidates :
            for candidate_stored in  self.__candidates_with_all_datas : 
                if candidate_stored.candidate.first_name == candidate.candidate.first_name and candidate_stored.candidate.last_name == candidate.candidate.last_name : 
                    candidate_stored.candidate.vote = candidate.candidate.vote
                    candidate_stored.candidate.rate_vote_registered = candidate.candidate.rate_vote_registered
                    candidate_stored.candidate.rate_vote_expressed = candidate.candidate.rate_vote_expressed
                    candidate_stored.election = candidate.election
        return self.__candidates_with_all_datas
                    