import pandas as pd


from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices

fileManager = FileManager()
departmentServices = DepartmentServices()
districtServices = DistrictServices()
workflow = WorkflowManager(fileManager, departmentServices, districtServices, pd)
workflow.store_departments()