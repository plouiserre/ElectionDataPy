from src.Adapter.Adapter import Adapter

from src.Factory.CreatorElectionDataFirstRound import CreatorElectionDataFirstRound

class ResultsFirstRoundAdapter(Adapter) : 
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
        
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    
    def extracts_datas_from_files(self) : 
        datas_from_excel = self.excel_manager.import_first_round_results_datas(self.panda_lib) 
        all_datas_from_first_round = []
        
        for data_each_line in datas_from_excel : 
            creator = CreatorElectionDataFirstRound(None)
            data_election_first_round = creator.factory_method(data_each_line)
            all_datas_from_first_round.append(data_election_first_round)
            
        return all_datas_from_first_round