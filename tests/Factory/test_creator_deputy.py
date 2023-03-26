import unittest
import datetime

from src.Models.DeputyModel import DeputyModel
from src.Factory.CreatorDeputy import CreatorDeputy
from helper_test import HelperTest

#TODO factoize self assertpart 
class CreatorDeputyTest(unittest.TestCase):
    def test_creator_deputy(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertFalse(deputy.is_sorting)
        
        
    def test_creator_deputy_is_sorting(self):
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertTrue(deputy.is_sorting)
        
        
    def test_creator_deputy_with_candidate_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', 'datetime.datetime(1978, 06, 03, 0, 0)' , 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' ,'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertFalse(deputy.is_sorting)
        
        
    def test_creator_deputy_with_two_first_names(self) : 
        creator = CreatorDeputy(False)
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX' ,'XXXXX' , 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', 'datetime.datetime(1971, 12, 3, 0, 0)', 'Oui']
        
        deputy = creator.factory_method(deputy_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette Georgette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertTrue(deputy.is_sorting)
        
        
    def test_creator_deputy_with_candidate_both_have_two_first_names(self):
        creator = CreatorDeputy(True)
        
        deputy_data = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'M', 'Cazenave', 'Thomas' ,'Eric', 'datetime.datetime(1978, 06, 03, 0, 0)' , 'ENS', 'Cadre de la fonction publique', 'Non', 'F', 'BARTEBIN-SOURHOU', 'Huguette' , 'Georgette', 'datetime.datetime(1971, 12, 3, 0, 0)', 'Non']
        
        deputy = creator.factory_method(deputy_data)
        
        self.assertEqual('F', deputy.sexe)
        self.assertEqual('BARTEBIN-SOURHOU', deputy.last_name)
        self.assertEqual('Huguette Georgette', deputy.first_name)
        self.assertEqual(datetime.datetime(1971,12,3), deputy.birth_date)
        self.assertFalse(deputy.is_sorting)