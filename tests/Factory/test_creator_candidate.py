import unittest
import datetime
from src.Factory.CreatorCandidate import CreatorCandidate

from tests.helper_test import HelperTest
from tests.base_unit_test import BaseUnitTest

class CreatorCandidateTest(unittest.TestCase):
    def test_creator_candidate_from_gironde(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','1978-06-03 00:00:00','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(candidate_data)
        
        candidate_model_check = ["Cazenave", "Thomas", "M", 7, "Cadre de la fonction publique", datetime.datetime(1978,6,3), False]     
        self.__assert_candidate_model(candidate_model_check, candidate)
        

    def test_creator_candidate_woman_sorting_candidate(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','F','TRASTOUR-ISNART','Laurence','1972-03-06 00:00:00','LR','Cadre de la fonction publique','Oui','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        candidate = creator.factory_method(candidate_data)
        
        candidate_model_check = ["TRASTOUR-ISNART", "Laurence", "F", 11, "Cadre de la fonction publique", datetime.datetime(1972,3,6), True]     
        self.__assert_candidate_model(candidate_model_check, candidate)
        
        
    def test_creator_candidate_two_first_name(self) : 
        creator = self.__get_creator_init()
        
        candidate_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','M','Cazenave','Thomas','Eric','1978-06-03 00:00:00','ENS','Cadre de la fonction publique','Non','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
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
        self.assertTrue(candidate_data_check[5] == candidate_model.birthdate)
        self.assertEqual(candidate_data_check[6], candidate_model.is_sorting)
        
        
    #TODO factorize the assert part
    def test_creator_candidate_female_candidate_first_round_data(self) : 
        creator = CreatorCandidate(None)
        
        candidate_data = [ 8, 'F', 'ARMENJON', 'Eliane', 'ECO', '1161', '1.35', '2.78', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(candidate_data)
        
        self.assertEqual('F', candidate.sexe)
        self.assertEqual('ARMENJON', candidate.last_name)
        self.assertEqual('Eliane', candidate.first_name)
        self.assertEqual(1161, candidate.vote)
        self.assertEqual(1.35, candidate.rate_vote_registered)
        self.assertEqual(2.78, candidate.rate_vote_expressed)
        
        
    def test_creator_candidate_male_first_round_data(self) :
        creator = CreatorCandidate(None)
        
        candidate_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(candidate_data)
        
        self.assertEqual('M', candidate.sexe)
        self.assertEqual('THOMASSIN', candidate.last_name)
        self.assertEqual('Geoffrey', candidate.first_name)
        self.assertEqual(216, candidate.vote)
        self.assertEqual(0.27, candidate.rate_vote_registered)
        self.assertEqual(0.54, candidate.rate_vote_expressed)
        
        
    def test_creator_candidate_male_first_vote_bad_formatted(self) : 
        creator = CreatorCandidate(None)
        
        candidate_data = [6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', '216.0', '0.27', '0.54', 'nan']
        
        candidate = creator.factory_candidate_first_round_method(candidate_data)
        
        self.assertEqual('M', candidate.sexe)
        self.assertEqual('THOMASSIN', candidate.last_name)
        self.assertEqual('Geoffrey', candidate.first_name)
        self.assertEqual(216, candidate.vote)
        self.assertEqual(0.27, candidate.rate_vote_registered)
        self.assertEqual(0.54, candidate.rate_vote_expressed)
        
        
    if __name__ == "__main__":
        unittest.main()