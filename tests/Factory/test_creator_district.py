import unittest
from src.Factory.CreatorDistrict import CreatorDistrict

from tests.helper_test import HelperTest

class CreatorDistrictTest(unittest.TestCase):
    
    def test_creator_districs_in_gironde_department(self) : 
        creator = CreatorDistrict()
        election_data = ['XXXXX','XXXXX','13','13 ème circonscription','XXXXX','XXXXX','XXXXX','XXXXX']
        
        district = creator.factory_method(election_data)
        
        self.assertEqual(13, district.number)
        self.assertEqual("13 ème circonscription", district.name)
        
        
    if __name__ == "__main__":
        unittest.main()  