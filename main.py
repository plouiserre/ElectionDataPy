import pandas as pd


from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices

#TODO check if we can improve the import of this file
#TODO put in constructor the arguments of the method

fileManager = FileManager()
workflow = WorkflowManager()
departmentServices = DepartmentServices()
districtServices = DistrictServices()
workflow.store_departments(fileManager, departmentServices, districtServices, pd)