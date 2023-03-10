from src.Models.DistrictModel import DistrictModel
from src.Factory.CreatorDistrict import CreatorDistrict

class DistrictServices :
    def __init__(self) :
        self.districts = []
        self.departments = []
    
    def manage_districts(self, candidates, departments, district_repository):
        self.departments = departments
        
        for candidate in candidates :
           district = candidate.district 
           department_id = self.get_department_id(candidate)
           candidate.department.id = department_id
           is_exists = self.district_exists(district.number, district.department.id)
           if is_exists == False :                 
                self.districts.append(district)
        district_repository.save_districts(self.districts)        
        
        
    def get_department_id(self, candidate) : 
        department_id = 0
        for department_number, department in self.departments.items() : 
            if candidate.department.number == department_number :
                department_id = department.id
                break
        return department_id
                
           
    def district_exists(self, district_number, department_id) :
        is_exist = False
        for district in self.districts:
            if district.number == district_number and district.department.id == department_id :
                is_exist = True
                break
        return is_exist