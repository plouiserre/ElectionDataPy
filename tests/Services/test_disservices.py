import unittest
from mock import Mock

from src.Services.DistrictServices import DistrictServices
from src.Models.DepartmentModel import DepartmentModel

from tests.helper_test import HelperTest

class DistrictServicesTest(unittest.TestCase): 
    
    def test_construct_districts_two_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_two_candidates_data_model()
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
        dis.store_districts(candidates, departments, dis_repo)        
        districts = dis.districts
        
        self.assertEqual(2, len(districts))
        self.assertEqual(4, districts[0].number)
        self.assertEqual("4ème circonscription", districts[0].name)
        self.assertEqual(66, districts[0].department.id)
        self.assertEqual(13, districts[1].number)
        self.assertEqual("13ème circonscription", districts[1].name)
        self.assertEqual(67, districts[1].department.id)
        
    def test_construct_districts_neighbourg_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_eight_candidates_data_model()
        departments = helper.get_six_departments()
        
        dis_repo = Mock()
        dis = DistrictServices()
        dis.store_districts(candidates, departments, dis_repo)    
        districts = dis.districts
        
        self.assertEqual(6, len(districts))
        self.assertEqual(1, districts[0].number)
        self.assertEqual("1ère circonscription", districts[0].name)
        self.assertEqual(65, districts[0].department.id)
        self.assertEqual(4, districts[1].number)
        self.assertEqual("4ème circonscription", districts[1].name)
        self.assertEqual(66, districts[1].department.id)
        self.assertEqual(2, districts[2].number)
        self.assertEqual("2ème circonscription", districts[2].name)
        self.assertEqual(67, districts[2].department.id)
        self.assertEqual(6, districts[3].number)
        self.assertEqual("6ème circonscription", districts[3].name)
        self.assertEqual(68, districts[3].department.id)
        self.assertEqual(1, districts[4].number)
        self.assertEqual("1ère circonscription", districts[4].name)
        self.assertEqual(69, districts[4].department.id)
        self.assertEqual(13, districts[5].number)
        self.assertEqual("13ème circonscription", districts[5].name)
        self.assertEqual(70, districts[5].department.id) 
        
        
    def test_construct_districts_corsica_candidates(self) :
        helper = HelperTest()
        candidates = helper.get_two_corsica_candidates_data_model()
        first_department = DepartmentModel()
        first_department.id = 65
        first_department.name = "Corse"
        first_department.number = 20
        second_department = DepartmentModel()
        second_department.id = 65
        second_department.name = "Corse"
        second_department.number = 20
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        
        dis_repo = Mock()
        dis = DistrictServices()
        dis.store_districts(candidates, departments, dis_repo)    
        districts = dis.districts
        
        self.assertEqual(2, len(districts))
        self.assertEqual(4, districts[0].number)
        self.assertEqual("4ème circonscription", districts[0].name)
        self.assertEqual(65, districts[0].department.id)
        self.assertEqual(13, districts[1].number) 
        self.assertEqual("13ème circonscription", districts[1].name)        
        self.assertEqual(65, districts[1].department.id)        
        
    
    def test_districts_repository_save_districts_called(self) :
        mock_dependency = Mock()
        district_services = DistrictServices()
        
        district_services.store_districts([],[],mock_dependency)
        
        self.assertTrue(mock_dependency.get_dependency.called)
        
    if __name__ == "__main__":
        unittest.main()