from src.Adapter.Adapter import Adapter
from src.Factory.CreatorElectionData import CreatorElectionData 


#TODO try to replace modify constructor to use ONLY dependency
class CandidateAdapter(Adapter) : 
    def __init__(self, pd, excel_manager, party_service, party_repository) :
        self.excel_manager = excel_manager
        self.pd = pd
        self.parties = []
        self.party_service = party_service
        self.party_repository = party_repository
        
    
    def get_datas_needed(self) : 
        self.parties = self.party_service.load_parties(self.party_repository)
        
    
    def extracts_datas_from_files(self) : 
        #TODO rename import_candidates_datas in import_elections_datas
        clients_datas = self.excel_manager.import_candidates_datas(self.pd)       
        elections_datas = []
        creator = CreatorElectionData(self.parties)
            
        for index in range(len(clients_datas)) : 
            last_election_data_created = creator.last_election_data_created
            election_data = creator.factory_method(clients_datas[index])
            if last_election_data_created != None and len(last_election_data_created.candidates) > 0 and creator.is_new_election_data_model_created == True :
                    elections_datas.append(last_election_data_created)
            if index + 1 == len(clients_datas) : 
                    elections_datas.append(election_data)
           
        return elections_datas