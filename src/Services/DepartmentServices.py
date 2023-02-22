from src.Models.DepartmentModel import DepartmentModel
from src.Factory.CreatorDepartment import CreatorDepartment

class DepartmentServices :
    def __init__(self) :
        self.departments = {}
    
    def manage_departments(self, candidates, department_repository):
        for candidate in candidates :
            department = candidate.department
            is_exists = self.deparment_exists(department.number)
            if is_exists == False :
                self.departments.update({department.number: department})   
        department_repository.save_departments(self.departments)
    
    def deparment_exists(self, number) :
        is_exist = False
        for deparment in self.departments:
            if deparment == number :
                is_exist = True
                break
        return is_exist