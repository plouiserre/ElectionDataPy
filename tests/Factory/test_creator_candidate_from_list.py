import unittest
import datetime
from src.Factory.CreatorCandidateFromList import CreatorCandidateFromList

from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorCandidateTestFromList(unittest.TestCase):
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
        creator = CreatorCandidateFromList(parties) 
        return creator
        
    if __name__ == "__main__":
        unittest.main()