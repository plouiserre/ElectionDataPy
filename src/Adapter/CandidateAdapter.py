from src.Adapter.Adapter import Adapter
from src.Factory.CreatorCandidateData import CreatorCandidateData 

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
        clients_datas = self.excel_manager.import_candidates_datas(self.pd)       
        candidates = []
        
        for client_data in clients_datas : 
            creator = CreatorCandidateData(self.parties)
            candidate = creator.factory_method(client_data)
            candidates.append(candidate)
        
        return candidates