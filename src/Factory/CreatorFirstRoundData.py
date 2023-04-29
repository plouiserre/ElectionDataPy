from src.Models.FirstRoundDataModel import FirstRoundDataModel
from src.Factory.CreatorDepartment import CreatorDepartment
from src.Factory.CreatorDistrict import CreatorDistrict
from src.Factory.CreatorElection import CreatorElection

#TODO factoriser avec le code dans creatorcandidatedata    
class CreatorFirstRoundData : 
    def __init__(self) :
        self.__first_round_data = FirstRoundDataModel()
        
    def factory_method(self, data) : 
        datas = self.__get_datas_cleaned(data)
        self.__get_department_model(datas)
        self.__get_district_model(datas)
        self.__get_election_model(datas)
        
        return self.__first_round_data
    
    
    #TODO passer par des self pour les paramètres
    def __get_department_model(self, datas) : 
        creator_departement = CreatorDepartment()
        self.__first_round_data.department = creator_departement.factory_method(datas)
        
        
    def __get_district_model(self, datas) : 
        creator_district = CreatorDistrict()
        self.__first_round_data.district = creator_district.factory_method(datas)
        
    def __get_election_model(self, datas) : 
        creator_election = CreatorElection()
        self.__first_round_data.election = creator_election.factory_method(datas)
        
    
    def __get_datas_cleaned(self, data) : 
        data = ' '.join(data.split())
        data = data.replace('\t',' ')
        data = data.replace('\n ',' ')
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')    
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
        return data.split('_') 