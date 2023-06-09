import unittest

from src.Factory.CreatorCandidates import CreatorCandidates
from tests.assert_test import AssertTest

class CreatorCandidatesTest(unittest.TestCase) : 
    
    def test_creator_candidates_from_first_round_data_excel_first_line(self) : 
        creator = CreatorCandidates()
        candidates_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX',4,'M', 'LAHY', 'Éric', 'DXG', 391, '0.45', '0.94', 'nan', 8, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, '1.35', '2.78', 'nan', 'nan', 'nan']
        
        candidates = creator.factory_method(candidates_data)  
        
        self.assertEqual(2, len(candidates))        
        candidate_model_check = ["XXXX","M", "LAHY", "Éric","XXXX", 391, 0.45, 0.94]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[0])   
        
        candidate_model_check = ["XXXX","F", "ARMENJON", "Eliane","XXXX", 1161, 1.35, 2.78]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[1]) 
        
  
    def test_creator_candidates_from_first_round_data_excel_second_line(self) : 
        creator = CreatorCandidates()
        candidates_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX',3,'F', 'VUITTON', 'Brigitte', 'DXG', 779, '0.98', '1.93', 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, '16.56', '32.51', 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, '0.27', '0.54', 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, '0.0', '0.0', 'nan', 'nan']
         
        candidates = creator.factory_method(candidates_data)
        
        self.assertEqual(4, len(candidates))        
        candidate_model_check = ["XXXX","F", "VUITTON", "Brigitte","XXXX", 779, 0.98, 1.93]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[0])   
        
        candidate_model_check = ["XXXX","M", "RAVACLEY", "Stéphane","XXXX", 13112, 16.56, 32.51]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[1])  
            
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[2])   
        
        candidate_model_check = ["XXXX","F", "MEYER", "Claudine","XXXX", 0, 0.0, 0.0]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidates[3]) 
        