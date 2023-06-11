from mock import Mock
import unittest
from unittest.mock import patch

from src.Adapter.ResultsSecondRoundAdapter import ResultsSecondRoundAdapter
from src.Excel.ExcelManager import ExcelManager

class ResultSecondRoundAdapter(unittest.TestCase) : 
    
    @patch.object(ExcelManager, 'import_second_round_results_datas')
    def test_excel_manager_called_in_extracts_datas_from_files(self, mock_excel_manager) :
        mock_excel_manager.import_second_round_results_datas.return_value = ''
        pd = Mock()
        
        elections_second_round_datas = ResultsSecondRoundAdapter(pd, mock_excel_manager)
        elections_second_round_datas.extracts_datas_from_files()
        
        self.assertTrue(mock_excel_manager.import_second_round_results_datas.called)   