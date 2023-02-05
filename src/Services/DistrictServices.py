from src.Models.DistrictModel import DistrictModel

class DistrictServices :
    def __init__(self) :
        self.districts = []
    
    #TODO improve this code
    #TODO reduce parameters of this methods
    def manage_districts(self, candidates, departments, district_repository):
        for candidate in candidates :
           district = DistrictModel() 
           department_id = 0
           department_name = self.get_department_name(candidate, departments)           
           for department_number in departments : 
                if department_name == departments[department_number].name : 
                    department_id = departments[department_number].id
                    break
                elif department_name =="Corse-du-Sud" or department_name == "Haute-Corse" : 
                    department_id = departments[20].id
                else :
                    continue 
           district.to_district_model(candidate, department_id)
           is_exists = self.district_exists(district.number, district.department_id)
           if is_exists == False :                 
                self.districts.append(district)
        district_repository.save_districts(self.districts)        
        
        
    def get_department_name(self, candidate, departments) : 
        department_name = ''
        for i in departments : 
            if departments[i].name in candidate :
                department_name = departments[i].name
                break
        return department_name
                
           
    def district_exists(self, district_number, department_id) :
        is_exist = False
        for district in self.districts:
            if district.number == district_number and district.department_id == department_id :
                is_exist = True
                break
        return is_exist