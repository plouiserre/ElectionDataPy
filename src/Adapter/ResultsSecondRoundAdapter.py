from src.Adapter.Adapter import Adapter

class ResultsSecondRoundAdapter(Adapter) :
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
        
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    
    def extracts_datas_from_files(self) : 
        datas_from_excel = self.excel_manager.import_second_round_results_datas(self.panda_lib) 
        print("yeah it works!")