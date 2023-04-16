import unittest
from mock import Mock

from src.Adapter.FirstRoundAdapter import FirstRoundAdapter

class FirstRoundAdapterTest(unittest.TestCase) :
    def test_excel_manager_called_in_extracts_datas_from_files(self) : 
        excel_manager_mock = Mock()
        panda_lib_mock = Mock()
        first_round_adapter = FirstRoundAdapter(panda_lib_mock, excel_manager_mock)
        
        first_round_adapter.extracts_datas_from_files()
        
        self.assertTrue(excel_manager_mock.import_first_round_results_datas.called)        
        
        
        