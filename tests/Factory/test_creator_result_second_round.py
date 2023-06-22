import unittest

from src.Factory.CreatorResultSecondRound import CreatorResultSecondRound
from src.Models.ResultModel import ResultModel
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorResultSecondRoundTest(unittest.TestCase) :
    
    def test_creator_first_line(self) :
        creator = CreatorResultSecondRound([])
        
        result_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Complet', '327 172', '52.6', 155, '47.4', 4, '1.22', '2.58', 5, '1.53', '3.23', 146 ,'44.65', '94.19', 'XXXXX', 'XXXXX']
        result_model = creator.factory_method(result_data)
        last_result_model_created = creator.last_element_created
        
        result_context_check = ['Complet', 2, 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146 , 44.65, 94.19]
        assert_test = AssertTest(self, 1)
       
        assert_test.assert_result_data_rounds_result(result_context_check, result_model)
        assert_test.assert_result_data_rounds_result(result_context_check, last_result_model_created)   
             
        
    def test_creator_second_line_with_one_last_election_data_created(self) :
        helper = HelperTest()
        last_election_data_created = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorResultSecondRound(last_election_data_created)
        
        result_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Complet', '604 317', '52.48', 287, '47.52', 6, '0.99', '2.09', 6, '0.99', '2.09', 275, '45.53', '95.82', 'XXXXX', 'XXXXX']
        result_model = creator.factory_method(result_data)
        last_result_model_created = creator.last_element_created
        
        result_context_check = ['Complet', 2, 931, 489, 52.54, 442, 47.46, 10, 1.105, 2.335, 11, 1.26, 2.66, 421, 45.09, 95.005]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, result_model)
        
        result_context_check = ['Complet', 2, 604, 317, 52.48, 287, 47.52, 6, 0.99, 2.09, 6, 0.99, 2.09, 275, 45.53, 95.82]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, last_result_model_created)
        
        
    def test_creator_result_with_two_last_election_data_created_second_round_data(self) :  
        helper = HelperTest()
        last_election_data_created = helper.get_two_cities_data_first_department_first_district_last_election_data_model()
        creator = CreatorResultSecondRound(last_election_data_created)
        
        result_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Complet', '446 239', '53.59', 207, '46.41', 10, '2.24', '4.83', 2, '0.45', '0.97', 195, '43.72', '94.2', 'XXXXX', 'XXXXX']
        result_model = creator.factory_method(result_data)
        last_result_model_created = creator.last_element_created
        
        result_context_check = ['Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, result_model)
        
        result_context_check = ['Complet', 2, 446, 239, 53.59, 207, 46.41, 10, 2.24, 4.83, 2, 0.45, 0.97, 195, 43.72, 94.2]
        assert_test = AssertTest(self, 1)
        assert_test.assert_result_data_rounds_result(result_context_check, last_result_model_created)