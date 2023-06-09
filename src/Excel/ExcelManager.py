class ExcelManager : 
    def __init__(self):
        pass
    
    def import_elections_datas(self, pd):
        #path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\candidates.xlsx"
        path_file ="/Users/pierre-louisserre/Projects/ElectionDataPy/files/candidates.xlsx"
        data = pd.read_excel(path_file)
        candidates = [] 
        for candidate in enumerate(data.values) :
            can = self.__transform_excel_datas(candidate[1])
            candidates.append(can)
        return candidates    
        
        
    def import_first_round_results_datas(self, pd):
        #path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\result_first_round.xlsx"
        path_file ="/Users/pierre-louisserre/Projects/ElectionDataPy/files/result_first_round.xlsx"
        data = pd.read_excel(path_file)
        first_round_datas = []
        for first_round_datas_district in enumerate(data.values) :
            data = self.__transform_excel_datas(first_round_datas_district[1])
            first_round_datas.append(data)
        return first_round_datas
    
    
    def __transform_excel_datas(self, excel_data) : 
        data_clean = '['
        for i in range(0, len(excel_data)) :
            data = str(excel_data[i])
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