import unittest
import datetime
from src.Factory.CreatorCandidate import CreatorCandidate

from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorCandidateTest(unittest.TestCase):
    def test_creator_candidate_from_gironde(self) : 
        creator = self.__get_creator_init()
        
        election_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','1978-06-03 00:00:00','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["Cazenave", "Thomas", "M", 7, "Cadre de la fonction publique", datetime.datetime(1978,6,3), False]   
        assert_test = AssertTest(self, 1)  
        assert_test.assert_candidate_model_basic(candidate_model_check, candidate)
        

    def test_creator_candidate_woman_sorting_candidate(self) : 
        creator = self.__get_creator_init()
        
        election_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','F','TRASTOUR-ISNART','Laurence','1972-03-06 00:00:00','LR','Cadre de la fonction publique','Oui','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["TRASTOUR-ISNART", "Laurence", "F", 11, "Cadre de la fonction publique", datetime.datetime(1972,3,6), True]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_candidate_model_basic(candidate_model_check, candidate)
        
        
    def test_creator_candidate_two_first_name(self) : 
        creator = self.__get_creator_init()
        
        election_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','Eric','1978-06-03 00:00:00','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(election_data)
        
        candidate_model_check = ["Cazenave", "Thomas Eric", "M", 7, "Cadre de la fonction publique", datetime.datetime(1978,6,3), False]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_candidate_model_basic(candidate_model_check, candidate)   
    
    
    def __get_creator_init(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidate(parties) 
        return creator
        
        
    def test_creator_candidate_female_candidate_first_round_data(self) : 
        creator = CreatorCandidate(None)
        
        election_data = [ 8, 'F', 'ARMENJON', 'Eliane', 'ECO', '1161', '1.35', '2.78', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(election_data)
        
        candidate_model_check = ["XXXX","F", "ARMENJON", "Eliane","XXXX", 1161, 1.35, 2.78]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    def test_creator_candidate_male_first_round_data(self) :
        creator = CreatorCandidate(None)
        
        election_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(election_data)
        
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    def test_creator_candidate_male_first_vote_bad_formatted(self) : 
        creator = CreatorCandidate(None)
        
        election_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216.0', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(election_data)
        
        candidate_model_check = ["XXXX","M", "THOMASSIN", "Geoffrey","XXXX", 216, 0.27, 0.54]     
        assert_test = AssertTest(self, 1)  
        assert_test.assert_election_data_first_round_result(candidate_model_check, candidate)   
        
        
    if __name__ == "__main__":
        unittest.main()