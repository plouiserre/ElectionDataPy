import unittest

from src.Factory.CreatorElection import CreatorElection
from Models.ElectionModel import ElectionModel

class CreatorElectionTest(unittest.TestCase) : 
     #TODO factoriser code 
    def test_creator_election_first_line(self) : 
        creator = CreatorElection()
        
        election_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', 86187, 43652, '50.65', 42535, '49.35', 490, '0.57', '1.15', 234, '0.27', '0.55', 41811, '48.51', '98.3', 'XXXX', 'XXXX', 'XXXX' ]
        election = creator.factory_method(election_data)
        
        self.assertEqual('Complet', election.state_compute)
        self.assertEqual(86187, election.registered)
        self.assertEqual(43652, election.abstaining)
        self.assertEqual(50.65, election.rate_abstaining)
        self.assertEqual(42535, election.voting)
        self.assertEqual(49.35, election.rate_voting)  
        self.assertEqual(490, election.blank_balot)    
        self.assertEqual(0.57, election.rate_blank_registered)   
        self.assertEqual(1.15, election.rate_blank_voting)       
        self.assertEqual(234, election.null_ballot)  
        self.assertEqual(0.27, election.rate_null_registered)  
        self.assertEqual(0.55, election.rate_null_voting)  
        self.assertEqual(41811, election.expressed)  
        self.assertEqual(48.51, election.rate_express_registered)  
        self.assertEqual(98.3, election.rate_express_voting)  
        
        
    def test_creator_election_second_line(self) :
        creator = CreatorElection()
        
        election_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', 80824, 35239, '43.6', 45585, '56.4', 457, '0.57', '1', 192, '0.24', '0.42', 44936, '55.6', '98.58', 'XXXX', 'XXXX', 'XXXX']
        election = creator.factory_method(election_data)
        
        self.assertEqual('Complet', election.state_compute)
        self.assertEqual(80824, election.registered)
        self.assertEqual(35239, election.abstaining)
        self.assertEqual(43.6, election.rate_abstaining)
        self.assertEqual(45585, election.voting)
        self.assertEqual(56.4, election.rate_voting)  
        self.assertEqual(457, election.blank_balot)    
        self.assertEqual(0.57, election.rate_blank_registered)   
        self.assertEqual(1, election.rate_blank_voting)        
        self.assertEqual(192, election.null_ballot)  
        self.assertEqual(0.24, election.rate_null_registered)  
        self.assertEqual(0.42, election.rate_null_voting)  
        self.assertEqual(44936, election.expressed)  
        self.assertEqual(55.6, election.rate_express_registered)  
        self.assertEqual(98.58, election.rate_express_voting)  
        
        
    