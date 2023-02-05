import re

class DistrictModel : 
    def __init__(self) :
        self.id = 0
        self.number = 0
        self.department_id = 0
        self.name = ''
        
    def to_district_model(self, data, department_id) :         
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')
        data = self.clean_data(data)
        datas = data.split('_')
        district_number = datas[2]
        self.number = int(district_number)
        self.department_id  = department_id
        self.name = datas[3]
        
        
    def clean_data(self, data) : 
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
        