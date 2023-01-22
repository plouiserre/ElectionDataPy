import re

class DistrictModel : 
    def __init__(self) :
        self.id = 0
        self.number = 0
        self.department_id = 0
        self.name = ''
        
    #TODO clean
    #TODO erase departments arguments of the methods and the dictionary departments
    def to_district_model(self, data, department_id) :         
        old_data = data
        data = data.replace('[','')
        data = data.replace(']','')
        #data = data.replace('\'','')
        data = data.replace('\' \'','_')
        data = self.clean_data(data)
        datas = data.split('_')
        '''
        pour régler ce problème je dois d'abord supprimer les '
        ensuite je fais une boucle et je supprime les entrées vides '' ou ' '
        pour finir je récupère les bonnes données
        '''
        '''district_number = datas[2].replace('\'','')
        self.number = int(district_number)
        self.department_id = department_id
        department_name = datas[3]+" "+datas[4]
        self.name = department_name.replace('\'','')'''
        district_number = datas[2]
        self.number = int(district_number)
        self.department_id  = department_id
        self.name = datas[3]
        
        
    def clean_data(self, data) : 
        #"'01' 'Ain' '05' '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non'"
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
        