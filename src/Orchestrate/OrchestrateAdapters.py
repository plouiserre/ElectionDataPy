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
        
        self.__merge_elections_datas_from_excels(candidates_by_adapter[1])
                
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
    
    
    def __merge_elections_datas_from_excels(self, elections_datas) : 
        for elections_data in elections_datas :
            for candidate in elections_data.candidates :
                for candidates_stored in  self.__candidates_with_all_datas : 
                    for candidate_stored in candidates_stored.candidates :
                        if candidate_stored.first_name == candidate.first_name and candidate_stored.last_name == candidate.last_name : 
                            candidate_stored.vote = candidate.vote
                            candidate_stored.rate_vote_registered = candidate.rate_vote_registered
                            candidate_stored.rate_vote_expressed = candidate.rate_vote_expressed
                            candidates_stored.result = elections_data.result
        return self.__candidates_with_all_datas
                    