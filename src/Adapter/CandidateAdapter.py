from src.Adapter.Adapter import Adapter
from src.Factory.CreatorElectionData import CreatorElectionData 


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
        excel_elections_datas = self.excel_manager.import_elections_datas(self.pd)       
        elections_datas = []
        creator = CreatorElectionData(self.parties)
            
        for index in range(len(excel_elections_datas)) : 
            last_election_data_created = creator.last_election_data_created
            election_data = creator.factory_method(excel_elections_datas[index])
            if last_election_data_created != None and len(last_election_data_created.candidates) > 0 and creator.is_new_election_data_model_created == True :
                    elections_datas.append(last_election_data_created)
            if index + 1 == len(excel_elections_datas) : 
                    elections_datas.append(election_data)
           
        return elections_datas