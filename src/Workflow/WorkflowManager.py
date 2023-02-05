from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DistrictRepository import DistrictRepository
from src.Repository.mydb import MyDb

class WorkflowManager :
    def __init__(self, fileManager, departmentService, districtService, pd) :
        self.file_manager = fileManager
        self.deparment_service = departmentService
        self.district_service = districtService
        self.pd = pd
        
    def store_departments(self) :
        mydb = MyDb()
        department_repository = DepartmentRepository(mydb)
        district_repository = DistrictRepository(mydb)
        candidates = self.file_manager.import_candidates_datas(self.pd)
        self.deparment_service.manage_departments(candidates, department_repository)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, district_repository)