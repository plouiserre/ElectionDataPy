from src.Models.DepartmentModel import DepartmentModel

class DepartmentServices :
    def __init__(self) :
        self.departments = []
    
    #TODO check name is ok about the s of the end of the class or update the name
    def manage_departments(self, candidates, department_repository):
        for candidate in candidates :
            department = DepartmentModel()
            department.to_department_model(candidate)
            is_exists = self.deparment_exists(department.number)
            if is_exists == False :
                self.departments.append(department)   
        department_repository.save_departments(self.departments)
    
    def deparment_exists(self, number) :
        is_exist = False
        for deparment in self.departments:
            if deparment.number == number :
                is_exist = True
                break
        return is_exist