#TODO add some attributes to improve quality code
class FileManager : 
    def __init__(self):
        pass
    
    def import_candidates_datas(self, pd):
        #TODO put a relative path
        path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\candidates.xlsx"
        data = pd.read_excel(path_file)
        candidates = [] 
        for candidate in enumerate(data.values) :
            can = self.get_candidate_datas(candidate[1])
            candidates.append(can)
        return candidates
        
    
    def get_candidate_datas(self, candidate) : 
        data_clean = '['
        for i in range(0, len(candidate)) :
            data = str(candidate[i])
            is_int_acceptable = data.isdigit() and i != 0
            if i == 0 : 
                if is_int_acceptable : 
                    data_clean += data
                else : 
                    data_clean += "\'"+data+"\'"
            else :
                if is_int_acceptable : 
                    data_clean += " "+data
                else : 
                    data_clean += " \'"+data+"\'"
        data_clean += ']'
        return data_clean