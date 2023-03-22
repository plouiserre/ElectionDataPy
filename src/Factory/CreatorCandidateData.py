import datetime

from src.Models.CandidateDataModel import CandidateDataModel
from src.Factory.CreatorDepartment import CreatorDepartment
from src.Factory.CreatorDistrict import CreatorDistrict
from src.Factory.Creator import Creator

class CreatorCandidateData(Creator) : 
    def __init__(self, parties) :
        self.candidate_data = CandidateDataModel()
        self.datas = []
        self.is_candidate_first_name_simple = True
        self.is_deputy_first_name_simple = True
        self.parties = parties
        
        
    def factory_method(self, data):
        data = self.__clean_data(data)
        
        self.datas = data.split('_')    
        
        self.__get_department_candidate_datas()    
        
        self.__get_district_candidate_datas()
        
        self.__get_candidate_datas()
        
        self.__get_deputy_datas()
               
        return self.candidate_data
    
    
    #TODO simple and explicit this complex method
    def __clean_data(self, data) : 
        data = ' '.join(data.split())
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
       self.candidate_data.candidate.sexe = self.datas[5]
       self.candidate_data.candidate.last_name = self.datas[6]
       if self.datas[11] == 'Oui' :
           self.candidate_data.candidate_is_sorting = True
       self.__get_candidate_first_name()
       self.__get_candidate_birth_date()
       self.__get_candidate_party()
       self.__get_candidate_jobs()
       
    
    def __get_candidate_first_name(self) :  
        if str.isalpha(self.datas[8]) : 
            self.is_candidate_first_name_simple = False
            self.candidate_data.candidate.first_name = self.datas[7]+" "+self.datas[8]
        else :
            self.candidate_data.candidate.first_name = self.datas[7]
              
       
    def __get_candidate_birth_date(self) : 
        birthdate = ''
        if  self.is_candidate_first_name_simple == False :
            birthdate = self.datas[9]
        else : 
            birthdate = self.datas[8]
        birthdate = birthdate.replace('-', '/')
        birthdate = birthdate.replace(' 00:00:00','')
        birthdate_elements = birthdate.split('/')
        year = int(birthdate_elements[0])
        month = int(birthdate_elements[1])
        day = int(birthdate_elements[2])
        self.candidate_data.candidate.birth_date = datetime.datetime(year, month, day)
        
    
    def __get_candidate_party(self) : 
        party_shortname = ''
        if  self.is_candidate_first_name_simple :
           party_shortname = self.datas[9]
        else :
           party_shortname = self.datas[10]
        for party in self.parties : 
            if party.short_name == party_shortname : 
                self.candidate_data.candidate.party_id = party.id
            
            
    def __get_candidate_jobs(self) : 
         if  self.is_candidate_first_name_simple :
            self.candidate_data.candidate.job = self.datas[10]
         else :
            self.candidate_data.candidate.job = self.datas[11]
            
    
    def __get_deputy_datas(self) : 
         self.__get_deputy_sexe()
         self.__get_deputy_last_name()
         self.__get_deputy_first_name()
         self.__get_deputy_birthdate()
         self.__get_deputy_sorting()
         
                
    def __get_deputy_sexe(self) :
         if  self.is_candidate_first_name_simple :
            self.candidate_data.deputy.sexe = self.datas[12]
         else :
            self.candidate_data.deputy.sexe = self.datas[13]
            
            
    def __get_deputy_last_name(self) : 
        if self.is_candidate_first_name_simple : 
            self.candidate_data.deputy.last_name = self.datas[13]
        else : 
            self.candidate_data.deputy.last_name = self.datas[14]
            
            
    def __get_deputy_first_name(self) :         
        deputy_first_name_index = 14
        if self.is_candidate_first_name_simple == False : 
            deputy_first_name_index += 1
        if (('datetime' in self.datas[15]) == False and self.is_candidate_first_name_simple) or (('datetime' in self.datas[16]) == False and self.is_candidate_first_name_simple == False) :
             self.is_deputy_first_name_simple = False
        if self.is_deputy_first_name_simple == False :
            self.candidate_data.deputy.first_name = self.datas[deputy_first_name_index] +' '+ self.datas[deputy_first_name_index + 1]
        else :
            self.candidate_data.deputy.first_name = self.datas[deputy_first_name_index]
            
            
    def __get_deputy_birthdate(self) : 
        birthdate = ''
        if self.is_candidate_first_name_simple and self.is_deputy_first_name_simple : 
           birthdate = self.datas[15]
        elif (self.is_candidate_first_name_simple == False and self.is_deputy_first_name_simple) or (self.is_candidate_first_name_simple and self.is_deputy_first_name_simple == False) :
            birthdate = self.datas[16]
        else : 
            birthdate = self.datas[17]
        birthdate = birthdate.replace('datetime.datetime(', '')
        birthdate = birthdate.replace(', 0, 0)','')
        birthdate = birthdate.replace(')','')
        birthdate_elements = birthdate.split(',')
        year = int(str.strip(birthdate_elements[0]))
        month = int(str.strip(birthdate_elements[1]))
        day = int(str.strip(birthdate_elements[2]))
        self.candidate_data.deputy.birth_date = datetime.datetime(year, month, day)
        
        
    def __get_deputy_sorting(self) : 
        if self.is_candidate_first_name_simple : 
          if 'Oui' in self.datas[16]  :
                self.candidate_data.deputy.is_sorting = True
        else : 
            if 'Oui' in self.datas[17] :
                self.candidate_data.deputy.is_sorting  = True