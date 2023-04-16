from src.Adapter.Adapter import Adapter

class FirstRoundAdapter(Adapter) : 
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    
    def extracts_datas_from_files(self) : 
        self.excel_manager.import_first_round_results_datas(self.panda_lib) 
    