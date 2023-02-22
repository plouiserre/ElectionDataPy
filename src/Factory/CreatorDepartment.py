from src.Models.DepartmentModel import DepartmentModel
from src.Factory.Creator import Creator

class CreatorDepartment(Creator) : 
    def factory_method(self, candidate_data) :         
        dep = DepartmentModel()
        department_id = candidate_data[0].replace('\'','')
      
        if department_id == '2A' or department_id == '2B' : 
            dep.number = 20
            dep.name = "Corse"
        elif department_id == "ZA" :
            dep.number = 971
            dep.name = "Guadeloupe"
        elif department_id == "ZB": 
            dep.name = "Martinique"
            dep.number = 972
        elif department_id == "ZC": 
            dep.name = "Guyane"
            dep.number = 973
        elif department_id == "ZD": 
            dep.name = "La Réunion"
            dep.number = 974
        elif department_id =="ZM":
            dep.name = "Mayotte"
            dep.number = 976
        elif department_id == "ZN":
            dep.name = "Nouvelle-Calédonie"
            dep.number = 988
        elif department_id == "ZP":
            dep.name = "Polynésie française"
            dep.number = 987
        elif department_id == "ZS" : 
            dep.name = "Saint-Pierre-et-Miquelon"
            dep.number = 975
        elif department_id == "ZW" : 
            dep.name = "Wallis et Futuna"
            dep.number = 986
        elif department_id == "ZX" : 
            dep.name = "Saint-Martin/Saint-Barthélemy"
            dep.number = 978
        elif department_id == "ZZ" : 
            dep.name = "Français établis hors de France"
            dep.number= 99
        else :
            id_clean = candidate_data[0].replace('\'','')            
            dep.number = int(id_clean)
            dep.name = candidate_data[1]
            
        return dep