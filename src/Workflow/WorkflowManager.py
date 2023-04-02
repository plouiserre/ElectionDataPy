from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DistrictRepository import DistrictRepository
from src.Repository.CandidateRepository import CandidateRepository
from src.Repository.DeputyRepository import DeputyRepository

#TODO mieux travailler les dépendances
#- pour une première étape, les init des repositories devront se faire dans les services
#- pour une seconde étape, faire une classe qui init tout et qui fournit le bon objet au bon moment
class WorkflowManager :
    def __init__(self, departmentService, districtService, adapters, candidate_service, deputy_service, mydb) :
        self.deparment_service = departmentService
        self.district_service = districtService
        self.adapters = adapters
        self.candidate_service = candidate_service
        self.deputy_service = deputy_service
        self.department_repository = DepartmentRepository(mydb)
        self.district_repository = DistrictRepository(mydb)
        self.candidate_repository = CandidateRepository(mydb)
        self.deputy_repository = DeputyRepository(mydb)
        self.parties = []
        
        
    def store_datas(self) :
        candidates = self.__get_datas_from_adapters()
        self.deparment_service.manage_departments(candidates, self.department_repository)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, self.district_repository)
        self.candidate_service.manage_candidates(candidates, self.candidate_repository, self.district_service.districts)
        self.deputy_service.manage_deputies(candidates, self.candidate_service.candidates, self.deputy_repository)
        
        
    def __get_datas_from_adapters(self) : 
        candidates = [] 
        for adapter in self.adapters : 
            adapter.get_datas_needed()
            candidates = adapter.extracts_datas_from_files()
        return candidates