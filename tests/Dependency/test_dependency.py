import unittest

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Adapter.ElectionDistrictFirstRoundAdapter import ElectionDistrictFirstRoundAdapter
from src.Dependency.Dependency import Dependency
from src.Excel.ExcelManager import ExcelManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices
from src.Services.PartyServices import PartyServices
from src.Services.CandidateServices import CandidateServices
from src.Services.DeputyServices import DeputyServices
from src.Repository.PartyRepository import PartyRepository
from src.Repository.CandidateRepository import CandidateRepository
from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.DeputyRepository import DeputyRepository
from src.Repository.DistrictRepository import DistrictRepository


#TODO ajouter un test pour electiondistrictfirstroundadapter
class DependencyTest(unittest.TestCase) : 
    def test_get_excel_dependency(self) : 
        dependency = self.__get_dependencies_to_test("excel")
        
        self.assertTrue(isinstance(dependency, ExcelManager))
        
        
    def test_get_department_service_dependency(self) : 
        dependency = self.__get_dependencies_to_test("deparmentservices")
        
        self.assertTrue(isinstance(dependency, DepartmentServices))
        
        
    def test_get_district_service_dependency(self) : 
        dependency = self.__get_dependencies_to_test("districtservices")
        
        self.assertTrue(isinstance(dependency, DistrictServices))
        
        
    def test_get_party_service_dependency(self) : 
        dependency = self.__get_dependencies_to_test("partyservices")
        
        self.assertTrue(isinstance(dependency, PartyServices))
        
        
    def test_get_party_repository_dependency(self) : 
        dependency = self.__get_dependencies_to_test("partyrepository")
        
        self.assertTrue(isinstance(dependency, PartyRepository))
        
        
    def test_get_candidate_service_dependency(self) : 
        dependency = self.__get_dependencies_to_test("candidateservices")
        
        self.assertTrue(isinstance(dependency, CandidateServices))
        
        
    def test_get_deputy_service_dependency(self) : 
        dependency = self.__get_dependencies_to_test("deputyservices")
        
        self.assertTrue(isinstance(dependency, DeputyServices))
        
        
    def test_get_candidate_repository_dependency(self) : 
        dependency = self.__get_dependencies_to_test("candidaterepository")
        
        self.assertTrue(isinstance(dependency, CandidateRepository))
        
        
    def test_get_department_repository_dependency(self) : 
        dependency = self.__get_dependencies_to_test("departmentrepository")
        
        self.assertTrue(isinstance(dependency, DepartmentRepository))
        
        
    def test_get_deputy_repository_dependency(self) : 
        dependency = self.__get_dependencies_to_test("deputyrepository")
        
        self.assertTrue(isinstance(dependency, DeputyRepository))
        
        
    def test_get_district_repository_dependency(self) : 
        dependency = self.__get_dependencies_to_test("districtrepository")
        
        self.assertTrue(isinstance(dependency, DistrictRepository))
        
        
    def test_get_adapters_dependency(self) : 
        dependency = self.__get_dependencies_to_test("adapters")
        
        self.assertEqual(2, len(dependency))        
        self.assertTrue(isinstance(dependency[0], CandidateAdapter))
        self.assertTrue(isinstance(dependency[1], ElectionDistrictFirstRoundAdapter))
        
        
    def __get_dependencies_to_test(self, key) : 
        dep = Dependency()        
        dep.init_dependencies()
        dependency = dep.get_dependency(key)
        return dependency
        