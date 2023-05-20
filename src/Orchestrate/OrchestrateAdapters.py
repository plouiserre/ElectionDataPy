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
    
    
    #TODO find better name and naming of parameters
    def __orders_datas_to_get_candidates_with_all_datas(self, candidates_data) : 
        #list_candidates = self.__get_simple_candidates_list(candidates)
        for list_candidates in candidates_data :
            for candidate in list_candidates.candidates :
                for candidates_stored in  self.__candidates_with_all_datas : 
                    for candidate_stored in candidates_stored.candidates :
                        if candidate_stored.first_name == candidate.first_name and candidate_stored.last_name == candidate.last_name : 
                            candidate_stored.vote = candidate.vote
                            candidate_stored.rate_vote_registered = candidate.rate_vote_registered
                            candidate_stored.rate_vote_expressed = candidate.rate_vote_expressed
                            candidates_stored.election = list_candidates.election
        return self.__candidates_with_all_datas
                    