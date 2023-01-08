import unittest
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices

class WorkflowTest(unittest.TestCase):
    @patch.object(FileManager,'import_candidates_datas')
    @patch.object(DepartmentServices,'manage_departments')
    def test_call_workflow_called_external_methods(self, mock_filemanager, mock_departmentservice):
        workflow = WorkflowManager()
        
        workflow.store_departments(FileManager, DepartmentServices)
        
        self.assertTrue(mock_filemanager.called)
        self.assertTrue(mock_departmentservice.called)
        
    if __name__ == "__main__":
        unittest.main()