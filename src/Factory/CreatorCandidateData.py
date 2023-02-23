from src.Models.CandidateDataModel import CandidateDataModel
from src.Factory.CreatorDepartment import CreatorDepartment
from src.Factory.CreatorDistrict import CreatorDistrict
from src.Factory.Creator import Creator

class CreatorCandidateData(Creator) : 
    def __init__(self) -> None:
        self.candidate_data = CandidateDataModel()
        self.datas = []
        self.is_first_name_simple = True
        
        
    def factory_method(self, data):
        data = self.__clean_data(data)
        
        self.datas = data.split('_')    
        
        self.__get_department_candidate_datas()    
        
        self.__get_district_candidate_datas()
        
        #self.__get_candidate_datas()
               
        return self.candidate_data
    
    
    def __clean_data(self, data) : 
        data = data.replace('\t',' ')
        data = data.replace('\n ',' ')
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
        dep_creator = CreatorDepartment()
        self.candidate_data.department = dep_creator.factory_method(self.datas)
            
            
    def __get_district_candidate_datas(self) : 
        dis_creator = CreatorDistrict()
        self.candidate_data.district = dis_creator.factory_method(self.datas)
        self.candidate_data.district.department = self.candidate_data.department
        
        
    def __get_candidate_datas(self) : 
       self.candidate_data.candidate_sexe = self.datas[5]
       self.candidate_data.candidate_last_name = self.datas[6]
       if self.datas[11] == 'Oui' :
           self.candidate_data.candidate_is_sorting = True
       self.__get_candidate_first_name()
       self.__get_candidate_birth_date()
       self.__get_candidate_party()
       self.__get_candidate_jobs()
       
       
    def __get_candidate_first_name(self) :  
        if "datetime.datetime(" in self.datas[8] :
            self.candidate_data.candidate_first_name = self.datas[7]
        else :
            self.is_first_name_simple = False
            self.candidate_data.candidate_first_name = self.datas[7]+" "+self.datas[8]
              
       
    #WARNING for the moment we accept day like 0x
    def __get_candidate_birth_date(self) : 
        birthdate = ''
        if  self.is_first_name_simple :
            birthdate = self.datas[8]
        else :
            birthdate = self.datas[9]
        birthdate = str.replace(birthdate, 'datetime.datetime(','')
        birthdate = str.replace(birthdate, ')','')
        birthdate_element = birthdate.split(',')
        self.candidate_data.candidate_birth_date = str.strip(birthdate_element[1])+'/'+str.strip(birthdate_element[2])+'/'+str.strip(birthdate_element[0])
        
    
    def __get_candidate_party(self) : 
         if  self.is_first_name_simple :
            self.candidate_data.candidate_party = self.datas[9]
         else :
            self.candidate_data.candidate_party = self.datas[10]
            
            
    def __get_candidate_jobs(self) : 
         if  self.is_first_name_simple :
            self.candidate_data.candidate_job = self.datas[10]
         else :
            self.candidate_data.candidate_job = self.datas[11]