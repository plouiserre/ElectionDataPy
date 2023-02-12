from src.Models.DepartmentModel import DepartmentModel
from src.Factory.Creator import Creator

class CreatorDepartment(Creator) : 
    def factory_method(self, data) :         
        dep = DepartmentModel()
        
        datas = self.__get_datas(data)
        
        id = datas[0].replace('\'','')
      
        if id == '2A' or id == '2B' : 
            dep.number = 20
            dep.name = "Corse"
        elif id == "ZA" :
            dep.number = 971
            dep.name = "Guadeloupe"
        elif id == "ZB": 
            dep.name = "Martinique"
            dep.number = 972
        elif id == "ZC": 
            dep.name = "Guyane"
            dep.number = 973
        elif id == "ZD": 
            dep.name = "La Réunion"
            dep.number = 974
        elif id =="ZM":
            dep.name = "Mayotte"
            dep.number = 976
        elif id == "ZN":
            dep.name = "Nouvelle-Calédonie"
            dep.number = 988
        elif id == "ZP":
            dep.name = "Polynésie française"
            dep.number = 987
        elif id == "ZS" : 
            dep.name = "Saint-Pierre-et-Miquelon"
            dep.number = 975
        elif id == "ZW" : 
            dep.name = "Wallis et Futuna"
            dep.number = 986
        elif id == "ZX" : 
            dep.name = "Saint-Martin/Saint-Barthélemy"
            dep.number = 978
        elif id == "ZZ" : 
            dep.name = "Français établis hors de France"
            dep.number = 99
        else :
            id_clean = datas[0].replace('\'','')            
            dep.number = int(id_clean)
            dep.name = datas[1]
            
        return dep
            
            
    def __get_datas(self, data) : 
        data = data.replace('[','')
        data = data.replace(']','')         
        data = data.replace("\"","'")
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')
        datas = data.split('_')
        
        return datas