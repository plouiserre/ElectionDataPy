import unittest
from mock import Mock
from unittest.mock import patch
from src.Workflow.WorkflowManager import WorkflowManager

#TODO reprendre ce code car le TU marche mal
class WorkflowTest(unittest.TestCase):
    
    def test_call_workflow_called_external_methods(self):
        departmentService_mock = Mock()
        departmentService_mock.manage_departments() 
        district_service_mock = Mock()
        district_service_mock.import_candidates_datas()
        candidate_adapter_mock = Mock()
        candidate_adapter_mock.get_candidates()
        adapters = []
        adapters.append(candidate_adapter_mock)
        candidate_service_mock = Mock()
        candidate_service_mock.manage_candidates()
        deputy_service_mock = Mock()
        deputy_service_mock.manage_deputies()
        mydb_mock = Mock()
        workflow = WorkflowManager(departmentService_mock, district_service_mock, adapters, candidate_service_mock, deputy_service_mock, mydb_mock)                
        
        workflow.store_datas()
        
        self.assertTrue(departmentService_mock.manage_departments.called)
        self.assertTrue(district_service_mock.import_candidates_datas.called)
        self.assertTrue(candidate_adapter_mock.get_candidates.called)        
        self.assertTrue(candidate_service_mock.manage_candidates.called)
        
    if __name__ == "__main__":
        unittest.main()