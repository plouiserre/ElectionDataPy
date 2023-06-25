import datetime
import unittest
from unittest.mock import patch


from helper_test import HelperTest
from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Adapter.ResultsFirstRoundAdapter import ResultsFirstRoundAdapter
from src.Adapter.ResultsSecondRoundAdapter import ResultsSecondRoundAdapter
from src.Dependency.Dependency import Dependency
from src.Models.ElectionDataModel import ElectionDataModel
from src.Orchestrate.OrchestrateAdapters import OrchestrateAdapters
from tests.assert_test import AssertTest

class OrchestrateStoreAdaptersTest(unittest.TestCase):
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_two_elections_datas_from_adapters_list_first_rounds(self, mock_dependency, mock_candidate_adapter, mock_result_district_first_round_adapter) :        
        helper = HelperTest()
        
        mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_two_elections_data_model()
        mock_result_district_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_two_candidates()             
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_result_district_first_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate_all_data = candidates[0]        
        second_candidates_all_data = candidates[1]
        
        self.assertEqual(2, len(candidates))
        
        assert_test = AssertTest(self, 1)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, second_candidates_all_data)
        
        
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsSecondRoundAdapter, 'extracts_datas_from_files')
    def test_get_two_elections_datas_from_adapters_list_first_second_rounds(self, mock_dependency, mock_candidate_adapter, mock_result_first_round_adapter, mock_result_second_round_adapter) :        
        helper = HelperTest()
        
        mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_two_elections_data_model()
        mock_result_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_two_candidates()             
        mock_result_second_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_second_round_adapter_two_candidates()
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_result_first_round_adapter, mock_result_second_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate_all_data = candidates[0]        
        second_candidates_all_data = candidates[1]
        
        self.assertEqual(2, len(candidates))
        
        assert_test = AssertTest(self, 2)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, 21463213, 36.65, 19.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042, "Completed", 2, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, 9014651432, 63.05, 38.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032, "Completed", 2, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, second_candidates_all_data)        
    
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsSecondRoundAdapter, 'extracts_datas_from_files')
    def test_get_four_elections_datas_from_adapters_list_first_second_rounds(self, mock_dependency, mock_candidate_adapter, mock_results_first_round_adapter, mock_result_second_round_adapter) :        
        helper = HelperTest()
        
        mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_candidate_adapter_four_candidates()
        mock_results_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_four_candidates()             
        mock_result_second_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_second_round_adapter_four_candidates()
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_results_first_round_adapter, mock_result_second_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()     
        
        first_candidate_all_data = candidates[0]
        second_candidates_all_data = candidates[1]
        third_candidate_all_data = candidates[2]
        fourth_candidate_all_data = candidates[3]
        
        self.assertEqual(4, len(candidates))
        
        assert_test = AssertTest(self, 1)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, 21463213, 36.65, 19.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042, "Completed", 2, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, 9014651432, 63.05, 38.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032, "Completed", 2, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, second_candidates_all_data)    
        
        result_data_check = [33, "Gironde", 6, "6ème circonscription", "Penny", "Hofstadter", datetime.datetime(1985,11,30), "Sales", "F", True, 5, 46513465, 65.65, 5624, 46513465, 65.65, 5624, "Cooper", "Sheldon", "M", datetime.datetime(1974,3,24),  False, "Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052,  "Completed", 2, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, third_candidate_all_data)   
       
        result_data_check = [92, "Hautes Seine", 8, "8ème circonscription", "Robin", "Scherbatsky", datetime.datetime(1982,4,3), "Journaliste", "F", False, 4, 96513465, 91.05, 46.512, 96513465, 91.05, 46.512, "Aldrin", "Lily", "F", datetime.datetime(1974,3,24),  False, "Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01, 19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032, "Completed", 2, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01, 19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, fourth_candidate_all_data)     
        
        
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_four_elections_datas_from_adapters_list_first_rounds(self, mock_dependency, mock_candidate_adapter, mock_results_first_round_adapter) :        
        helper = HelperTest()
        
        mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_candidate_adapter_four_candidates()
        mock_results_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_four_candidates()             
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_results_first_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()       
        
        first_candidate_all_data = candidates[0]
        second_candidates_all_data = candidates[1]
        third_candidate_all_data = candidates[2]
        fourth_candidate_all_data = candidates[3]
        
        self.assertEqual(4, len(candidates))
        
        assert_test = AssertTest(self, 1)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True,  "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, second_candidates_all_data)    
        
        result_data_check = [33, "Gironde", 6, "6ème circonscription", "Penny", "Hofstadter", datetime.datetime(1985,11,30), "Sales", "F", True, 5, 46513465, 65.65, 5624, "Cooper", "Sheldon", "M", datetime.datetime(1974,3,24),  False, "Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, third_candidate_all_data)   
       
        result_data_check = [92, "Hautes Seine", 8, "8ème circonscription", "Robin", "Scherbatsky", datetime.datetime(1982,4,3), "Journaliste", "F", False, 4, 96513465, 91.05, 46.512, "Aldrin", "Lily", "F", datetime.datetime(1974,3,24),  False, "Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01, 19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, fourth_candidate_all_data)     
        
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsSecondRoundAdapter, 'extracts_datas_from_files')
    def test_get_four_elections_first_round_two_elections_second_rounds(self, mock_dependency, mock_candidate_adapter, mock_results_first_round_adapter, mock_result_second_round_adapter):
        helper = HelperTest()
        
        mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_candidate_adapter_four_candidates()
        mock_results_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_four_candidates()             
        mock_result_second_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_second_round_adapter_two_candidates()
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_results_first_round_adapter, mock_result_second_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate_all_data = candidates[0]
        second_candidates_all_data = candidates[1]
        third_candidate_all_data = candidates[2]
        fourth_candidate_all_data = candidates[3]
        
        self.assertEqual(4, len(candidates))
        
        assert_test = AssertTest(self, 1)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, 21463213, 36.65, 19.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042, "Completed", 2, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, 9014651432, 63.05, 38.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032, "Completed", 2, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, second_candidates_all_data)    
        
        result_data_check = [33, "Gironde", 6, "6ème circonscription", "Penny", "Hofstadter", datetime.datetime(1985,11,30), "Sales", "F", True, 5, 46513465, 65.65, 5624, "Cooper", "Sheldon", "M", datetime.datetime(1974,3,24),  False, "Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, third_candidate_all_data)   
       
        result_data_check = [92, "Hautes Seine", 8, "8ème circonscription", "Robin", "Scherbatsky", datetime.datetime(1982,4,3), "Journaliste", "F", False, 4, 96513465, 91.05, 46.512, "Aldrin", "Lily", "F", datetime.datetime(1974,3,24),  False, "Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01, 19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032]
        assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, fourth_candidate_all_data)   