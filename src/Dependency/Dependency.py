import pandas as pd

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Excel.ExcelManager import ExcelManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices
from src.Services.CandidateServices import CandidateServices
from src.Services.PartyServices import PartyServices
from src.Services.DeputyServices import DeputyServices
from src.Repository.mydb import MyDb
from src.Repository.PartyRepository import PartyRepository
from src.Repository.CandidateRepository import CandidateRepository
from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DeputyRepository import DeputyRepository
from src.Repository.DistrictRepository import DistrictRepository

class Dependency: 
    def __init__(self) :
        self.__dependencies = {}
        
        
    #TODO if it is too big split in little method
    def init_dependencies(self) :
        excel_manager = ExcelManager()
        self.__add_dependencies("excel", excel_manager)
        
        departmentServices = DepartmentServices()
        self.__add_dependencies("deparmentservices", departmentServices)
        
        districtServices = DistrictServices()
        self.__add_dependencies("districtservices", districtServices)
        
        party_service = PartyServices()        
        self.__add_dependencies("partyservices", party_service)
        
        mydb = MyDb()
        self.__add_dependencies("mydb", mydb)     
           
        party_repository = PartyRepository(mydb)
        self.__add_dependencies("partyrepository", party_repository)
           
        candidate_adapter = CandidateAdapter(pd, excel_manager, party_service, party_repository)        
        adapters = []
        adapters.append(candidate_adapter)
        self.__add_dependencies("adapters", adapters)
        
        candidate_service = CandidateServices()
        self.__add_dependencies("candidateservices", candidate_service)
        
        deputy_service = DeputyServices()
        self.__add_dependencies("deputyservices", deputy_service)
        
        district_repository = DistrictRepository(mydb)
        self.__add_dependencies("districtrepository",district_repository)
        
        department_repository = DepartmentRepository(mydb)
        self.__add_dependencies("departmentrepository",department_repository)
        
        candidate_repository = CandidateRepository(mydb)
        self.__add_dependencies("candidaterepository",candidate_repository)
        
        deputy_repository = DeputyRepository(mydb)
        self.__add_dependencies("deputyrepository",deputy_repository)
        
        
    def __add_dependencies(self, key, object) :
        self.__dependencies[key] = object
        
    #TODO 
    # -> throw exeception if key is unknown
    # -> add a unit test to check the exception
    def get_dependency(self, key) : 
        return self.__dependencies[key]
    