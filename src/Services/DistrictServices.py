from src.Models.DistrictModel import DistrictModel
from src.Factory.CreatorDistrict import CreatorDistrict

class DistrictServices :
    def __init__(self) :
        self.districts = []
        self.departments = []
    
    def manage_districts(self, candidates, departments, district_repository):
        self.departments = departments
        
        for candidate in candidates :
           creator_district = CreatorDistrict()
           department_id = 0
           department_name = candidate.department_name
           for department_number in departments : 
                if department_name == self.departments[department_number].name : 
                    department_id = self.departments[department_number].id
                    break
                elif department_name =="Corse-du-Sud" or department_name == "Haute-Corse" : 
                    department_id = self.departments[20].id
                    break
                else :
                    continue 
           district = DistrictModel() 
           district = creator_district.factory_method(candidate)
           district.department_id = department_id
           is_exists = self.district_exists(district.number, district.department_id)
           if is_exists == False :                 
                self.districts.append(district)
        district_repository.save_districts(self.districts)        
        
        
    def get_department_name(self, candidate) : 
        department_name = ''
        for i in self.departments : 
            if self.departments[i].name in candidate :
                department_name = self.departments[i].name
                break
        return department_name
                
           
    def district_exists(self, district_number, department_id) :
        is_exist = False
        for district in self.districts:
            if district.number == district_number and district.department_id == department_id :
                is_exist = True
                break
        return is_exist