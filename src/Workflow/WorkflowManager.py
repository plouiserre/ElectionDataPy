from src.Repository.DepartmentRepository import DepartmentRepository

class WorkflowManager :
    def __init__(self) :
        pass

    def store_departments(self, fileManager, departmentService) :
        department_repository = DepartmentRepository()
        candidates = fileManager.import_candidates_datas()
        departmentService.manage_departments(candidates, department_repository)