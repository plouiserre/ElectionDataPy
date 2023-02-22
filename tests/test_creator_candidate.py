import unittest
from src.Factory.CreatorCandidate import CreatorCandidate
#from src.Models.CandidateDataModel import CandidateDataModel

from tests.helper_test import HelperTest

class CreatorCandidateTest(unittest.TestCase):
    def test_creator_candidate_from_gironde(self) : 
        creator = CreatorCandidate()
        helper = HelperTest()
        candidate_data = helper.get_one_candidate_data_model()
        
        candidate = creator.factory_method(candidate_data)
        
        self.assertEqual("06/03/1978", candidate.birth_date)
        self.assertEqual("Thomas", candidate.first_name)
        self.assertEqual("Cazenave", candidate.last_name)
        self.assertEqual(False, candidate.is_sorting)
        self.assertEqual("Cadre de la fonction publique", candidate.job)
        self.assertEqual("ENS", candidate.party)
        self.assertEqual("M", candidate.sexe)
        

    if __name__ == "__main__":
        unittest.main()