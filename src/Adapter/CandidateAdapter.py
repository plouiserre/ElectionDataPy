from src.Excel.ExcelManager import ExcelManager
from src.Models.CandidateDataModel import CandidateDataModel
from src.Factory.CreatorCandidateData import CreatorCandidateData

class CandidateAdapter : 
    def __init__(self, pd, excel_manager) :
        self.excel_manager = excel_manager
        self.pd = pd
        pass
    
    def get_candidates(self) : 
        clients_datas = self.excel_manager.import_candidates_datas(self.pd)       
        candidates = []
        
        for client_data in clients_datas : 
            creator = CreatorCandidateData()
            candidate = creator.factory_method(client_data)
            candidates.append(candidate)
        
        return candidates