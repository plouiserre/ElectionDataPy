import unittest

from src.Factory.CreatorCandidateSecondRound import CreatorCandidateSecondRound
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorCandidateSecondRoundTest(unittest.TestCase) :
    def test_creator_candidate_female_candidate_second_round_data(self) : 
        creator = CreatorCandidateSecondRound(None, None) 
        
        election_data = [ 8, 'F', 'ARMENJON', 'Eliane', 'ECO', '1161', '1.35', '2.78', 'nan']
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX","F", "ARMENJON", "Eliane","XXXX", 1161, 1.35, 2.78]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidate)  
        
        
    def test_creator_candidate_male_first_round_data(self) :
        creator = CreatorCandidateSecondRound(None, None)
        
        election_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidate) 
        
        
    def test_creator_candidate_with__one_last_election_data_created(self) :
        helper = HelperTest()
        last_election_data = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorCandidateSecondRound(None, last_election_data)
        
        election_data = [8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 108, '17.88', '39.27', 'nan'] 
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX", "M", "GUÉRAUD", "Sébastien", "XXXX", 151, 15.515, 34.36]
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_second_round_result(candidate_model_check, candidate) 
            