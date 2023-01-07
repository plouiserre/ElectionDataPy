import unittest
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices

class WorkflowTest(unittest.TestCase):
    @patch.object(FileManager,'ImportCandidatesDatas')
    @patch.object(DepartmentServices,'Manage_Departments')
    def test_call_workflow_called_external_methods(self, mock_filemanager, mock_departmentservice):
        workflow = WorkflowManager()
        
        workflow.StoreDepartments(FileManager, DepartmentServices)
        
        self.assertTrue(mock_filemanager.called)
        self.assertTrue(mock_departmentservice.called)
        
    if __name__ == "__main__":
        unittest.main()