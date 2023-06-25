from src.Adapter.Adapter import Adapter
from src.Factory.CreatorElectionDataSecondRound import CreatorElectionDataSecondRound

class ResultsSecondRoundAdapter(Adapter) :
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
        self.all_election_data_created = []
        self.last_election_datas_created = []
        self.creator = None
        
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    
    def extracts_datas_from_files(self) : 
        datas_from_excel = self.excel_manager.import_second_round_results_datas(self.panda_lib) 
        all_datas_second_rounds = []
        
        for index in range(len(datas_from_excel)) :
            data_election_second_round = self.__construct_data_election_second_round(index, datas_from_excel)
            last_election_data_created = self.__get_last_election_data_created_and_store_it()
            if index > 0 : 
                election_data_created_last_turn = self.all_election_data_created[index - 1]
                if election_data_created_last_turn.department.name != last_election_data_created.department.name or election_data_created_last_turn.district.name != last_election_data_created.district.name :
                    all_datas_second_rounds.append(election_data_created_last_turn)
                    self.last_election_datas_created = [last_election_data_created]
            if index == len(datas_from_excel) - 1 :
                all_datas_second_rounds.append(data_election_second_round)
            
        return all_datas_second_rounds
    
    
    def __construct_data_election_second_round(self, index, datas_from_excel) :
        data_each_line = datas_from_excel[index]
        self.creator = CreatorElectionDataSecondRound(None, self.last_election_datas_created)
        data_election_second_round = self.creator.factory_method(data_each_line)
        self.all_election_data_created.append(data_election_second_round)
        return data_election_second_round
        
        
    def __get_last_election_data_created_and_store_it(self) :
        last_election_data_created = self.creator.last_element_created
        self.last_election_datas_created.append(last_election_data_created)
        return last_election_data_created