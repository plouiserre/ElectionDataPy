import unittest
import datetime

from src.Factory.CreatorDeputy import CreatorDeputy
from tests.assert_test import AssertTest

class CreatorDeputyTest(unittest.TestCase):
    def test_creator_deputy(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Bond' ,'James' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'1971-12-03 00:00:00', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), False, 'Bond', 'James']  
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_is_sorting(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Addams' ,'Mercredi' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'1971-12-03 00:00:00', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), True, 'Addams', 'Mercredi']  
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 
        
      
    def test_creator_birthdate_format_different(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Shelby' ,'Thomas' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'1972-12-03 00:00:00', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1972,12,3), False, 'Shelby', 'Thomas']    
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_candidate_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', '1978-06-03 00:00:00', 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'1971-12-03 00:00:00', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), False, 'Cazenave', 'Thomas Eric']  
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_two_first_names(self) : 
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'Lannister' ,'Tyrion' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', '1971-12-03 00:00:00', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette Georgette", "F", datetime.datetime(1971,12,3), True, 'Lannister', 'Tyrion']    
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_candidate_both_have_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', '1978-06-03 00:00:00', 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', '1971-12-03 00:00:00', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette Georgette", "F", datetime.datetime(1971,12,3), False, 'Cazenave', 'Thomas Eric']  
        assert_test = AssertTest(self, 0) 
        assert_test.assert_deputy_model(deputy_model_check, deputy) 