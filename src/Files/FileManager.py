import pandas as pd

class FileManager : 
    def __init__(self):
        pass
    
    def import_candidates_datas(self):
        #TODO put a relative path
        path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\candidates.xlsx"
        data = pd.read_excel(path_file, index_col=None, header=None)
        candidates = [] 
        for i, candidate in enumerate(data.values) :
            if i == 0 : 
                continue
            can = str(candidate)
            candidates.append(can)
        return candidates
        