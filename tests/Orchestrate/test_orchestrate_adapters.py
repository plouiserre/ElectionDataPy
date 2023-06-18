import datetime
import unittest
from unittest.mock import patch


from helper_test import HelperTest
from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Adapter.ResultsFirstRoundAdapter import ResultsFirstRoundAdapter
from src.Dependency.Dependency import Dependency
from src.Models.ElectionDataModel import ElectionDataModel
from src.Models.ResultModel import ResultModel
from src.Orchestrate.OrchestrateAdapters import OrchestrateAdapters
from tests.assert_test import AssertTest

#TODO factorize with helper test
class OrchestrateStoreAdaptersTest(unittest.TestCase):
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_candidates_datas_from_adapters_two_candidates_data_models(self, mock_dependency, mock_candidate_adapter, mock_result_district_first_round_adapter) :        
        mock_candidate_adapter.extracts_datas_from_files.return_value = self.__get_election_data_from_candidate_adapter_two_candidates()
        mock_result_district_first_round_adapter.extracts_datas_from_files.return_value = self.__get_election_data_from_first_round_adapter_two_candidates()             
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_result_district_first_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate_all_data = candidates[0]        
        second_candidates_all_data = candidates[1]
        
        self.assertEqual(2, len(candidates))
        
        assert_test = AssertTest(self, 1)
        
        result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, second_candidates_all_data)        
        
        
        
    def __get_election_data_from_candidate_adapter_two_candidates(self) :
        helper = HelperTest()
        elections = helper.get_two_elections_data_model()
        return elections
    
    
    def __get_election_data_from_first_round_adapter_two_candidates(self) :        
        helper = HelperTest()
        
        first_department = helper.get_department("Aisne",2)
        first_district = helper.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_candidate = helper.get_candidate("Wednesday", None, None, None, "Addams", 0, "F")
        first_candidate.vote_first_round = 5463213
        first_candidate.rate_vote_registered_first_round = 12.65
        first_candidate.rate_vote_expressed_first_round = 9.24
        first_election_data = ElectionDataModel()
        first_election_data.department = first_department
        first_election_data.district = first_district
        first_election_data.candidates.append(first_candidate)
        first_election_data.result = self.__get_result("Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042)        
        second_department = helper.get_department("Nord",59)
        second_district = helper.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_candidate = helper.get_candidate("Thomas",  None, None, None, "Shelby", 0, "M")
        second_candidate.vote_first_round = 614651432
        second_candidate.rate_vote_registered_first_round = 37.95
        second_candidate.rate_vote_expressed_first_round = 35.57  
        second_election_data = ElectionDataModel()
        second_election_data.department = second_department
        second_election_data.district = second_district
        second_election_data.candidates.append(second_candidate)
        second_election_data.result = self.__get_result("Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032)
        
        candidates = [first_election_data, second_election_data]
        
        return candidates
    
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ResultsFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_candidates_datas_from_adapters_four_candidates_data_models(self, mock_dependency, mock_candidate_adapter, mock_results_first_round_adapter) :        
        mock_candidate_adapter.extracts_datas_from_files.return_value = self.__get_election_data_from_candidate_adapter_four_candidates()
        mock_results_first_round_adapter.extracts_datas_from_files.return_value = self.__get_election_data_from_first_round_adapter_four_candidates()             
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
        assert_test.assert_result_data_model_with_all_infos(result_data_check, first_candidate_all_data)
        
        result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True,  "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, second_candidates_all_data)    
        
        result_data_check = [33, "Gironde", 6, "6ème circonscription", "Penny", "Hofstadter", datetime.datetime(1985,11,30), "Sales", "F", True, 5, 46513465, 65.65, 5624, "Cooper", "Sheldon", "M", datetime.datetime(1974,3,24),  False, "Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, third_candidate_all_data)   
       
        result_data_check = [92, "Hautes Seine", 8, "8ème circonscription", "Robin", "Scherbatsky", datetime.datetime(1982,4,3), "Journaliste", "F", False, 4, 96513465, 91.05, 46.512, "Aldrin", "Lily", "F", datetime.datetime(1974,3,24),  False, "Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01, 19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032]
        assert_test.assert_result_data_model_with_all_infos(result_data_check, fourth_candidate_all_data)     
        
        
    def __get_election_data_from_candidate_adapter_four_candidates(self) : 
        candidates = self.__get_election_data_from_candidate_adapter_two_candidates()
        
        helper = HelperTest()
        
        third_election_data = ElectionDataModel()
        third_department = helper.get_department("Gironde", 33)
        third_district = helper.get_district("6ème circonscription", 6)
        third_candidate = helper.get_candidate("Penny", datetime.datetime(1985,11,30), True, "Sales", "Hofstadter", 5, "F")
        third_deputy = helper.get_deputy("Sheldon", "Cooper", datetime.datetime(1974,3,24),"M",False)
        third_election_data.candidates.append(third_candidate)
        third_election_data.department = third_department
        third_election_data.deputies.append(third_deputy)
        third_election_data.district = third_district
        
        fourth_election_data = ElectionDataModel()
        fourth_department = helper.get_department("Hautes Seine", 92)
        fourth_district = helper.get_district("8ème circonscription", 8)
        fourth_candidate = helper.get_candidate("Robin", datetime.datetime(1982,4,3), False, "Journaliste", "Scherbatsky", 4, "F")
        fourth_deputy = helper.get_deputy("Lily", "Aldrin", datetime.datetime(1974,3,24),"F",False)
        fourth_election_data.candidates.append(fourth_candidate)
        fourth_election_data.department = fourth_department
        fourth_election_data.deputies.append(fourth_deputy)
        fourth_election_data.district = fourth_district
        
        candidates.append(third_election_data)
        candidates.append(fourth_election_data)
        
        return candidates
    
    
    def __get_election_data_from_first_round_adapter_four_candidates(self) : 
        candidates = self.__get_election_data_from_first_round_adapter_two_candidates()
        
        helper = HelperTest()
        
        third_department = helper.get_department("Gironde", 33)
        third_district = helper.get_district("6ème circonscription", 6)
        third_district.department = third_department
        third_candidate = helper.get_candidate("Penny", None, None, None, "Hofstadter", 0, "F")
        third_candidate.vote_first_round = 46513465
        third_candidate.rate_vote_registered_first_round = 65.65
        third_candidate.rate_vote_expressed_first_round = 5624
        third_election_data = ElectionDataModel()
        third_election_data.department = third_department
        third_election_data.district = third_district
        third_election_data.candidates.append(third_candidate)
        third_election_data.result = self.__get_result("Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052)
        
        fourth_department = helper.get_department("Hautes Seine", 92)
        fourth_district = helper.get_district("8ème circonscription", 8) 
        fourth_district.department = fourth_department
        fourth_candidate = helper.get_candidate("Robin",  None, None, None, "Scherbatsky", 0, "F")
        fourth_candidate.vote_first_round = 96513465
        fourth_candidate.rate_vote_registered_first_round = 91.05
        fourth_candidate.rate_vote_expressed_first_round = 46.512
        fourth_election_data = ElectionDataModel()
        fourth_election_data.department = fourth_department
        fourth_election_data.district = fourth_district
        fourth_election_data.candidates.append(fourth_candidate)
        fourth_election_data.result = self.__get_result("Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01,  19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032)
        
        candidates.append(third_election_data)
        candidates.append(fourth_election_data)
        
        return candidates
        
        
        
    def __get_result(self, state_compute, round_number, registered, abstaining, rate_abstaining, voting, rate_voting, blank_balot, rate_blank_registered, rate_blank_voting, null_ballot, 
                       rate_null_registered, rate_null_voting, expressed, rate_express_registered, rate_express_voting) : 
        result = ResultModel()
        result.state_compute = state_compute
        result.round_number = round_number
        result.registered = registered
        result.abstaining = abstaining
        result.rate_abstaining = rate_abstaining
        result.voting = voting
        result.rate_voting = rate_voting
        result.blank_balot = blank_balot
        result.rate_blank_registered = rate_blank_registered
        result.rate_blank_voting = rate_blank_voting
        result.null_ballot = null_ballot
        result.rate_null_registered = rate_null_registered
        result.rate_null_voting = rate_null_voting
        result.expressed = expressed
        result.rate_express_registered = rate_express_registered
        result.rate_express_voting = rate_express_voting
        return result