from src.Workflow.WorkflowManager import WorkflowManager
from src.Database.DatabaseManager import DatabaseManager

database = DatabaseManager()
workflow = WorkflowManager(database)
workflow.InitWorkflowDatabase()