import unittest
import datetime

from mock import Mock
from src.Services.DeputyServices import DeputyServices
from src.Repository.DeputyRepository import DeputyRepository
from helper_test import HelperTest

class DeputyServicesTest(unittest.TestCase) :
    
    def test_construct_deputies_two_candidates(self) : 
        helper = HelperTest()
        deputy_services = DeputyServices()
        deputy_repository = Mock()
        candidates_data_model = helper.get_two_candidates_data_model()
        candidates = helper.get_two_candidates_model()
        
        deputy_services.manage_deputies(candidates_data_model, candidates, deputy_repository)
        deputies = deputy_services.deputies
        
        self.assertEqual(2, len(deputies))
        self.assertTrue(datetime.datetime(2002, 4, 2) == deputies[0].birthdate)
        self.assertEqual("Enid", deputies[0].first_name)
        self.assertEqual("Sinclair", deputies[0].last_name)
        self.assertFalse(deputies[0].is_sorting)
        self.assertEqual(1, deputies[0].candidate.id)
        self.assertTrue(datetime.datetime(1968, 8,17) == deputies[1].birthdate)
        self.assertEqual("Polly", deputies[1].first_name)
        self.assertEqual("Gray", deputies[1].last_name)
        self.assertTrue(deputies[1].is_sorting)
        self.assertEqual(2, deputies[1].candidate.id)