import unittest
#import mock
from mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager

class WorkflowTest(unittest.TestCase):

    @patch.object(FileManager,'ImportCandidatesDatas')
    def test_call_database_creation(self, mock_filemanager):
        workflow = WorkflowManager()
        
        workflow.StoreDepartments(FileManager)
        
        self.assertTrue(mock_filemanager.called)
        
    if __name__ == "__main__":
        unittest.main()