import pandas as pd

class FileManager : 
    def __init__(self):
        pass
    
    def ImportCandidatesDatas(self):
        path_file = "/Users/plouiserre/Projects/ElectionDataPy/files/candidates.xlsx"
        data = pd.read_excel(path_file, header=None)
        candidates = [] 
        for candidate in data.values :
            can = str(candidate)
            candidates.append(can)
        return candidates
        