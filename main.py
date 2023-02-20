import pandas as pd

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Excel.ExcelManager import ExcelManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices
from src.Workflow.WorkflowManager import WorkflowManager

excel_manager = ExcelManager()
departmentServices = DepartmentServices()
districtServices = DistrictServices()
candidate_adapter = CandidateAdapter(pd, excel_manager)
workflow = WorkflowManager(departmentServices, districtServices, candidate_adapter)
workflow.store_departments()