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
        self.assertEqual(candidate_data_check[6], candidate_data_model.candidate.last_name)
        self.assertEqual(candidate_data_check[7], candidate_data_model.candidate.first_name)
        self.assertEqual(candidate_data_check[8], candidate_data_model.candidate.sexe)
        self.assertEqual(candidate_data_check[9], candidate_data_model.candidate.party_id)
        self.assertEqual(candidate_data_check[10], candidate_data_model.candidate.job)
        self.assertTrue(candidate_data_check[11] == candidate_data_model.candidate.birth_date)
        #TODO refaire cette partie
        self.assertEqual(candidate_data_check[12], candidate_data_model.candidate_is_sorting)
        
        self.assertEqual(candidate_data_check[13], candidate_data_model.deputy.sexe)
        self.assertEqual(candidate_data_check[14], candidate_data_model.deputy.last_name)
        self.assertEqual(candidate_data_check[15], candidate_data_model.deputy.first_name)
        self.assertTrue(candidate_data_check[16] == candidate_data_model.deputy.birth_date)
        self.assertEqual(candidate_data_check[17], candidate_data_model.deputy.is_sorting)
        
        
        
       #model = creator.factory_method("['M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']")
       