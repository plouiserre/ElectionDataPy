from src.Models.department_model import DepartmentModel

class DepartmentServices :
    def __init__(self) :
        pass
    
    def Manage_Departments(self, candidates):
        departments = []
        for candidate in candidates :
            department = DepartmentModel()
            department.to_department_model(candidate)
            is_exists = self.deparment_exists(departments, department.id)
            if is_exists == False :
                departments.append(department)      
        return departments
    
    def deparment_exists(self, departments, id) :
        is_exist = False
        for deparment in departments:
            if deparment.id == id :
                is_exist = True
                break
        return is_exist