import unittest


class BaseUnitTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)        
    
    def assert_candidate_model(self, candidate_data_check, candidate_data_model) :
        self.assertEqual(candidate_data_check[0], candidate_data_model.department.number)
        self.assertEqual(candidate_data_check[1], candidate_data_model.department.name)
        self.assertEqual(candidate_data_check[2], candidate_data_model.district.number)
        self.assertEqual(candidate_data_check[3], candidate_data_model.district.name)
        self.assertEqual(candidate_data_check[4], candidate_data_model.district.department.number)
        self.assertEqual(candidate_data_check[5], candidate_data_model.district.department.name)
        self.assertEqual(candidate_data_check[6], candidate_data_model.candidates[0].last_name)
        self.assertEqual(candidate_data_check[7], candidate_data_model.candidates[0].first_name)
        self.assertEqual(candidate_data_check[8], candidate_data_model.candidates[0].sexe)
        self.assertEqual(candidate_data_check[9], candidate_data_model.candidates[0].party_id)
        self.assertEqual(candidate_data_check[10], candidate_data_model.candidates[0].job)
        self.assertTrue(candidate_data_check[11] == candidate_data_model.candidates[0].birthdate)
        self.assertEqual(candidate_data_check[12], candidate_data_model.candidates[0].is_sorting)
        
        self.assertEqual(candidate_data_check[13], candidate_data_model.deputies[0].sexe)
        self.assertEqual(candidate_data_check[14], candidate_data_model.deputies[0].last_name)
        self.assertEqual(candidate_data_check[15], candidate_data_model.deputies[0].first_name)
        self.assertTrue(candidate_data_check[16] == candidate_data_model.deputies[0].birthdate)
        self.assertEqual(candidate_data_check[17], candidate_data_model.deputies[0].is_sorting)
        self.assertEqual(candidate_data_check[6], candidate_data_model.deputies[0].candidate.last_name)
        self.assertEqual(candidate_data_check[7], candidate_data_model.deputies[0].candidate.first_name)
       