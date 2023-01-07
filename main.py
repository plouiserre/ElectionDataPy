from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices

#TODO modify methods names to correspond standards
fileManager = FileManager()
workflow = WorkflowManager()
departmentServices = DepartmentServices()
workflow.StoreDepartments(fileManager, departmentServices)

