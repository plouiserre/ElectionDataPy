from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager

#TODO modify methods names to correspond standards
fileManager = FileManager()
workflow = WorkflowManager()
workflow.StoreDepartments(fileManager)

