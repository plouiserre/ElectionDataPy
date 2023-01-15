import re

class DistrictModel : 
    def __init__(self) :
        self.id = 0
        self.number = 0
        self.department_id = 0
        self.name = ''
        
    #TODO clean
    def to_district_model(self, data, department_id) :         
        old_data = data
        data = data.replace('[','')
        data = data.replace(']','')
        #data = data.replace('\'','')
        datas = data.split('\'')
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
        if datas[1] == '21' :
            print(old_data)
        district_number = datas[5]
        self.number = int(district_number)
        self.department_id  = department_id
        self.name = datas[7]
        