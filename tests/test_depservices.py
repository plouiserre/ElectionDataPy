import unittest
from unittest.mock import patch

from src.Services.DepartmentServices import DepartmentServices

from src.Repository.DepartmentRepository import DepartmentRepository

from tests.helper_test import HelperTest

#TODO mock repository to prevent insert in database
#TODO put an contrustor to factorize the code

class DepartmentServicesTest(unittest.TestCase):
    def test_construct_departments_two_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_two_candidates()
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        dep.manage_departments(candidates, dep_repo)        
        departments = dep.departments
        
        self.assertEqual(2, len(departments))
        self.assertEqual(2, departments[0].number)
        self.assertEqual("Aisne", departments[0].name)
        self.assertEqual(59, departments[1].number)
        self.assertEqual("Nord", departments[1].name)
        
        
    def test_construct_departments_many_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_six_candidates()
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        dep.manage_departments(candidates, dep_repo)        
        departments = dep.departments
        
        self.assertEqual(6, len(candidates))
        self.assertEqual(1, departments[0].number)
        self.assertEqual("Ain", departments[0].name)
        self.assertEqual(2, departments[1].number)
        self.assertEqual("Aisne", departments[1].name)
        self.assertEqual(4, departments[2].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[2].name)
        self.assertEqual(6, departments[3].number)
        self.assertEqual("Alpes-Maritimes", departments[3].name)
        self.assertEqual(10, departments[4].number)
        self.assertEqual("Aube", departments[4].name)
        self.assertEqual(59, departments[5].number)
        self.assertEqual("Nord", departments[5].name)
        
    def test_construct_departments_neighbourg_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_eigth_candidates()
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        dep.manage_departments(candidates, dep_repo)        
        departments = dep.departments
        
        self.assertEqual(6, len(departments ))
        self.assertEqual(1, departments[0].number)
        self.assertEqual("Ain", departments[0].name)
        self.assertEqual(2, departments[1].number)
        self.assertEqual("Aisne", departments[1].name)
        self.assertEqual(4, departments[2].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[2].name)
        self.assertEqual(6, departments[3].number)
        self.assertEqual("Alpes-Maritimes", departments[3].name)
        self.assertEqual(10, departments[4].number)
        self.assertEqual("Aube", departments[4].name)
        self.assertEqual(59, departments[5].number)
        self.assertEqual("Nord", departments[5].name)
        
        
    @patch.object(DepartmentRepository,'save_departments')
    def test_deparments_repository_save_departments_called(self, mock_departmentrepository) : 
        dep_repo = DepartmentRepository()
        department_services = DepartmentServices()
        
        department_services.manage_departments([], dep_repo)
        
        self.assertTrue(mock_departmentrepository.called)