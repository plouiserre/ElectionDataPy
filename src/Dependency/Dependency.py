import pandas as pd

class Dependency: 
    def __init__(self) :
        self.__dependencies = {}
        
        
    #TODO if it is too big split in little method
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
           
        candidate_adapter = self.__load_dynamically_dependency('src.Adapter.CandidateAdapter', 'CandidateAdapter', pd, excel_manager, party_service, party_repository)        
        self.__add_dependencies("candidateadapter", candidate_adapter)
        
        candidate_service =  self.__load_dynamically_dependency('src.Services.CandidateServices', 'CandidateServices')
        self.__add_dependencies("candidateservices", candidate_service)
        
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
        
    
    def __load_dynamically_dependency(self, module_address, name_class, *params) : 
        mod = __import__(module_address, fromlist=[name_class])
        klass = getattr(mod, name_class)
        if len(params) == 0 :
            return klass()
        else :
            return klass(*params)
        
        
    def __add_dependencies(self, key, object) :
        self.__dependencies[key] = object
        
    #TODO 
    # -> throw exeception if key is unknown
    # -> add a unit test to check the exception
    def get_dependency(self, key) : 
        return self.__dependencies[key]
    