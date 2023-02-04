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
           #TODO externalize in a new methods
           department_name = candidate.split(' ')[1].replace('\'','')
           for department_number in departments : 
                if department_name == departments[department_number].name : 
                    department_id = departments[department_number].id
                    break
                else :
                    continue 
           district.to_district_model(candidate, department_id)
           is_exists = self.district_exists(district.number, district.department_id)
           if is_exists == False :                 
                self.districts.append(district)
        district_repository.save_districts(self.districts)
                
           
    def district_exists(self, district_number, department_id) :
        is_exist = False
        for district in self.districts:
            if district.number == district_number and district.department_id == department_id :
                is_exist = True
                break
        return is_exist