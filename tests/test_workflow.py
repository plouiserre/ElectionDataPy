import unittest
from mock import Mock
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager
from src.Files.FileManager import FileManager
from src.Services.DepartmentServices import DepartmentServices
from src.Services.DistrictServices import DistrictServices

class WorkflowTest(unittest.TestCase):
    #TODO check if I can divide this test in three tests
    def test_call_workflow_called_external_methods(self):
        workflow = WorkflowManager()
        
        filemanager_mock = Mock()
        filemanager_mock.import_candidates_datas()
        departmentService_mock = Mock()
        departmentService_mock.manage_departments() 
        district_service_mock = Mock()
        district_service_mock.import_candidates_datas()
        
        workflow.store_departments(filemanager_mock, departmentService_mock, district_service_mock)
        
        self.assertTrue(filemanager_mock.import_candidates_datas.called)
        self.assertTrue(departmentService_mock.manage_departments.called)
        self.assertTrue(district_service_mock.import_candidates_datas.called)
        
        
    if __name__ == "__main__":
        unittest.main()
        
    #TODO in workflowmanager improve test to fail with this stupide code 
    '''   
    department_repository = DepartmentRepository()
        candidates = fileManager.import_candidates_datas()
        departmentService.manage_departments(candidates, department_repository)
        districtService.manage_districts()
    '''