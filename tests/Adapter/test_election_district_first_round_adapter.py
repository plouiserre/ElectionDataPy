import unittest
from mock import Mock
from unittest.mock import patch

from src.Adapter.ElectionDistrictFirstRoundAdapter import ElectionDistrictFirstRoundAdapter
from src.Models.CandidateDataModel import CandidateDataModel
from src.Excel.ExcelManager import ExcelManager
from tests.assert_test import AssertTest

class ElectionDistrictFirstRoundAdapterTest(unittest.TestCase): 
    
    #TODO repare this UT
    # def none_candidates(self, *args) : 
    #     candidates = []
    #     return candidates
    
    # @patch.object(ExcelManager, 'import_first_round_results_datas', side_effect = none_candidates)
    # def test_excel_manager_called_in_extracts_datas_from_files(self) : 
    #     pd = Mock()
    #     adapter = ElectionDistrictFirstRoundAdapter(pd, ExcelManager)
    #     elections_first_round_datas = ElectionDistrictFirstRoundAdapter(pd, ExcelManager)
        
    #     elections_first_round_datas.extracts_datas_from_files()
        
    #     self.assertTrue(ExcelManager.import_first_round_results_datas.called)              
        
    
    def get_two_candidate_data(self, *args) : 
        candidate_first = "['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']"
        candidate_second = "['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        candidates = [candidate_first, candidate_second]
        return candidates
    
    
    @patch.object(ExcelManager, 'import_first_round_results_datas', side_effect = get_two_candidate_data)
    def test_get_two_first_round_model_from_excel_manager(self, mock_excel_manager):
        pd = Mock()
        adapter = ElectionDistrictFirstRoundAdapter(pd, ExcelManager)
        
        elections_first_round_datas = adapter.extracts_datas_from_files()        
        
        self.assertEqual(2, len(elections_first_round_datas))
        
        candidate_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3, 2, 'M', 'LAHY', 'Éric', 'DXG', 391, 0.45, 0.94, 'nan', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 9982, 11.58, 23.87, 'nan', 7, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, 1.35, 2.78, 'nan', 1, 'M', 'GUILLERMIN', 'Vincent', 'ENS', 8071, 9.36, 19.3, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 10599, 12.3, 25.35, 'nan', '5.0', 'M', 'MENDES', 'Michael', 'DSV', 641, 0.74, 1.53, 'nan', '6.0', 'M', 'BELLON', 'Julien', 'REC', 1995, 2.31, 4.77, 'nan', '4.0', 'F', 'PIROUX GIANNOTTI', 'Brigitte', 'RN', 8971, 10.41, 21.46, 'nan', 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[0], CandidateDataModel))        
        self.assertEqual(8, len(elections_first_round_datas[0].candidates))
        assert_test = AssertTest(self, 8)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[0])        
        
        candidate_data_check = [25, 'Doubs', 2, '2ème circonscription', 'Complet', 79162, 37688, 47.61, 41474, 52.39, 821, 1.04, 1.98, 326, 0.41, 0.79, 40327, 50.94, 97.23, 8, 'F', 'VUITTON', 'Brigitte', 'DXG', 779, 0.98, 1.93, 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, 16.56, 32.51, 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, 0.27, 0.54, 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, 0, 0, 'nan', 3, 'M', 'ALAUZET', 'Eric', 'ENS', 12647, 15.98, 31.36, 'nan', 1, 'F', 'KAOULAL', 'Chafia', 'LR', 4354, 5.5, 10.8, 'nan', 7, 'M', 'PRENEL', 'Jim', 'DSV', 692, 0.87, 1.72, 'nan', 5, 'F', 'CARRAU', 'Barbara', 'REC', 1472, 1.86, 3.65, 'nan', 9, 'M', 'FUSIS', 'Eric', 'RN', 7055, 8.91, 17.49, 'nan' 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[1], CandidateDataModel))
        self.assertEqual(9, len(elections_first_round_datas[1].candidates))
        assert_test = AssertTest(self, 9)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[1])    
        
        
    def get_four_candidate_data(self, *args) : 
        candidate_first = "['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']"
        candidate_second = "['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        candidate_third = "['28' 'Eure-et-Loir' 3 '3ème circonscription' 'Complet' 71342 37670 '52.8' 33672 '47.2' 523 '0.73' '1.55' 222 '0.31' '0.66' 32927 '46.15' '97.79' 8 'M' 'CHEVROLLIER' 'Vincent' 'DXG' 325 '0.46' '0.99' 'nan' 13 'F' 'LAMOUREUX' 'Aurore' 'DXG' 274 '0.38' '0.83' 'nan' 2 'F' 'ORFILA' 'Valéria' 'NUP' 6283 '8.81' '19.08' 'nan' 9 'F' 'JOLY' 'Vivette' 'ECO' 904 '1.27' '2.75' 'nan' '11.0' 'F' 'DARDABA' 'Soumaya' 'ECO' '620.0' '0.87' '1.88' 'nan' '12.0' 'F' 'BARBIER' 'Claire' 'ECO' '289.0' '0.41' '0.88' 'nan' '4.0' 'F' 'GERACI' 'Carole' 'DIV' '1705.0' '2.39' '5.18' 'nan' '5.0' 'M' 'LAMIRAULT' 'Luc' 'ENS' '9505.0' '13.32' '28.87' 'nan' '10.0' 'M' 'RIBAS' 'Romain' 'DVC' '329.0' '0.46' '1.0' 'nan' '3.0' 'M' 'MARTIAL' 'Rémi' 'LR' '2934.0' '4.11' '8.91' 'nan' '7.0' 'M' 'BOUTICOURT' 'Damien' 'DSV' '539.0' '0.76' '1.64' 'nan' '1.0' 'M' 'LAQUA' 'Éric' 'REC' '1134.0' '1.59' '3.44' 'nan' '6.0' 'F' 'FLAUNET' 'Régine' 'RN' '8086.0' '11.33' '24.56' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        candidate_fourth = "['69' 'Rhône' 6 '6ème circonscription' 'Complet' 89563 48901 '54.6' 40662 '45.4' 461 '0.51' '1.13' 136 '0.15' '0.33' 40065 '44.73' '98.53' 6 'M' 'PRIVOLT' 'Grégoire' 'DXG' 107 '0.12' '0.27' 'nan' 7 'F' 'BOUHAMI' 'Nadia' 'DXG' 347 '0.39' '0.87' 'nan' 1 'F' 'BUISSON' 'Katia' 'RDG' 2632 '2.94' '6.57' 'nan' 14 'M' 'AMARD' 'Gabriel' 'NUP' 16545 '18.47' '41.3' 'nan' '9.0' 'F' 'ROCHE' 'Ingrid' 'ECO' '490.0' '0.55' '1.22' 'nan' '12.0' 'M' 'MEZIANI' 'Zaïr' 'ECO' '720.0' '0.8' '1.8' 'nan' '3.0' 'M' 'RYCKAERT' 'Paul' 'DIV' '28.0' '0.03' '0.07' 'nan' '8.0' 'F' 'BOUTAYEB' 'Maude' 'DIV' '224.0' '0.25' '0.56' 'nan' '15.0' 'M' 'VIEIRA' 'Philippe' 'DIV' '684.0' '0.76' '1.71' 'nan' '4.0' 'F' 'WINKERMULLER' 'Laura' 'REG' '183.0' '0.2' '0.46' 'nan' '13.0' 'F' 'HAZIZA' 'Emmanuelle' 'ENS' '10777.0' '12.03' '26.9' 'nan' '2.0' 'M' 'SENDE' 'Jean-Eric' 'DVC' '526.0' '0.59' '1.31' 'nan' '5.0' 'M' 'CHARLIEU' 'Clément' 'UDI' '700.0' '0.78' '1.75' 'nan' '11.0' 'M' 'PORTA' 'Pierre' 'REC' '1774.0' '1.98' '4.43' 'nan' '10.0' 'F' 'MOREL' 'Michèle' 'RN' '4328.0' '4.83' '10.8' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        candidates = [candidate_first, candidate_second, candidate_third, candidate_fourth]
        return candidates
        
    @patch.object(ExcelManager, 'import_first_round_results_datas', side_effect = get_four_candidate_data)
    def test_get_fourth_first_round_model_from_excel_manager(self, mock_excel_manager):
        pd = Mock()
        adapter = ElectionDistrictFirstRoundAdapter(pd, ExcelManager)
        
        elections_first_round_datas = adapter.extracts_datas_from_files()
        
        self.assertEqual(4, len(elections_first_round_datas))
        
        candidate_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3, 2, 'M', 'LAHY', 'Éric', 'DXG', 391, 0.45, 0.94, 'nan', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 9982, 11.58, 23.87, 'nan', 7, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, 1.35, 2.78, 'nan', 1, 'M', 'GUILLERMIN', 'Vincent', 'ENS', 8071, 9.36, 19.3, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 10599, 12.3, 25.35, 'nan', '5.0', 'M', 'MENDES', 'Michael', 'DSV', 641, 0.74, 1.53, 'nan', '6.0', 'M', 'BELLON', 'Julien', 'REC', 1995, 2.31, 4.77, 'nan', '4.0', 'F', 'PIROUX GIANNOTTI', 'Brigitte', 'RN', 8971, 10.41, 21.46, 'nan', 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[0], CandidateDataModel))        
        assert_test = AssertTest(self, 8)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[0])        
        
        candidate_data_check = [25, 'Doubs', 2, '2ème circonscription', 'Complet', 79162, 37688, 47.61, 41474, 52.39, 821, 1.04, 1.98, 326, 0.41, 0.79, 40327, 50.94, 97.23, 8, 'F', 'VUITTON', 'Brigitte', 'DXG', 779, 0.98, 1.93, 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, 16.56, 32.51, 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, 0.27, 0.54, 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, 0, 0, 'nan', 3, 'M', 'ALAUZET', 'Eric', 'ENS', 12647, 15.98, 31.36, 'nan', 1, 'F', 'KAOULAL', 'Chafia', 'LR', 4354, 5.5, 10.8, 'nan', 7, 'M', 'PRENEL', 'Jim', 'DSV', 692, 0.87, 1.72, 'nan', 5, 'F', 'CARRAU', 'Barbara', 'REC', 1472, 1.86, 3.65, 'nan', 9, 'M', 'FUSIS', 'Eric', 'RN', 7055, 8.91, 17.49, 'nan' 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[1], CandidateDataModel))
        assert_test = AssertTest(self, 9)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[1])    
        
        candidate_data_check = [28, 'Eure-et-Loir', 3, '3ème circonscription', 'Complet', 71342, 37670, 52.8, 33672, 47.2, 523, 0.73, 1.55, 222, 0.31, 0.66, 32927, 46.15, 97.79, 8, 'M', 'CHEVROLLIER', 'Vincent', 'DXG', 325, 0.46, 0.99, 'nan', 13, 'F', 'LAMOUREUX', 'Aurore', 'DXG', 274, 0.38, 0.83, 'nan', 2, 'F', 'ORFILA', 'Valéria', 'NUP', 6283, 8.81, 19.08, 'nan', 9, 'F', 'JOLY', 'Vivette', 'ECO', 904, 1.27, 2.75, 'nan', 11, 'F', 'DARDABA', 'Soumaya', 'ECO', 620, 0.87, 1.88, 'nan', 12, 'F', 'BARBIER', 'Claire', 'ECO', 289, 0.41, 0.88, 'nan', 4, 'F', 'GERACI', 'Carole', 'DIV', 1705, 2.39, 5.18, 'nan', 5, 'M', 'LAMIRAULT', 'Luc', 'ENS', 9505, 13.32, 28.87, 'nan', 10, 'M', 'RIBAS', 'Romain', 'DVC', 329, 0.46, 1, 'nan', 3, 'M', 'MARTIAL', 'Rémi', 'LR', 2934, 4.11, 8.91, 'nan', 7, 'M', 'BOUTICOURT', 'Damien', 'DSV', 539, 0.76, 1.64, 'nan', 1, 'M', 'LAQUA', 'Éric', 'REC', 1134, 1.59, 3.44, 'nan', 6, 'F', 'FLAUNET', 'Régine', 'RN', 8086, 11.33, 24.56, 'nan', 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[2], CandidateDataModel))
        assert_test = AssertTest(self, 13)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[2])        
        
        candidate_data_check = [69, 'Rhône', 6, '6ème circonscription', 'Complet', 89563, 48901, 54.6, 40662, 45.4, 461, 0.51, 1.13, 136, 0.15, 0.33, 40065, 44.73, 98.53, 6, 'M', 'PRIVOLT', 'Grégoire', 'DXG', 107, 0.12, 0.27, 'nan', 7, 'F', 'BOUHAMI', 'Nadia', 'DXG', 347, 0.39, 0.87, 'nan', 1, 'F', 'BUISSON', 'Katia', 'RDG', 2632, 2.94, 6.57, 'nan', 14, 'M', 'AMARD', 'Gabriel', 'NUP', 16545, 18.47, 41.3, 'nan', 9, 'F', 'ROCHE', 'Ingrid', 'ECO', 490, 0.55, 1.22, 'nan', 12, 'M', 'MEZIANI', 'Zaïr', 'ECO', 720, 0.8, 1.8, 'nan', 3, 'M', 'RYCKAERT', 'Paul', 'DIV', 28, 0.03, 0.07, 'nan', 8, 'F', 'BOUTAYEB', 'Maude', 'DIV', 224, 0.25, 0.56, 'nan', 15, 'M', 'VIEIRA', 'Philippe', 'DIV', 684, 0.76, 1.71, 'nan', 4, 'F', 'WINKERMULLER', 'Laura', 'REG', 183, 0.2, 0.46, 'nan', 13, 'F', 'HAZIZA', 'Emmanuelle', 'ENS', 10777, 12.03, 26.9, 'nan', 2, 'M', 'SENDE', 'Jean-Eric', 'DVC', 526, 0.59, 1.31, 'nan', 5, 'M', 'CHARLIEU', 'Clément', 'UDI', 700, 0.78, 1.75, 'nan', 11, 'M', 'PORTA', 'Pierre', 'REC', 1774, 1.98, 4.43, 'nan', 10, 'F', 'MOREL', 'Michèle', 'RN', 4328, 4.83, 10.8, 'nan', 'nan']
        self.assertTrue(isinstance(elections_first_round_datas[3], CandidateDataModel))
        assert_test = AssertTest(self, 15)        
        assert_test.assert_candidate_data_model_from_first_round_election(candidate_data_check, elections_first_round_datas[3])