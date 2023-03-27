import unittest
import datetime
from src.Factory.CreatorCandidate import CreatorCandidate

from tests.helper_test import HelperTest
from tests.base_unit_test import BaseUnitTest

class CreatorCandidateTest(unittest.TestCase):
    def test_creator_candidate_from_gironde(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','datetime.datetime(1978, 06, 03, 0, 0)','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(candidate_data)
        
        candidate_model_check = ["Cazenave", "Thomas", "M", 7, "Cadre de la fonction publique", datetime.datetime(1978,6,3), False]     
        self.__assert_candidate_model(candidate_model_check, candidate)
        

    def test_creator_candidate_woman_sorting_candidate(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','F','TRASTOUR-ISNART','Laurence','datetime.datetime(1972, 03, 06, 0, 0)','LR','Cadre de la fonction publique','Oui','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(candidate_data)
        
        candidate_model_check = ["TRASTOUR-ISNART", "Laurence", "F", 11, "Cadre de la fonction publique", datetime.datetime(1972,3,6), True]     
        self.__assert_candidate_model(candidate_model_check, candidate)
        
        
    def test_creator_candidate_two_first_name(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','Eric','datetime.datetime(1978, 06, 03, 0, 0)','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(candidate_data)
        
        candidate_model_check = ["Cazenave", "Thomas Eric", "M", 7, "Cadre de la fonction publique", datetime.datetime(1978,6,3), False]     
        self.__assert_candidate_model(candidate_model_check, candidate)
        
    
    def __get_creator_init(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidate(parties)
        return creator
    
    
    def  __assert_candidate_model(self, candidate_data_check, candidate_model) :
        self.assertEqual(candidate_data_check[0], candidate_model.last_name)
        self.assertEqual(candidate_data_check[1], candidate_model.first_name)
        self.assertEqual(candidate_data_check[2], candidate_model.sexe)
        self.assertEqual(candidate_data_check[3], candidate_model.party_id)
        self.assertEqual(candidate_data_check[4], candidate_model.job)
        self.assertTrue(candidate_data_check[5] == candidate_model.birth_date)
        self.assertEqual(candidate_data_check[6], candidate_model.is_sorting)
        

    if __name__ == "__main__":
        unittest.main()