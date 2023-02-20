import unittest
from src.Factory.CreatorDepartment import CreatorDepartment
#from src.Models.CandidateDataModel import CandidateDataModel

from tests.helper_test import HelperTest

class CreatorDepartmentTest(unittest.TestCase):
    def test_creator_department_gironde(self) : 
        creator = CreatorDepartment()
        helper = HelperTest()
        candidate_data = helper.get_one_candidate_data_model()
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(33, department.number)
        self.assertEqual("Gironde", department.name)

    if __name__ == "__main__":
        unittest.main()