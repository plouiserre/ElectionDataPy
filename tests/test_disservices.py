import unittest
from mock import Mock
from unittest.mock import patch

from src.Services.DistrictServices import DistrictServices
from src.Models.DepartmentModel import DepartmentModel

from src.Repository.DistrictRepository import DistrictRepository

from tests.helper_test import HelperTest

#TODO add departments in helper too
class DistrictServicesTest(unittest.TestCase): 
        
    def test_construct_districts_two_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_two_candidates()
        first_department = DepartmentModel()
        first_department.id = 66
        first_department.name = "Aisne"
        first_department.number = 2
        second_department = DepartmentModel()
        second_department.id = 67
        second_department.name = "Nord"
        second_department.number = 59
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        
        dis_repo = Mock()
        dis = DistrictServices()
        dis.manage_districts(candidates, departments, dis_repo)        
        districts = dis.districts
        
        self.assertEqual(2, len(districts))
        self.assertEqual(4, districts[0].number)
        self.assertEqual("4ème circonscription", districts[0].name)
        self.assertEqual(66, districts[0].department_id)
        self.assertEqual(13, districts[1].number)
        self.assertEqual("13ème circonscription", districts[1].name)
        self.assertEqual(67, districts[1].department_id)
        
        
    def test_construct_districts_many_candidates(self) : 
        helper = HelperTest()
        candidates = helper.get_six_candidates()
        first_department = DepartmentModel()
        first_department.id = 65
        first_department.name = "Ain"
        first_department.number = 1
        second_department = DepartmentModel()
        second_department.id = 66
        second_department.name = "Aisne"
        second_department.number = 2
        third_department = DepartmentModel()
        third_department.id = 67
        third_department.name = "Alpes-de-Haute-Provence"
        third_department.number = 4
        fourth_department = DepartmentModel()
        fourth_department.id = 68
        fourth_department.name = "Alpes-Maritimes"
        fourth_department.number = 6
        fifth_department = DepartmentModel()
        fifth_department.id = 69
        fifth_department.name = "Aube"
        fifth_department.number = 10
        sixth_department = DepartmentModel()
        sixth_department.id = 70
        sixth_department.name = "Nord"
        sixth_department.number = 59
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        departments.update({third_department.number : third_department}) 
        departments.update({fourth_department.number : fourth_department})
        departments.update({fifth_department.number : fifth_department}) 
        departments.update({sixth_department.number : sixth_department})
        
        dis_repo = Mock()
        dis = DistrictServices()
        dis.manage_districts(candidates, departments, dis_repo)       
        districts = dis.districts
        
        self.assertEqual(6, len(districts))
        self.assertEqual(1, districts[0].number)
        self.assertEqual("1ère circonscription", districts[0].name)
        self.assertEqual(65, districts[0].department_id)
        self.assertEqual(4, districts[1].number)
        self.assertEqual("4ème circonscription", districts[1].name)
        self.assertEqual(66, districts[1].department_id)
        self.assertEqual(2, districts[2].number)
        self.assertEqual("2ème circonscription", districts[2].name)
        self.assertEqual(67, districts[2].department_id)
        self.assertEqual(6, districts[3].number)
        self.assertEqual("6ème circonscription", districts[3].name)
        self.assertEqual(68, districts[3].department_id)
        self.assertEqual(1, districts[4].number)
        self.assertEqual("1ère circonscription", districts[4].name)
        self.assertEqual(69, districts[4].department_id)
        self.assertEqual(13, districts[5].number)
        self.assertEqual("13ème circonscription", districts[5].name)
        self.assertEqual(70, districts[5].department_id)
        
        
    def test_construct_districts_neighbourg_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_eigth_candidates()
        first_department = DepartmentModel()
        first_department.id = 65
        first_department.name = "Ain"
        first_department.number = 1
        second_department = DepartmentModel()
        second_department.id = 66
        second_department.name = "Aisne"
        second_department.number = 2
        third_department = DepartmentModel()
        third_department.id = 67
        third_department.name = "Alpes-de-Haute-Provence"
        third_department.number = 4
        fourth_department = DepartmentModel()
        fourth_department.id = 68
        fourth_department.name = "Alpes-Maritimes"
        fourth_department.number = 6
        fifth_department = DepartmentModel()
        fifth_department.id = 69
        fifth_department.name = "Aube"
        fifth_department.number = 10
        sixth_department = DepartmentModel()
        sixth_department.id = 70
        sixth_department.name = "Nord"
        sixth_department.number = 59
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        departments.update({third_department.number : third_department}) 
        departments.update({fourth_department.number : fourth_department})
        departments.update({fifth_department.number : fifth_department}) 
        departments.update({sixth_department.number : sixth_department})
        
        dis_repo = Mock()
        dis = DistrictServices()
        dis.manage_districts(candidates, departments, dis_repo)    
        districts = dis.districts
        
        self.assertEqual(6, len(districts))
        self.assertEqual(1, districts[0].number)
        self.assertEqual("1ère circonscription", districts[0].name)
        self.assertEqual(65, districts[0].department_id)
        self.assertEqual(4, districts[1].number)
        self.assertEqual("4ème circonscription", districts[1].name)
        self.assertEqual(66, districts[1].department_id)
        self.assertEqual(2, districts[2].number)
        self.assertEqual("2ème circonscription", districts[2].name)
        self.assertEqual(67, districts[2].department_id)
        self.assertEqual(6, districts[3].number)
        self.assertEqual("6ème circonscription", districts[3].name)
        self.assertEqual(68, districts[3].department_id)
        self.assertEqual(1, districts[4].number)
        self.assertEqual("1ère circonscription", districts[4].name)
        self.assertEqual(69, districts[4].department_id)
        self.assertEqual(13, districts[5].number)
        self.assertEqual("13ème circonscription", districts[5].name)
        self.assertEqual(70, districts[5].department_id)        
    
    
    @patch.object(DistrictRepository, 'save_districts')
    def test_districts_repository_save_districts_called(self, mock_districtrepository) :
        dis_repo = DistrictRepository()
        district_services = DistrictServices()
        
        district_services.manage_districts([],[],dis_repo)
        
        self.assertTrue(mock_districtrepository.called)