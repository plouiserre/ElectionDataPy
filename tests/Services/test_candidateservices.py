import unittest
from mock import Mock

from src.Services.CandidateServices import CandidateServices
from src.Models.DistrictModel import DistrictModel
from src.Models.DepartmentModel import DepartmentModel
from tests.helper_test import HelperTest

#TODO rework this UT
class CandidatesServicesTest(unittest.TestCase) : 
    #TODO dans la liste des districts ajouter le lien des départements et ajouter deux distrits bidons (un rien à voir rien avec tout à voir sauf le dep et en première place)
    #TODO cleaner 
    def test_call_candidate_repository(self) : 
        helper = HelperTest()
        candidates = helper.get_two_candidates_data_model()
        candidate_repository_mock = Mock()
        department_one = DepartmentModel()
        department_one.name = "Ain"
        department_one.number = 1
        district_one = DistrictModel()
        district_one.name = "4ème circonscription"
        district_one.number = 4
        district_one.id = 1
        district_one.department = department_one
        department_two = DepartmentModel()
        department_two.name = "Nord"
        department_two.number = 59
        district_two = DistrictModel()
        district_two.name = "13ème circonscription"
        district_two.number = 13
        district_two.id = 2
        district_two.department = department_two
        department_third = DepartmentModel()
        department_third.name = "Gironde"
        department_third.number = 33
        district_third = DistrictModel()
        district_third.name = "10ème circonscription"
        district_third.number = 10
        district_third.id = 3
        district_third.department = department_third
        department_fourth = DepartmentModel()
        department_fourth.name = "Aisne"
        department_fourth.number = 2
        district_fourth = DistrictModel()
        district_fourth.name = "4ème circonscription"
        district_fourth.number = 4
        district_fourth.id = 4
        district_fourth.department = department_fourth
        dictricts = [district_one, district_two, district_third, district_fourth]
        
        candidate_service = CandidateServices()
        candidate_service.manage_candidates(candidates, candidate_repository_mock, dictricts)
        candidates = candidate_service.candidates
        
        self.assertTrue(candidate_repository_mock.save_candidates.called)
        self.assertEqual(2, len(candidates))
        self.assertEqual(4, candidates[0].district_id)
        self.assertEqual(2, candidates[1].district_id)
        