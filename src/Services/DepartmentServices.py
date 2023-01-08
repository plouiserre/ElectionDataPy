from src.Models.department_model import DepartmentModel

class DepartmentServices :
    def __init__(self) :
        self.departments = []
    
    #TODO put departments in elements of the class and not return of this method or delete the test needed that
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