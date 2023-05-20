import datetime
import unittest
from unittest.mock import patch

from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Adapter.ElectionDistrictFirstRoundAdapter import ElectionDistrictFirstRoundAdapter
from src.Dependency.Dependency import Dependency
from src.Models.CandidateDataModel import CandidateDataModel
from src.Models.ElectionModel import ElectionModel
from src.Orchestrate.OrchestrateAdapters import OrchestrateAdapters
from helper_test import HelperTest

#TODO factorize with helper test
class OrchestrateStoreAdaptersTest(unittest.TestCase):
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ElectionDistrictFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_candidates_datas_from_adapters_two_candidates_data_models(self, mock_dependency, mock_candidate_adapter, mock_election_district_first_round_adapter) :        
        mock_candidate_adapter.extracts_datas_from_files.return_value = self.__get_candidate_data_from_candidate_adapter_two_candidates()
        mock_election_district_first_round_adapter.extracts_datas_from_files.return_value = self.__get_candidate_data_from_first_round_adapter_two_candidates()             
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_election_district_first_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate_all_data = candidates[0]
        first_candidate = first_candidate_all_data.candidates[0]
        
        second_candidates_all_data = candidates[1]
        second_candidate = second_candidates_all_data.candidates[0]
        
        self.assertEqual(2, len(candidates))
        
        self.assertEqual("Aisne", first_candidate_all_data.department.name)
        self.assertEqual(2, first_candidate_all_data.department.number)
        self.assertEqual("4ème circonscription", first_candidate_all_data.district.name)
        self.assertEqual(4, first_candidate_all_data.district.number)
        self.assertEqual("Wednesday", first_candidate.first_name)
        self.assertEqual("Addams", first_candidate.last_name)
        self.assertTrue(datetime.datetime(2002,9,27) == first_candidate.birthdate)
        self.assertEqual("Student", first_candidate.job)
        self.assertEqual("F", first_candidate.sexe)
        self.assertFalse(first_candidate.is_sorting)
        self.assertEqual(3, first_candidate.party_id)
        self.assertEqual(5463213,first_candidate.vote)
        self.assertEqual(12.65,first_candidate.rate_vote_registered)
        self.assertEqual(9.24,first_candidate.rate_vote_expressed)
        self.assertEqual("Enid", first_candidate_all_data.deputies[0].first_name)
        self.assertEqual("Sinclair", first_candidate_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(2002, 4, 2) == first_candidate_all_data.deputies[0].birthdate)
        self.assertEqual("F", first_candidate_all_data.deputies[0].sexe)
        self.assertFalse(first_candidate_all_data.deputies[0].is_sorting)
        self.assertEqual("Completed", first_candidate_all_data.election.state_compute)
        self.assertEqual(4654321, first_candidate_all_data.election.registered)
        self.assertEqual(56123, first_candidate_all_data.election.abstaining)
        self.assertEqual(10.5, first_candidate_all_data.election.rate_abstaining)
        self.assertEqual(3561234, first_candidate_all_data.election.voting)
        self.assertEqual(95.5, first_candidate_all_data.election.rate_voting)
        self.assertEqual(1234, first_candidate_all_data.election.blank_balot)
        self.assertEqual(30.1, first_candidate_all_data.election.rate_blank_registered)
        self.assertEqual(12.15, first_candidate_all_data.election.rate_blank_voting)
        self.assertEqual(123, first_candidate_all_data.election.null_ballot)
        self.assertEqual(1.01, first_candidate_all_data.election.rate_null_registered)
        self.assertEqual(0.75, first_candidate_all_data.election.rate_null_voting)
        self.assertEqual(7456, first_candidate_all_data.election.expressed)
        self.assertEqual(0.345, first_candidate_all_data.election.rate_express_registered)
        self.assertEqual(0.042, first_candidate_all_data.election.rate_express_voting)
        
        
        self.assertEqual("Nord", second_candidates_all_data.department.name)
        self.assertEqual(59, second_candidates_all_data.department.number)
        self.assertEqual("13ème circonscription", second_candidates_all_data.district.name)
        self.assertEqual(13, second_candidates_all_data.district.number)
        self.assertEqual("Thomas", second_candidate.first_name)
        self.assertEqual("Shelby", second_candidate.last_name)
        self.assertTrue(datetime.datetime(1976,5,25) == second_candidate.birthdate)
        self.assertEqual("Gangster", second_candidate.job)
        self.assertEqual("M", second_candidate.sexe)
        self.assertTrue(second_candidate.is_sorting)
        self.assertEqual(6, second_candidate.party_id)
        self.assertEqual(614651432,second_candidate.vote)
        self.assertEqual(37.95,second_candidate.rate_vote_registered)
        self.assertEqual(35.57,second_candidate.rate_vote_expressed)
        self.assertEqual("Polly", second_candidates_all_data.deputies[0].first_name)
        self.assertEqual("Gray", second_candidates_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(1968, 8,17) == second_candidates_all_data.deputies[0].birthdate)
        self.assertEqual("F", second_candidates_all_data.deputies[0].sexe)
        self.assertTrue(second_candidates_all_data.deputies[0].is_sorting) 
        self.assertEqual("Completed", second_candidates_all_data.election.state_compute)
        self.assertEqual(897465143, second_candidates_all_data.election.registered)
        self.assertEqual(561023, second_candidates_all_data.election.abstaining)
        self.assertEqual(9.5, second_candidates_all_data.election.rate_abstaining)
        self.assertEqual(857465143, second_candidates_all_data.election.voting)
        self.assertEqual(75.5, second_candidates_all_data.election.rate_voting)
        self.assertEqual(134, second_candidates_all_data.election.blank_balot)
        self.assertEqual(3.01, second_candidates_all_data.election.rate_blank_registered)
        self.assertEqual(9.15, second_candidates_all_data.election.rate_blank_voting)
        self.assertEqual(103, second_candidates_all_data.election.null_ballot)
        self.assertEqual(0.91, second_candidates_all_data.election.rate_null_registered)
        self.assertEqual(0.65, second_candidates_all_data.election.rate_null_voting)
        self.assertEqual(6456, second_candidates_all_data.election.expressed)
        self.assertEqual(0.245, second_candidates_all_data.election.rate_express_registered)
        self.assertEqual(0.032, second_candidates_all_data.election.rate_express_voting)              
        
        
    def __get_candidate_data_from_candidate_adapter_two_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_two_candidates_data_model()
        return candidates
    
    
    def __get_candidate_data_from_first_round_adapter_two_candidates(self) :        
        helper = HelperTest()
        
        first_department = helper.get_department("Aisne",2)
        first_district = helper.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_candidate = helper.get_candidate("Wednesday", None, None, None, "Addams", 0, "F")
        first_candidate.vote = 5463213
        first_candidate.rate_vote_registered = 12.65
        first_candidate.rate_vote_expressed = 9.24
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = first_department
        first_candidate_data.district = first_district
        first_candidate_data.candidates.append(first_candidate)
        first_candidate_data.election = self.__get_election("Completed", 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042)        
        second_department = helper.get_department("Nord",59)
        second_district = helper.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_candidate = helper.get_candidate("Thomas",  None, None, None, "Shelby", 0, "M")
        second_candidate.vote = 614651432
        second_candidate.rate_vote_registered = 37.95
        second_candidate.rate_vote_expressed = 35.57  
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = second_department
        second_candidate_data.district = second_district
        second_candidate_data.candidates.append(second_candidate)
        second_candidate_data.election = self.__get_election("Completed", 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032)
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates
    
    
    @patch.object(Dependency,'get_dependency')
    @patch.object(CandidateAdapter, 'extracts_datas_from_files')
    @patch.object(ElectionDistrictFirstRoundAdapter, 'extracts_datas_from_files')
    def test_get_candidates_datas_from_adapters_four_candidates_data_models(self, mock_dependency, mock_candidate_adapter, mock_election_district_first_round_adapter) :        
        mock_candidate_adapter.extracts_datas_from_files.return_value = self.__get_candidate_data_from_candidate_adapter_four_candidates()
        mock_election_district_first_round_adapter.extracts_datas_from_files.return_value = self.__get_candidate_data_from_first_round_adapter_four_candidates()             
        mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_election_district_first_round_adapter]
        
        orchestrate = OrchestrateAdapters(mock_dependency)
        
        candidates = orchestrate.get_candidates_datas_from_adapters()
        
        first_candidate = candidates[0]
        second_candidate = candidates[1]
        third_candidate = candidates[2]
        fourth_candidate = candidates[3]
        
        first_candidate_all_data = candidates[0]
        first_candidate = first_candidate_all_data.candidates[0]
        
        second_candidates_all_data = candidates[1]
        second_candidate = second_candidates_all_data.candidates[0]
        
        third_candidate_all_data = candidates[2]
        third_candidate = third_candidate_all_data.candidates[0]
        
        fourth_candidates_all_data = candidates[3]
        fourth_candidate = fourth_candidates_all_data.candidates[0]
        
        self.assertEqual(4, len(candidates))
        
        self.assertEqual("Aisne", first_candidate_all_data.department.name)
        self.assertEqual(2, first_candidate_all_data.department.number)
        self.assertEqual("4ème circonscription", first_candidate_all_data.district.name)
        self.assertEqual(4, first_candidate_all_data.district.number)
        self.assertEqual("Wednesday", first_candidate.first_name)
        self.assertEqual("Addams", first_candidate.last_name)
        self.assertTrue(datetime.datetime(2002,9,27) == first_candidate.birthdate)
        self.assertEqual("Student", first_candidate.job)
        self.assertEqual("F", first_candidate.sexe)
        self.assertFalse(first_candidate.is_sorting)
        self.assertEqual(3, first_candidate.party_id)
        self.assertEqual(5463213,first_candidate.vote)
        self.assertEqual(12.65,first_candidate.rate_vote_registered)
        self.assertEqual(9.24,first_candidate.rate_vote_expressed)
        self.assertEqual("Enid", first_candidate_all_data.deputies[0].first_name)
        self.assertEqual("Sinclair", first_candidate_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(2002, 4, 2) == first_candidate_all_data.deputies[0].birthdate)
        self.assertEqual("F", first_candidate_all_data.deputies[0].sexe)
        self.assertFalse(first_candidate_all_data.deputies[0].is_sorting)
        self.assertEqual("Completed", first_candidate_all_data.election.state_compute)
        self.assertEqual(4654321, first_candidate_all_data.election.registered)
        self.assertEqual(56123, first_candidate_all_data.election.abstaining)
        self.assertEqual(10.5, first_candidate_all_data.election.rate_abstaining)
        self.assertEqual(3561234, first_candidate_all_data.election.voting)
        self.assertEqual(95.5, first_candidate_all_data.election.rate_voting)
        self.assertEqual(1234, first_candidate_all_data.election.blank_balot)
        self.assertEqual(30.1, first_candidate_all_data.election.rate_blank_registered)
        self.assertEqual(12.15, first_candidate_all_data.election.rate_blank_voting)
        self.assertEqual(123, first_candidate_all_data.election.null_ballot)
        self.assertEqual(1.01, first_candidate_all_data.election.rate_null_registered)
        self.assertEqual(0.75, first_candidate_all_data.election.rate_null_voting)
        self.assertEqual(7456, first_candidate_all_data.election.expressed)
        self.assertEqual(0.345, first_candidate_all_data.election.rate_express_registered)
        self.assertEqual(0.042, first_candidate_all_data.election.rate_express_voting)
        
        
        self.assertEqual("Nord", second_candidates_all_data.department.name)
        self.assertEqual(59, second_candidates_all_data.department.number)
        self.assertEqual("13ème circonscription", second_candidates_all_data.district.name)
        self.assertEqual(13, second_candidates_all_data.district.number)
        self.assertEqual("Thomas", second_candidate.first_name)
        self.assertEqual("Shelby", second_candidate.last_name)
        self.assertTrue(datetime.datetime(1976,5,25) == second_candidate.birthdate)
        self.assertEqual("Gangster", second_candidate.job)
        self.assertEqual("M", second_candidate.sexe)
        self.assertTrue(second_candidate.is_sorting)
        self.assertEqual(6, second_candidate.party_id)
        self.assertEqual(614651432,second_candidate.vote)
        self.assertEqual(37.95,second_candidate.rate_vote_registered)
        self.assertEqual(35.57,second_candidate.rate_vote_expressed)
        self.assertEqual("Polly", second_candidates_all_data.deputies[0].first_name)
        self.assertEqual("Gray", second_candidates_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(1968, 8,17) == second_candidates_all_data.deputies[0].birthdate)
        self.assertEqual("F", second_candidates_all_data.deputies[0].sexe)
        self.assertTrue(second_candidates_all_data.deputies[0].is_sorting) 
        self.assertEqual("Completed", second_candidates_all_data.election.state_compute)
        self.assertEqual(897465143, second_candidates_all_data.election.registered)
        self.assertEqual(561023, second_candidates_all_data.election.abstaining)
        self.assertEqual(9.5, second_candidates_all_data.election.rate_abstaining)
        self.assertEqual(857465143, second_candidates_all_data.election.voting)
        self.assertEqual(75.5, second_candidates_all_data.election.rate_voting)
        self.assertEqual(134, second_candidates_all_data.election.blank_balot)
        self.assertEqual(3.01, second_candidates_all_data.election.rate_blank_registered)
        self.assertEqual(9.15, second_candidates_all_data.election.rate_blank_voting)
        self.assertEqual(103, second_candidates_all_data.election.null_ballot)
        self.assertEqual(0.91, second_candidates_all_data.election.rate_null_registered)
        self.assertEqual(0.65, second_candidates_all_data.election.rate_null_voting)
        self.assertEqual(6456, second_candidates_all_data.election.expressed)
        self.assertEqual(0.245, second_candidates_all_data.election.rate_express_registered)
        self.assertEqual(0.032, second_candidates_all_data.election.rate_express_voting)      
        
        self.assertEqual("Gironde", third_candidate_all_data.department.name)
        self.assertEqual(33, third_candidate_all_data.department.number)
        self.assertEqual("6ème circonscription", third_candidate_all_data.district.name)
        self.assertEqual(6, third_candidate_all_data.district.number)
        self.assertEqual("Penny", third_candidate.first_name)
        self.assertEqual("Hofstadter", third_candidate.last_name)
        self.assertTrue(datetime.datetime(1985,11,30) == third_candidate.birthdate)
        self.assertEqual("Sales", third_candidate.job)
        self.assertEqual("F", third_candidate.sexe)
        self.assertTrue(third_candidate.is_sorting)
        self.assertEqual(5, third_candidate.party_id)
        self.assertEqual(46513465,third_candidate.vote)
        self.assertEqual(65.65,third_candidate.rate_vote_registered)
        self.assertEqual(5624,third_candidate.rate_vote_expressed)
        self.assertEqual("Sheldon", third_candidate_all_data.deputies[0].first_name)
        self.assertEqual("Cooper", third_candidate_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(1974,3,24) == third_candidate_all_data.deputies[0].birthdate)
        self.assertEqual("M", third_candidate_all_data.deputies[0].sexe)
        self.assertFalse(third_candidate_all_data.deputies[0].is_sorting)         
        self.assertEqual("Completed", third_candidate_all_data.election.state_compute)
        self.assertEqual(15132134, third_candidate_all_data.election.registered)
        self.assertEqual(46123, third_candidate_all_data.election.abstaining)
        self.assertEqual(30.5, third_candidate_all_data.election.rate_abstaining)
        self.assertEqual(2561234, third_candidate_all_data.election.voting)
        self.assertEqual(75.5, third_candidate_all_data.election.rate_voting)
        self.assertEqual(666, third_candidate_all_data.election.blank_balot)
        self.assertEqual(20.1, third_candidate_all_data.election.rate_blank_registered)
        self.assertEqual(8.15, third_candidate_all_data.election.rate_blank_voting)
        self.assertEqual(113, third_candidate_all_data.election.null_ballot)
        self.assertEqual(0.71, third_candidate_all_data.election.rate_null_registered)
        self.assertEqual(0.85, third_candidate_all_data.election.rate_null_voting)
        self.assertEqual(8456, third_candidate_all_data.election.expressed)
        self.assertEqual(0.245, third_candidate_all_data.election.rate_express_registered)
        self.assertEqual(0.052, third_candidate_all_data.election.rate_express_voting)   
        
        self.assertEqual("Hautes Seine", fourth_candidates_all_data.department.name)
        self.assertEqual(92, fourth_candidates_all_data.department.number)
        self.assertEqual("8ème circonscription", fourth_candidates_all_data.district.name)
        self.assertEqual(8, fourth_candidates_all_data.district.number)
        self.assertEqual("Robin", fourth_candidate.first_name)
        self.assertEqual("Scherbatsky", fourth_candidate.last_name)
        self.assertTrue(datetime.datetime(1982,4,3) == fourth_candidate.birthdate)
        self.assertEqual("Journaliste", fourth_candidate.job)
        self.assertEqual("F", fourth_candidate.sexe)
        self.assertFalse(fourth_candidate.is_sorting)
        self.assertEqual(4, fourth_candidate.party_id)
        self.assertEqual(96513465,fourth_candidate.vote)
        self.assertEqual(91.05,fourth_candidate.rate_vote_registered)
        self.assertEqual(46.512,fourth_candidate.rate_vote_expressed)
        self.assertEqual("Lily", fourth_candidates_all_data.deputies[0].first_name)
        self.assertEqual("Aldrin", fourth_candidates_all_data.deputies[0].last_name)
        self.assertTrue(datetime.datetime(1974,3,24) == fourth_candidates_all_data.deputies[0].birthdate)
        self.assertEqual("F", fourth_candidates_all_data.deputies[0].sexe)
        self.assertFalse(fourth_candidates_all_data.deputies[0].is_sorting) 
        self.assertEqual("Completed", fourth_candidates_all_data.election.state_compute)
        self.assertEqual(4635123, fourth_candidates_all_data.election.registered)
        self.assertEqual(45646, fourth_candidates_all_data.election.abstaining)
        self.assertEqual(19.5, fourth_candidates_all_data.election.rate_abstaining)
        self.assertEqual(646543, fourth_candidates_all_data.election.voting)
        self.assertEqual(66.4, fourth_candidates_all_data.election.rate_voting)
        self.assertEqual(234, fourth_candidates_all_data.election.blank_balot)
        self.assertEqual(5.01, fourth_candidates_all_data.election.rate_blank_registered)
        self.assertEqual(19.15, fourth_candidates_all_data.election.rate_blank_voting)
        self.assertEqual(93, fourth_candidates_all_data.election.null_ballot)
        self.assertEqual(1.91, fourth_candidates_all_data.election.rate_null_registered)
        self.assertEqual(0.55, fourth_candidates_all_data.election.rate_null_voting)
        self.assertEqual(5456, fourth_candidates_all_data.election.expressed)
        self.assertEqual(0.235, fourth_candidates_all_data.election.rate_express_registered)
        self.assertEqual(0.032, fourth_candidates_all_data.election.rate_express_voting)   
        
        
    def __get_candidate_data_from_candidate_adapter_four_candidates(self) : 
        candidates = self.__get_candidate_data_from_candidate_adapter_two_candidates()
        
        helper = HelperTest()
        
        third_candidate_data = CandidateDataModel()
        third_department = helper.get_department("Gironde", 33)
        third_district = helper.get_district("6ème circonscription", 6)
        third_candidate = helper.get_candidate("Penny", datetime.datetime(1985,11,30), True, "Sales", "Hofstadter", 5, "F")
        third_deputy = helper.get_deputy("Sheldon", "Cooper", datetime.datetime(1974,3,24),"M",False)
        third_candidate_data.candidates.append(third_candidate)
        third_candidate_data.department = third_department
        third_candidate_data.deputies.append(third_deputy)
        third_candidate_data.district = third_district
        
        fourth_candidate_data = CandidateDataModel()
        fourth_department = helper.get_department("Hautes Seine", 92)
        fourth_district = helper.get_district("8ème circonscription", 8)
        fourth_candidate = helper.get_candidate("Robin", datetime.datetime(1982,4,3), False, "Journaliste", "Scherbatsky", 4, "F")
        fourth_deputy = helper.get_deputy("Lily", "Aldrin", datetime.datetime(1974,3,24),"F",False)
        fourth_candidate_data.candidates.append(fourth_candidate)
        fourth_candidate_data.department = fourth_department
        fourth_candidate_data.deputies.append(fourth_deputy)
        fourth_candidate_data.district = fourth_district
        
        candidates.append(third_candidate_data)
        candidates.append(fourth_candidate_data)
        
        return candidates
    
    
    def __get_candidate_data_from_first_round_adapter_four_candidates(self) : 
        candidates = self.__get_candidate_data_from_first_round_adapter_two_candidates()
        
        helper = HelperTest()
        
        third_department = helper.get_department("Gironde", 33)
        third_district = helper.get_district("6ème circonscription", 6)
        third_district.department = third_department
        third_candidate = helper.get_candidate("Penny", None, None, None, "Hofstadter", 0, "F")
        third_candidate.vote = 46513465
        third_candidate.rate_vote_registered = 65.65
        third_candidate.rate_vote_expressed = 5624
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department = third_department
        third_candidate_data.district = third_district
        third_candidate_data.candidates.append(third_candidate)
        third_candidate_data.election = self.__get_election("Completed", 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052)
        
        fourth_department = helper.get_department("Hautes Seine", 92)
        fourth_district = helper.get_district("8ème circonscription", 8) 
        fourth_district.department = fourth_department
        fourth_candidate = helper.get_candidate("Robin",  None, None, None, "Scherbatsky", 0, "F")
        fourth_candidate.vote = 96513465
        fourth_candidate.rate_vote_registered = 91.05
        fourth_candidate.rate_vote_expressed = 46.512
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department = fourth_department
        fourth_candidate_data.district = fourth_district
        fourth_candidate_data.candidates.append(fourth_candidate)
        fourth_candidate_data.election = self.__get_election("Completed", 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01,  19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032)
        
        candidates.append(third_candidate_data)
        candidates.append(fourth_candidate_data)
        
        return candidates
        
        
        
    def __get_election(self, state_compute, registered, abstaining, rate_abstaining, voting, rate_voting, blank_balot, rate_blank_registered, rate_blank_voting, null_ballot, 
                       rate_null_registered, rate_null_voting, expressed, rate_express_registered, rate_express_voting) : 
        election = ElectionModel()
        election.state_compute = state_compute
        election.registered = registered
        election.abstaining = abstaining
        election.rate_abstaining = rate_abstaining
        election.voting = voting
        election.rate_voting = rate_voting
        election.blank_balot = blank_balot
        election.rate_blank_registered = rate_blank_registered
        election.rate_blank_voting = rate_blank_voting
        election.null_ballot = null_ballot
        election.rate_null_registered = rate_null_registered
        election.rate_null_voting = rate_null_voting
        election.expressed = expressed
        election.rate_express_registered = rate_express_registered
        election.rate_express_voting = rate_express_voting
        return election