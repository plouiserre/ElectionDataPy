import unittest
from mock import Mock

from src.Services.CandidateServices import CandidateServices
from tests.helper_test import HelperTest

#TODO rework this UT
class CandidatesServicesTest(unittest.TestCase) : 
    
    def test_call_candidate_repository(self) : 
        helper = HelperTest()
        candidates = helper.get_two_candidates_data_model()
        candidate_repository_mock = Mock()
        
        candidate_service = CandidateServices()
        candidate_service.manage_candidates(candidates, candidate_repository_mock)
        
        self.assertTrue(candidate_repository_mock.save_candidates.called)
        