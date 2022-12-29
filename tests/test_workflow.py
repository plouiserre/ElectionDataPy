import unittest
import mock
from mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Database.DatabaseManager import DatabaseManager

class WorkflowTest(unittest.TestCase):

    @patch.object(DatabaseManager,'InitDatabase')
    def test_call_database_creation(self, mock_databaseManager):
        workflow = WorkflowManager(DatabaseManager)
        
        workflow.InitWorkflowDatabase()
        
        self.assertTrue(mock_databaseManager.called)

    if __name__ == "__main__":
        unittest.main()