import pandas as pd

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Excel.ExcelManager import ExcelManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices
from src.Services.CandidateServices import CandidateServices
from src.Services.PartyServices import PartyServices
from src.Services.DeputyServices import DeputyServices
from src.Workflow.WorkflowManager import WorkflowManager
from src.Repository.mydb import MyDb
from src.Repository.PartyRepository import PartyRepository

excel_manager = ExcelManager()
departmentServices = DepartmentServices()
districtServices = DistrictServices()
party_service = PartyServices()
mydb = MyDb()        
party_repository = PartyRepository(mydb)
candidate_adapter = CandidateAdapter(pd, excel_manager, party_service, party_repository)
candidate_service = CandidateServices()
deputy_service = DeputyServices()
adapters = []
adapters.append(candidate_adapter)
workflow = WorkflowManager(departmentServices, districtServices, adapters, candidate_service, deputy_service, mydb)
workflow.store_datas()