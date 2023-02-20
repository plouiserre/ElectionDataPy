import unittest
from mock import Mock
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager

class WorkflowTest(unittest.TestCase):
    #rework this TU
    def test_call_workflow_called_external_methods(self):
        departmentService_mock = Mock()
        departmentService_mock.manage_departments() 
        district_service_mock = Mock()
        district_service_mock.import_candidates_datas()
        candidate_adapter_mock = Mock()
        candidate_adapter_mock.get_candidates()
        workflow = WorkflowManager(departmentService_mock, district_service_mock, candidate_adapter_mock)        
        
        
        workflow.store_departments()
        
        self.assertTrue(departmentService_mock.manage_departments.called)
        self.assertTrue(district_service_mock.import_candidates_datas.called)
        self.assertTrue(candidate_adapter_mock.get_candidates.called)        
        
        
    if __name__ == "__main__":
        unittest.main()