import pandas as pd

class Dependency: 
    def __init__(self) :
        self.__dependencies = {}
        
        
    def init_dependencies(self) :
        excel_manager = self.__load_dynamically_dependency('src.Excel.ExcelManager', 'ExcelManager')
        self.__add_dependencies("excel", excel_manager)
        
        departmentServices =  self.__load_dynamically_dependency('src.Services.DepartmentServices', 'DepartmentServices')
        self.__add_dependencies("deparmentservices", departmentServices)
        
        districtServices =  self.__load_dynamically_dependency('src.Services.DistrictServices', 'DistrictServices')
        self.__add_dependencies("districtservices", districtServices)
        
        party_service = self.__load_dynamically_dependency('src.Services.PartyServices', 'PartyServices')
        self.__add_dependencies("partyservices", party_service)
        
        mydb =  self.__load_dynamically_dependency('src.Repository.mydb', 'MyDb')
        self.__add_dependencies("mydb", mydb)     
           
        party_repository =  self.__load_dynamically_dependency('src.Repository.PartyRepository', 'PartyRepository', mydb)
        self.__add_dependencies("partyrepository", party_repository)
           
        candidate_service =  self.__load_dynamically_dependency('src.Services.CandidateServices', 'CandidateServices')
        self.__add_dependencies("candidateservices", candidate_service)
        
        result_service =  self.__load_dynamically_dependency('src.Services.ResultServices', 'ResultServices')
        self.__add_dependencies("resultservices", result_service)
        
        self.__add_adapters(pd, excel_manager, party_service, party_repository)
        
        deputy_service =  self.__load_dynamically_dependency('src.Services.DeputyServices', 'DeputyServices')
        self.__add_dependencies("deputyservices", deputy_service)
        
        district_repository = self.__load_dynamically_dependency('src.Repository.DistrictRepository', 'DistrictRepository', mydb)
        self.__add_dependencies("districtrepository",district_repository)
        
        department_repository = self.__load_dynamically_dependency('src.Repository.DepartmentRepository', 'DepartmentRepository', mydb)
        self.__add_dependencies("departmentrepository",department_repository)
        
        candidate_repository = self.__load_dynamically_dependency('src.Repository.CandidateRepository', 'CandidateRepository', mydb)
        self.__add_dependencies("candidaterepository",candidate_repository)
        
        deputy_repository = self.__load_dynamically_dependency('src.Repository.DeputyRepository', 'DeputyRepository', mydb)
        self.__add_dependencies("deputyrepository",deputy_repository)
        
        deputy_repository = self.__load_dynamically_dependency('src.Repository.ResultRepository', 'ResultRepository', mydb)
        self.__add_dependencies("resultrepository",deputy_repository)
        
        
    def __add_adapters(self, pd, excel_manager, party_service, party_repository) : 
        candidate_adapter = self.__load_dynamically_dependency('src.Adapter.CandidateAdapter', 'CandidateAdapter', pd, excel_manager, party_service, party_repository)        
        first_round_adapter = self.__load_dynamically_dependency('src.Adapter.ResultsFirstRoundAdapter', 'ResultsFirstRoundAdapter', pd,excel_manager)        
        adapters = [candidate_adapter, first_round_adapter]
        self.__add_dependencies("adapters", adapters)
        
    
    def __load_dynamically_dependency(self, module_address, name_class, *params) : 
        mod = __import__(module_address, fromlist=[name_class])
        klass = getattr(mod, name_class)
        if len(params) == 0 :
            return klass()
        else :
            return klass(*params)
        
        
    def __add_dependencies(self, key, object) :
        self.__dependencies[key] = object
        
    
    def get_dependency(self, key) : 
        return self.__dependencies[key]
    