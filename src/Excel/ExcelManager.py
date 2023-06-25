class ExcelManager : 
    def __init__(self):
        pass
    
    def import_elections_datas(self, pd):
        #path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\candidates.xlsx"
        path_file ="/Users/pierre-louisserre/Projects/ElectionDataPy/files/candidates.xlsx"
        candidates = self.__extracts_datas_from_excel(pd, path_file)
        return candidates
        
        
    def import_first_round_results_datas(self, pd):
        #path_file = "C:\\Users\\ploui\\Projects\\ElectionDataPy\\files\\result_first_round.xlsx"
        path_file ="/Users/pierre-louisserre/Projects/ElectionDataPy/files/result_first_round.xlsx"
        first_round_datas = self.__extracts_datas_from_excel(pd, path_file)
        return first_round_datas
    
    
    def import_second_round_results_datas(self, pd) : 
        path_file = "/Users/pierre-louisserre/Projects/ElectionDataPy/files/result_second_round.xlsx"
        second_round_datas = self.__extracts_datas_from_excel(pd, path_file)
        return second_round_datas
    
    
    def __extracts_datas_from_excel(self, pd, path_file) : 
        data = pd.read_excel(path_file)
        datas = []
        for excel_data in enumerate(data.values) :
            data = self.__transform_excel_datas(excel_data[1])
            datas.append(data)
        return datas
    
    
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