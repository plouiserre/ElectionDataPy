from src.Models.CandidateDataModel import CandidateDataModel
from src.Factory.Creator import Creator

class CreatorCandidateData(Creator) : 
    def __init__(self) -> None:
        self.candidate_data = CandidateDataModel()
        self.datas = []
        
        
    def factory_method(self, data):
        data = self.__clean_data(data)
        
        self.datas = data.split('_')    
        
        self.__get_department_candidate_datas()    
        
        self.__get_district_candidate_datas()
               
        return self.candidate_data
    
    def __clean_data(self, data) : 
        data = data.replace('\t',' ')
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')    
        data_cleaned = data
        to_delete = ''
        for i in range(0, len(data)):
            caracter = data[i]
            if i == len(data)-1 : 
                break
            elif caracter == '\'' and to_delete == '' and data[i+1] == ' ':
                to_delete += caracter
            elif to_delete !='' : 
                to_delete += caracter
                if data[i+1] == '\'' and to_delete != '':
                    data_cleaned = data_cleaned.replace(to_delete, '_')
                    to_delete = ''
            else : 
                continue
        return data_cleaned
    
    
    def __get_department_candidate_datas(self) : 
        #TODO externalise in a specific method
        department_id = self.datas[0].replace('\'','')
      
        if department_id == '2A' or department_id == '2B' : 
            self.candidate_data.department_number = 20
            self.candidate_data.department_name = "Corse"
        elif department_id == "ZA" :
            self.candidate_data.department_number = 971
            self.candidate_data.department_name = "Guadeloupe"
        elif department_id == "ZB": 
            self.candidate_data.department_name = "Martinique"
            self.candidate_data.department_number = 972
        elif department_id == "ZC": 
            self.candidate_data.department_name = "Guyane"
            self.candidate_data.department_number = 973
        elif department_id == "ZD": 
            self.candidate_data.department_name = "La Réunion"
            self.candidate_data.department_number = 974
        elif department_id =="ZM":
            self.candidate_data.department_name = "Mayotte"
            self.candidate_data.department_number = 976
        elif department_id == "ZN":
            self.candidate_data.department_name = "Nouvelle-Calédonie"
            self.candidate_data.department_number = 988
        elif department_id == "ZP":
            self.candidate_data.department_name = "Polynésie française"
            self.candidate_data.department_number = 987
        elif department_id == "ZS" : 
            self.candidate_data.department_name = "Saint-Pierre-et-Miquelon"
            self.candidate_data.department_number = 975
        elif department_id == "ZW" : 
            self.candidate_data.department_name = "Wallis et Futuna"
            self.candidate_data.department_number = 986
        elif department_id == "ZX" : 
            self.candidate_data.department_name = "Saint-Martin/Saint-Barthélemy"
            self.candidate_data.department_number = 978
        elif department_id == "ZZ" : 
            self.candidate_data.department_name = "Français établis hors de France"
            self.candidate_data.department_number= 99
        else :
            id_clean = self.datas[0].replace('\'','')            
            self.candidate_data.department_number = int(id_clean)
            self.candidate_data.department_name = self.datas[1]
            
            
    def __get_district_candidate_datas(self) : 
        district_number = self.datas[2]
        self.candidate_data.district_number = int(district_number)
        self.candidate_data.district_name = self.datas[3]
        