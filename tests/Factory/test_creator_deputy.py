import unittest
import datetime

from src.Models.DeputyModel import DeputyModel
from src.Factory.CreatorDeputy import CreatorDeputy
from helper_test import HelperTest

class CreatorDeputyTest(unittest.TestCase):
    def test_creator_deputy(self):
        creator = CreatorDeputy()
        helper = HelperTest()
        candidate_data = helper.get_one_candidate_data_model()
        
        #candidate = creator.factory_method(candidate_data)
        
        #candidate_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(candidate_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertFalse(deputy.is_sorting)
        