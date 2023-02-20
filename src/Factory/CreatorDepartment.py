from src.Models.DepartmentModel import DepartmentModel
from src.Factory.Creator import Creator

class CreatorDepartment(Creator) : 
    def factory_method(self, candidate_data) :         
        dep = DepartmentModel()
        
        dep.number = candidate_data.department_number
        dep.name = candidate_data.department_name
        
        return dep