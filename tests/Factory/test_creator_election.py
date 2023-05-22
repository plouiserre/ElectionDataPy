import unittest

from src.Factory.CreatorResult import CreatorResult
from tests.assert_test import AssertTest

class CreatorResultTest(unittest.TestCase) : 
     #TODO factoriser code 
     #TODO factorize this assert part
    def test_creator_result_first_line(self) : 
        creator = CreatorResult()
        
        result_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', '86187 43652', '50.65', '42535', '49.35', '490', '0.57', '1.15', '234', '0.27', '0.55', '41811', '48.51', '98.3', 'XXXX', 'XXXX', 'XXXX' ]
        result_model = creator.factory_method(result_data)
        
        result_context_check = ['Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_first_round_result(result_context_check, result_model)
        
        
    def test_creator_result_second_line(self) :
        creator = CreatorResult()
        
        result_data = ['XXXX', 'XXXX', 'XXXX', 'XXXX', 'Complet', '80824 35239', '43.6', '45585', '56.4', '457', '0.57', '1', '192', '0.24', '0.42', '44936', '55.6', '98.58', 'XXXX', 'XXXX', 'XXXX']
        result_model = creator.factory_method(result_data)     
        
        result_context_check = ['Complet', 80824, 35239, 43.6, 45585, 56.4, 457, 0.57, 1, 192, 0.24, 0.42, 44936, 55.6, 98.58]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_first_round_result(result_context_check, result_model)