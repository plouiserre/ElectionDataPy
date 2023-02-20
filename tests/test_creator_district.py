import unittest
from src.Factory.CreatorDistrict import CreatorDistrict

from tests.helper_test import HelperTest

class CreatorDistrictTest(unittest.TestCase):
    
    def test_creator_districs_in_gironde_department(self) : 
        creator = CreatorDistrict()
        helper = HelperTest()
        candidate_data = helper.get_one_candidate_data_model()   
        
        district = creator.factory_method(candidate_data)
        
        self.assertEqual(1, district.number)
        self.assertEqual("1 ère circonscription", district.name)
        
    if __name__ == "__main__":
        unittest.main()  