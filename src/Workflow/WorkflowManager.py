from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DistrictRepository import DistrictRepository

class WorkflowManager :
    def __init__(self) :
        pass

    #TODO put this parameters in the construct to respect clean code
    def store_departments(self, fileManager, departmentService, districtService, pd) :
        department_repository = DepartmentRepository()
        district_repository = DistrictRepository()
        candidates = fileManager.import_candidates_datas(pd)
        departmentService.manage_departments(candidates, department_repository)
        districtService.manage_districts(candidates, departmentService.departments, district_repository)