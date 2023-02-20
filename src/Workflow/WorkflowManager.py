from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DistrictRepository import DistrictRepository
from src.Repository.mydb import MyDb

class WorkflowManager :
    def __init__(self, departmentService, districtService, candidate_adapter) :
        self.deparment_service = departmentService
        self.district_service = districtService
        self.candidate_adapter = candidate_adapter
        
    def store_departments(self) :
        mydb = MyDb()
        department_repository = DepartmentRepository(mydb)
        district_repository = DistrictRepository(mydb)
        candidates = self.candidate_adapter.get_candidates()
        self.deparment_service.manage_departments(candidates, department_repository)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, district_repository)