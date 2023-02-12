from src.Models.DistrictModel import DistrictModel
from src.Factory.Creator import Creator

class CreatorDistrict(Creator) : 
    def factory_method(self, data):
        dictrict = DistrictModel()
        data = data.replace('[','')
        data = data.replace(']','')
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')
        data = self.__clean_data(data)
        datas = data.split('_')
        district_number = datas[2]
        dictrict.number = int(district_number)
        dictrict.name = datas[3]
        return dictrict
        
        
    #TODO rename this method
    def __clean_data(self, data) : 
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