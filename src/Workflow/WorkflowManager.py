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
        
    #TODO externalize all repository thing in the constructor
    def store_departments(self) :
        mydb = MyDb()
        department_repository = DepartmentRepository(mydb)
        district_repository = DistrictRepository(mydb)
        party_repository = PartyRepository(mydb)
        candidate_repository = CandidateRepository(mydb)
        parties = self.party_service.load_parties(party_repository)
        candidates = self.candidate_adapter.get_candidates(parties)
        self.deparment_service.manage_departments(candidates, department_repository)
        self.district_service.manage_districts(candidates, self.deparment_service.departments, district_repository)
        self.candidate_service.manage_candidates(candidates, candidate_repository)