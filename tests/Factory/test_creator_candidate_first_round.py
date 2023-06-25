import unittest

from src.Factory.CreatorCandidateFirstRound import CreatorCandidateFirstRound

from tests.assert_test import AssertTest

class CreatorCandidateFirstRoundTest(unittest.TestCase) :
    def test_creator_candidate_female_candidate_first_round_data(self) : 
        creator = CreatorCandidateFirstRound(None)
        
        election_data = [ 8, 'F', 'ARMENJON', 'Eliane', 'ECO', '1161', '1.35', '2.78', 'nan']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX","F", "ARMENJON", "Eliane","XXXX", 1161, 1.35, 2.78]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    def test_creator_candidate_male_first_round_data(self) :
        creator = CreatorCandidateFirstRound(None)
        
        election_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    def test_creator_candidate_male_first_vote_bad_formatted(self) : 
        creator = CreatorCandidateFirstRound(None)
        
        election_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216.0', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    if __name__ == "__main__":
        unittest.main()