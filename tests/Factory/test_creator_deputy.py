import unittest
import datetime

from src.Models.DeputyModel import DeputyModel
from src.Factory.CreatorDeputy import CreatorDeputy
from helper_test import HelperTest

class CreatorDeputyTest(unittest.TestCase):
    def test_creator_deputy(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), False]   
        self.__assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_is_sorting(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), True]   
        self.__assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_candidate_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', 'datetime.datetime(1978, 06, 03, 0, 0)' , 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette", "F", datetime.datetime(1971,12,3), False]   
        self.__assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_two_first_names(self) : 
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', 'datetime.datetime(1971, 12, 3, 0, 0)', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette Georgette", "F", datetime.datetime(1971,12,3), True]   
        self.__assert_deputy_model(deputy_model_check, deputy) 
        
        
    def test_creator_deputy_with_candidate_both_have_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', 'datetime.datetime(1978, 06, 03, 0, 0)' , 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', 'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        deputy_model_check = ["BARTEBIN-SOURHOU", "Huguette Georgette", "F", datetime.datetime(1971,12,3), False]   
        self.__assert_deputy_model(deputy_model_check, deputy)  
        
        
    def  __assert_deputy_model(self, deputy_data_check, deputy_model) :
        self.assertEqual(deputy_data_check[0], deputy_model.last_name)
        self.assertEqual(deputy_data_check[1], deputy_model.first_name)
        self.assertEqual(deputy_data_check[2], deputy_model.sexe)
        self.assertTrue(deputy_data_check[3] == deputy_model.birth_date)
        self.assertEqual(deputy_data_check[4], deputy_model.is_sorting)