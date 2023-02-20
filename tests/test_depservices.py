import unittest
from mock import Mock
from unittest.mock import patch

from src.Repository.DepartmentRepository import DepartmentRepository
from src.Repository.mydb import MyDb

from src.Services.DepartmentServices import DepartmentServices

from tests.helper_test import HelperTest

class DepartmentServicesTest(unittest.TestCase):   
    def test_construct_departments_two_candidates(self) :        
        helper = HelperTest()
        candidates = helper.get_two_candidates_data_model()
        
        departments = self.call_manage_departments(candidates)
        
        self.assertEqual(2, len(departments))
        self.assertEqual(2, departments[2].number)
        self.assertEqual("Aisne", departments[2].name)
        self.assertEqual(59, departments[59].number)
        self.assertEqual("Nord", departments[59].name)
        
        
    def test_construct_departments_many_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_six_candidates_data_model()
        
        departments = self.call_manage_departments(candidates)
        
        self.assertEqual(6, len(candidates))
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
              
        departments = self.call_manage_departments(candidates)
        
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
        
        
    def call_manage_departments(self, candidates) : 
        dep_repo = Mock()
        dep = DepartmentServices()
        dep.manage_departments(candidates, dep_repo)        
        return dep.departments
        
        
    @patch.object(DepartmentRepository,'save_departments')
    def test_deparments_repository_save_departments_called(self, mock_departmentrepository) : 
        mydb = MyDb()
        dep_repo = DepartmentRepository(mydb)
        department_services = DepartmentServices()
        
        department_services.manage_departments([], dep_repo)
        
        self.assertTrue(mock_departmentrepository.called)
        
    if __name__ == "__main__":
        unittest.main()