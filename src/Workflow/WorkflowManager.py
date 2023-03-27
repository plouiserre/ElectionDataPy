from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DistrictRepository import DistrictRepository
from src.Repository.PartyRepository import PartyRepository
from src.Repository.CandidateRepository import CandidateRepository
from src.Repository.mydb import MyDb

class WorkflowManager :
    def __init__(self, departmentService, districtService, candidate_adapter, candidate_service, party_service) :
        self.deparment_service = departmentService
        self.district_service = districtService
        self.candidate_adapter = candidate_adapter
        self.candidate_service = candidate_service
        self.party_service = party_service
        mydb = MyDb()
        self.department_repository = DepartmentRepository(mydb)
        self.district_repository = DistrictRepository(mydb)
        self.party_repository = PartyRepository(mydb)
        self.candidate_repository = CandidateRepository(mydb)
        
        
    def store_departments(self) :
        parties = self.party_service.load_parties(self.party_repository)
        candidates = self.candidate_adapter.get_candidates(parties)
        self.deparment_service.manage_departments(candidates, self.department_repository)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, self.district_repository)
        self.candidate_service.manage_candidates(candidates, self.candidate_repository)