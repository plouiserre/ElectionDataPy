from mock import Mock
import unittest
from unittest.mock import patch

from src.Adapter.ResultsSecondRoundAdapter import ResultsSecondRoundAdapter
from src.Excel.ExcelManager import ExcelManager
from src.Models.ElectionDataModel import ElectionDataModel
from tests.assert_test import AssertTest

class ResultSecondRoundAdapterTest(unittest.TestCase) : 
    
    @patch.object(ExcelManager, 'import_second_round_results_datas')
    def test_excel_manager_called_in_extracts_datas_from_files(self, mock_excel_manager) :
        mock_excel_manager.import_second_round_results_datas.return_value = ''
        pd = Mock()
        
        elections_second_round_datas = ResultsSecondRoundAdapter(pd, mock_excel_manager)
        elections_second_round_datas.extracts_datas_from_files()
        
        self.assertTrue(mock_excel_manager.import_second_round_results_datas.called)
        
      
    def get_three_election_datas_from_first_district_ain(self, *args) :
        election_first = "['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_second = "['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_third = "['01' 'Ain' 1 '1ère circonscription' 29 'Beaupont' 'Complet' 446 239 '53.59' 207 '46.41' 10 '2.24' '4.83' 2 '0.45' '0.97' 195 '43.72' '94.2' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 67 '15.02' '34.36' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '128.0' '28.7' '65.64' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        elections = [election_first, election_second, election_third]
        return elections
    
    
    @patch.object(ExcelManager, 'import_second_round_results_datas', side_effect = get_three_election_datas_from_first_district_ain)
    def test_from_four_second_round_result_same_district_get_one_election_data_model(self, mock_excel_manager):
        pd= Mock()
        adapter = ResultsSecondRoundAdapter(pd, ExcelManager)
        
        result_second_round_datas = adapter.extracts_datas_from_files()  
        
        self.assertEqual(1, len(result_second_round_datas))
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 218, 15.35, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 398, 29.283, 65.64, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check, result_second_round_datas[0])
        
    
    def get_four_election_datas_from_two_departments(self, *args) : 
        election_first = "['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_second = "['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_third = "['01' 'Ain' 1 '1ère circonscription' 29 'Beaupont' 'Complet' 446 239 '53.59' 207 '46.41' 10 '2.24' '4.83' 2 '0.45' '0.97' 195 '43.72' '94.2' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 67 '15.02' '34.36' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '128.0' '28.7' '65.64' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_fourth = "['02' 'Aisne' 1 '1ère circonscription' 2 'Achery' 'Complet' 444 247 '55.63' 197 '44.37' 12 '2.7' '6.09' 2 '0.45' '1.02' 183 '41.22' '92.89' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 63 '14.19' '34.43' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '120.0' '27.03' '65.57' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        elections = [election_first, election_second, election_third, election_fourth]
        return elections
        
    @patch.object(ExcelManager, 'import_second_round_results_datas', side_effect = get_four_election_datas_from_two_departments)   
    def test_from_three_second_result_ain_and_one_aisne_get_two_election_data_model(self, mock_excel_manager) : 
        pd= Mock()
        adapter = ResultsSecondRoundAdapter(pd, ExcelManager)
        
        result_second_round_datas = adapter.extracts_datas_from_files()  
        
        self.assertEqual(2, len(result_second_round_datas))
        
        election_data_check_ain_department = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 218, 15.35, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 398, 29.283, 65.64, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_ain_department, result_second_round_datas[0])
        
        
        election_data_check_aisne_department = [2, 'Aisne', 1, '1ère circonscription', 'Complet', 2, 444, 247, 55.63, 197, 44.37, 12, 2.7, 6.09, 2, 0.45, 1.02, 183, 41.22, 92.89, 1,  'F', 'BONO-VANDORME', 'Aude', 'ENS', 63, 14.19, 34.43, 'nan', '7.0', 'M', 'DRAGON', 'Nicolas', 'RN', 120, 27.03, 65.57, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_aisne_department, result_second_round_datas[1])
        
        
    def get_five_election_datas_from_two_departments(self, *args) : 
        election_first = "['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_second = "['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_third = "['01' 'Ain' 1 '1ère circonscription' 29 'Beaupont' 'Complet' 446 239 '53.59' 207 '46.41' 10 '2.24' '4.83' 2 '0.45' '0.97' 195 '43.72' '94.2' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 67 '15.02' '34.36' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '128.0' '28.7' '65.64' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_fourth = "['02' 'Aisne' 1 '1ère circonscription' 2 'Achery' 'Complet' 444 247 '55.63' 197 '44.37' 12 '2.7' '6.09' 2 '0.45' '1.02' 183 '41.22' '92.89' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 63 '14.19' '34.43' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '120.0' '27.03' '65.57' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_fifth = "['02' 'Aisne' 1 '1ère circonscription' 5 'Aguilcourt' 'Complet' 315 152 '48.25' 163 '51.75' 7 '2.22' '4.29' 3 '0.95' '1.84' 153 '48.57' '93.87' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 57 '18.1' '37.25' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '96.0' '30.48' '62.75' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        elections = [election_first, election_second, election_third, election_fourth, election_fifth]
        return elections
    
    @patch.object(ExcelManager, 'import_second_round_results_datas', side_effect = get_five_election_datas_from_two_departments)   
    def test_from_three_second_result_ain_and_two_aisne_get_two_election_data_model(self, mock_excel_manager) : 
        pd= Mock()
        adapter = ResultsSecondRoundAdapter(pd, ExcelManager)
        
        result_second_round_datas = adapter.extracts_datas_from_files()  
        
        self.assertEqual(2, len(result_second_round_datas))
        
        election_data_check_ain_department = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 218, 15.35, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 398, 29.283, 65.64, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_ain_department, result_second_round_datas[0])
        
        
        election_data_check_aisne_department = [2, 'Aisne', 1, '1ère circonscription', 'Complet', 2, 759, 399, 51.94, 360, 48.06, 19, 2.46, 5.19, 5, 0.7, 1.43, 336, 44.895, 93.38, 1,  'F', 'BONO-VANDORME', 'Aude', 'ENS', 120, 16.145, 35.84, 'nan', '7.0', 'M', 'DRAGON', 'Nicolas', 'RN', 216, 28.755, 64.16, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_aisne_department, result_second_round_datas[1])
        
        
    def get_six_election_datas_from_three_departments(self, *args) : 
        election_first = "['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_second = "['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_third = "['01' 'Ain' 1 '1ère circonscription' 29 'Beaupont' 'Complet' 446 239 '53.59' 207 '46.41' 10 '2.24' '4.83' 2 '0.45' '0.97' 195 '43.72' '94.2' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 67 '15.02' '34.36' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '128.0' '28.7' '65.64' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_fourth = "['02' 'Aisne' 1 '1ère circonscription' 2 'Achery' 'Complet' 444 247 '55.63' 197 '44.37' 12 '2.7' '6.09' 2 '0.45' '1.02' 183 '41.22' '92.89' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 63 '14.19' '34.43' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '120.0' '27.03' '65.57' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_fifth = "['02' 'Aisne' 1 '1ère circonscription' 5 'Aguilcourt' 'Complet' 315 152 '48.25' 163 '51.75' 7 '2.22' '4.29' 3 '0.95' '1.84' 153 '48.57' '93.87' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 57 '18.1' '37.25' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '96.0' '30.48' '62.75' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        election_sixth = "['38' 'Isère' 2 '2ème circonscription' 188 'Herbeys' 'Complet' 1172 425 '36.26' 747 '63.74' 25 '2.13' '3.35' 8 '0.68' '1.07' 714 '60.92' '95.58' 1 'F' 'CHATELAIN' 'Cyrielle' 'NUP' 285 '24.32' '39.92' '9.0' 'M' 'COLAS-ROY' 'Jean-Charles' 'ENS' '429.0' '36.6' '60.08' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        elections = [election_first, election_second, election_third, election_fourth, election_fifth, election_sixth]
        return elections
        
    @patch.object(ExcelManager, 'import_second_round_results_datas', side_effect = get_six_election_datas_from_three_departments)   
    def test_from_three_second_result_ain_two_aisne_and_one_isere_get_two_election_data_model(self, mock_excel_manager) : 
        pd= Mock()
        adapter = ResultsSecondRoundAdapter(pd, ExcelManager)
        
        result_second_round_datas = adapter.extracts_datas_from_files()  
        
        self.assertEqual(3, len(result_second_round_datas))
        
        election_data_check_ain_department = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 218, 15.35, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 398, 29.283, 65.64, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_ain_department, result_second_round_datas[0])
        
        election_data_check_aisne_department = [2, 'Aisne', 1, '1ère circonscription', 'Complet', 2, 759, 399, 51.94, 360, 48.06, 19, 2.46, 5.19, 5, 0.7, 1.43, 336, 44.895, 93.38, 1,  'F', 'BONO-VANDORME', 'Aude', 'ENS', 120, 16.145, 35.84, 'nan', '7.0', 'M', 'DRAGON', 'Nicolas', 'RN', 216, 28.755, 64.16, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_aisne_department, result_second_round_datas[1])
        
        election_data_check_isere_department = [38, 'Isère', 2, '2ème circonscription', 'Complet', 2, 1172, 425, 36.26, 747, 63.74, 25, 2.13, 3.35, 8, 0.68, 1.07, 714, 60.92, 95.58, 1, 'F', 'CHATELAIN', 'Cyrielle', 'NUP', 285, 24.32, 39.92, 'nan', '9.0', 'M', 'COLAS-ROY', 'Jean-Charles', 'ENS', 429, 36.6, 60.08, 'nan', 'nan']
        self.assertTrue(isinstance(result_second_round_datas[0], ElectionDataModel))        
        self.assertEqual(2, len(result_second_round_datas[0].candidates))
        assert_test = AssertTest(self, 2)        
        assert_test.assert_election_data_model_second_round_result(election_data_check_isere_department, result_second_round_datas[2])