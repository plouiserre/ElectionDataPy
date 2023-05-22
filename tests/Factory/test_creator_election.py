import unittest

from src.Factory.CreatorElection import CreatorElection
from tests.assert_test import AssertTest

class CreatorElectionTest(unittest.TestCase) : 
     #TODO factoriser code 
     #TODO factorize this assert part
    def test_creator_election_first_line(self) : 
        creator = CreatorElection()
        
        election_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', '86187 43652', '50.65', '42535', '49.35', '490', '0.57', '1.15', '234', '0.27', '0.55', '41811', '48.51', '98.3', 'XXXX', 'XXXX', 'XXXX' ]
        election_model = creator.factory_method(election_data)
        
        election_context_check = ['Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3]
        assert_test = AssertTest(self, 1)
        assert_test.assert_election_data_first_round_election(election_context_check, election_model)
        
        
    def test_creator_election_second_line(self) :
        creator = CreatorElection()
        
        election_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', '80824 35239', '43.6', '45585', '56.4', '457', '0.57', '1', '192', '0.24', '0.42', '44936', '55.6', '98.58', 'XXXX', 'XXXX', 'XXXX']
        election_model = creator.factory_method(election_data)     
        
        election_context_check = ['Complet', 80824, 35239, 43.6, 45585, 56.4, 457, 0.57, 1, 192, 0.24, 0.42, 44936, 55.6, 98.58]
        assert_test = AssertTest(self, 1)
        assert_test.assert_election_data_first_round_election(election_context_check, election_model)