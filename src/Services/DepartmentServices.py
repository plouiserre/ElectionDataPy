from src.Models.department_model import DepartmentModel

class DepartmentServices :
    def __init__(self) :
        pass
    
    #TODO put departments in elements of the class and not return of this method or delete the test needed that
    def Manage_Departments(self, candidates, department_repository):
        departments = []
        for candidate in candidates :
            department = DepartmentModel()
            department.to_department_model(candidate)
            is_exists = self.deparment_exists(departments, department.number)
            if is_exists == False :
                departments.append(department)      
        department_repository.Save_Departments(departments)
        return departments
    
    def deparment_exists(self, departments, number) :
        is_exist = False
        for deparment in departments:
            if deparment.number == number :
                is_exist = True
                break
        return is_exist