import unittest

from src.Factory.CreatorCandidatesSecondRound import CreatorCandidatesSecondRound
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorCandidatesSecondRoundTest(unittest.TestCase) : 
    def test_creator_candidates_from_second_round_data_excel_first_line(self) : 
        creator = CreatorCandidatesSecondRound(None)
        candidates_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 43, '13.15', '29.45', '3.0', 'M', 'BRETON', 'Xavier', 'LR', '103.0', '31.5', '70.55', 'nan', 'nan']
        
        candidates = creator.factory_method(candidates_data)  
        
        self.assertEqual(2, len(candidates))        
        
        candidate_model_check = ["XXXX", "M", "GUÉRAUD", "Sébastien","XXXX", 43, 13.15, 29.45]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[0])   
        
        candidate_model_check = ["XXXX","M", "BRETON", "Xavier","XXXX", 103, 31.5, 70.55]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[1])         
        
        
    def test_creator_candidates_from_second_round_data_excel_second_line_with_last_election_data_model(self) :
        helper = HelperTest()
        last_election_data = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorCandidatesSecondRound(last_election_data)
        
        candidates_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 108, '17.88', '39.27', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 167, '27.65', '60.73', 'nan', 'nan']
        
        candidates = creator.factory_method(candidates_data)
        
        self.assertEqual(2, len(candidates))        
        
        candidate_model_check = ["XXXX", "M", "GUÉRAUD", "Sébastien","XXXX", 151, 15.515, 34.36]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[0])   
        
        candidate_model_check = ["XXXX","M", "BRETON", "Xavier","XXXX", 270, 29.575, 65.64]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[1]) 
        
        
    def test_creator_candidates_with_two_last_election_data_created_second_round_data(self) :
        helper = HelperTest()
        last_election_datas = helper.get_two_cities_data_first_department_first_district_last_election_data_model()
        creator = CreatorCandidatesSecondRound(last_election_datas)
        
        candidates_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 67, '15.02', '34.36', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 128, '28.7', '65.64', 'nan', 'nan']
        
        candidates = creator.factory_method(candidates_data)
        
        self.assertEqual(2, len(candidates))
        
        candidate_model_check = ["XXXX", "M", "GUÉRAUD", "Sébastien","XXXX", 218, 15.35, 34.36]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[0])   
        
        candidate_model_check = ["XXXX","M", "BRETON", "Xavier","XXXX", 398, 29.283, 65.64]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidates[1]) 