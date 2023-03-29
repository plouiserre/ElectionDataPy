import pandas as pd

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Excel.ExcelManager import ExcelManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices
from src.Services.CandidateServices import CandidateServices
from src.Services.PartyServices import PartyServices
from src.Services.DeputyServices import DeputyServices
from src.Workflow.WorkflowManager import WorkflowManager

excel_manager = ExcelManager()
departmentServices = DepartmentServices()
districtServices = DistrictServices()
candidate_adapter = CandidateAdapter(pd, excel_manager)
candidate_service = CandidateServices()
party_service = PartyServices()
deputy_service = DeputyServices()
workflow = WorkflowManager(departmentServices, districtServices, candidate_adapter, candidate_service, deputy_service, party_service)
workflow.store_departments()