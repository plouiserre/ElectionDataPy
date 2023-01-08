from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices

fileManager = FileManager()
workflow = WorkflowManager()
departmentServices = DepartmentServices()
workflow.store_departments(fileManager, departmentServices)