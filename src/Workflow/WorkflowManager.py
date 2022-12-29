from src.Database import DatabaseManager

class WorkflowManager :
    def __init__(self, DatabaseManager) :
        self.DatabaseManager = DatabaseManager

    def InitWorkflowDatabase(self) :
        self.DatabaseManager.InitDatabase()