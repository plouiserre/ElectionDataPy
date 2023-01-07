from src.Repository.DepartmentRepository import DepartmentRepository

class WorkflowManager :
    def __init__(self) :
        pass

    def StoreDepartments(self, fileManager, departmentService) :
        department_repository = DepartmentRepository()
        candidates = fileManager.ImportCandidatesDatas()
        departmentService.Manage_Departments(candidates, department_repository)