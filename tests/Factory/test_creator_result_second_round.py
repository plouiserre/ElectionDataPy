import unittest

from src.Factory.CreatorResultSecondRound import CreatorResultSecondRound
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorResultSecondRoundTest(unittest.TestCase) :
    
    #TODO quand j'aurai fait toute la chaîne il faudra surement modifier les results_data
    def test_creator_first_line(self) :
        creator = CreatorResultSecondRound(None)
        
        result_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Complet', '327 172', '52.6', 155, '47.4', 4, '1.22', '2.58', 5, '1.53', '3.23', 146 ,'44.65', '94.19', 'XXXXX', 'XXXXX']
        result_model = creator.factory_method(result_data)
        
        result_context_check = ['Complet', 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146 , 44.65, 94.19]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, result_model)
        
        
    def test_creator_second_line_with_one_last_election_data_created(self) :
        helper = HelperTest()
        last_election_data_created = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorResultSecondRound(last_election_data_created)
        
        result_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Complet', '604 317', '52.48', 287, '47.52', 6, '0.99', '2.09', 6, '0.99', '2.09', 275, '45.53', '95.82', 'XXXXX', 'XXXXX']
        result_model = creator.factory_method(result_data)
        
        result_context_check = ['Complet', 931, 489, 52.54, 442, 47.46, 10, 1.105, 2.335, 11, 1.26, 2.66, 421, 45.09, 95.005]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, result_model)