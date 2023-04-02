import unittest
from unittest.mock import patch
from mock import Mock
from src.Workflow.WorkflowManager import WorkflowManager
from src.Dependency.Dependency import Dependency

#TODO how to test if the calls externs are bad formated
class WorkflowTest(unittest.TestCase):
    
    def getIterablesObject(*args) : 
        arrays = []
        return arrays
    
    @patch.object(Dependency,'get_dependency', side_effect=getIterablesObject)
    def test_call_workflow_called_external_methods(self, mock_dependency):
        workflow = WorkflowManager(mock_dependency)                
        
        workflow.store_datas()
        
        self.assertTrue(mock_dependency.get_dependency.called)
        
    if __name__ == "__main__":
        unittest.main()