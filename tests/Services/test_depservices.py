import unittest
from mock import Mock

from src.Services.DepartmentServices import DepartmentServices

from tests.helper_test import HelperTest

class DepartmentServicesTest(unittest.TestCase):   
    def test_construct_departments_two_candidates(self) :        
        helper = HelperTest()
        elections = helper.get_two_elections_data_model()
        
        departments = self.call_store_departments(elections)
        
        self.assertEqual(2, len(departments))
        self.assertEqual(2, departments[2].number)
        self.assertEqual("Aisne", departments[2].name)
        self.assertEqual(59, departments[59].number)
        self.assertEqual("Nord", departments[59].name)
        
        
    def test_construct_departments_many_candidates(self) :
        helper = HelperTest()
        elections = helper.get_six_elections_data_model()
        
        departments = self.call_store_departments(elections)
        
        self.assertEqual(6, len(elections))
        self.assertEqual(1, departments[1].number)
        self.assertEqual("Ain", departments[1].name)
        self.assertEqual(2, departments[2].number)
        self.assertEqual("Aisne", departments[2].name)
        self.assertEqual(4, departments[4].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[4].name)
        self.assertEqual(6, departments[6].number)
        self.assertEqual("Alpes-Maritimes", departments[6].name)
        self.assertEqual(10, departments[10].number)
        self.assertEqual("Aube", departments[10].name)
        self.assertEqual(59, departments[59].number)
        self.assertEqual("Nord", departments[59].name)
        
    def test_construct_departments_neighbourg_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_eight_candidates_data_model()        
              
        departments = self.call_store_departments(candidates)
        
        self.assertEqual(6, len(departments ))
        self.assertEqual(1, departments[1].number)
        self.assertEqual("Ain", departments[1].name)
        self.assertEqual(2, departments[2].number)
        self.assertEqual("Aisne", departments[2].name)
        self.assertEqual(4, departments[4].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[4].name)
        self.assertEqual(6, departments[6].number)
        self.assertEqual("Alpes-Maritimes", departments[6].name)
        self.assertEqual(10, departments[10].number)
        self.assertEqual("Aube", departments[10].name)
        self.assertEqual(59, departments[59].number)
        self.assertEqual("Nord", departments[59].name)
        
        
    def call_store_departments(self, candidates) : 
        dep_repo = Mock()
        dep = DepartmentServices()
        dep.store_departments(candidates, dep_repo)        
        return dep.departments
        
        
    def test_deparments_repository_save_departments_called(self) : 
        mock_dependency = Mock()
        department_services = DepartmentServices()
        
        department_services.store_departments([], mock_dependency)
        
        self.assertTrue(mock_dependency.get_dependency.called)
        
    if __name__ == "__main__":
        unittest.main()