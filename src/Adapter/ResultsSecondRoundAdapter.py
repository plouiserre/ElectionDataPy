from src.Adapter.Adapter import Adapter
from src.Factory.CreatorElectionDataSecondRound import CreatorElectionDataSecondRound

class ResultsSecondRoundAdapter(Adapter) :
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
        
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    #TODO subdivise in sub method to clear the functioning of this method
    #TODO rename all variables
    def extracts_datas_from_files(self) : 
        datas_from_excel = self.excel_manager.import_second_round_results_datas(self.panda_lib) 
        all_datas_second_rounds = []
        last_election_datas_created = []
        #TODO study if it is useful if not kill it
        all_election_data_second_round_created = []
        
        for index in range(len(datas_from_excel)) :
            data_each_line = datas_from_excel[index]
            last_election_data_created_before_factory = None
            creator = CreatorElectionDataSecondRound(None, last_election_datas_created)
            data_election_second_round = creator.factory_method(data_each_line)
            all_election_data_second_round_created.append(data_election_second_round)
            last_election_data_created = creator.last_element_created
            last_election_datas_created.append(last_election_data_created)
            if index > 0 : 
                last_election_data_created_before_factory = all_election_data_second_round_created[index - 1]
                if last_election_data_created_before_factory.department.name != last_election_data_created.department.name or last_election_data_created_before_factory.district.name != last_election_data_created.district.name :
                    all_datas_second_rounds.append(last_election_data_created_before_factory)
                    last_election_datas_created = [last_election_data_created]
            if index == len(datas_from_excel) - 1 :
                all_datas_second_rounds.append(data_election_second_round)
            
        return all_datas_second_rounds