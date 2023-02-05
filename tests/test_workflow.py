import unittest
from mock import Mock
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices

class WorkflowTest(unittest.TestCase):
    def test_call_workflow_called_external_methods(self):
        filemanager_mock = Mock()
        filemanager_mock.import_candidates_datas()
        departmentService_mock = Mock()
        departmentService_mock.manage_departments() 
        district_service_mock = Mock()
        district_service_mock.import_candidates_datas()
        panda_mock = Mock()
        workflow = WorkflowManager(filemanager_mock, departmentService_mock, district_service_mock, panda_mock)        
        
        
        workflow.store_departments()
        
        self.assertTrue(filemanager_mock.import_candidates_datas.called)
        self.assertTrue(departmentService_mock.manage_departments.called)
        self.assertTrue(district_service_mock.import_candidates_datas.called)
        
        
    if __name__ == "__main__":
        unittest.main()