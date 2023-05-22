#TODO have all method assert

class AssertTest : 

    #TODO rename properties
    def __init__(self, unit_test, candidates_number) :
        self.unit_test = unit_test
        self.candidates_number = candidates_number
        
        
    def assert_all_candidates_infos_with_deputy(self, candidate_data_check, candidate_data_model) :
        self.unit_test.assertEqual(candidate_data_check[0], candidate_data_model.department.number)
        self.unit_test.assertEqual(candidate_data_check[1], candidate_data_model.department.name)
        self.unit_test.assertEqual(candidate_data_check[2], candidate_data_model.district.number)
        self.unit_test.assertEqual(candidate_data_check[3], candidate_data_model.district.name)
        self.unit_test.assertEqual(candidate_data_check[4], candidate_data_model.district.department.number)
        self.unit_test.assertEqual(candidate_data_check[5], candidate_data_model.district.department.name)
        self.unit_test.assertEqual(candidate_data_check[6], candidate_data_model.candidates[0].last_name)
        self.unit_test.assertEqual(candidate_data_check[7], candidate_data_model.candidates[0].first_name)
        self.unit_test.assertEqual(candidate_data_check[8], candidate_data_model.candidates[0].sexe)
        self.unit_test.assertEqual(candidate_data_check[9], candidate_data_model.candidates[0].party_id)
        self.unit_test.assertEqual(candidate_data_check[10], candidate_data_model.candidates[0].job)
        self.unit_test.assertTrue(candidate_data_check[11] == candidate_data_model.candidates[0].birthdate)
        self.unit_test.assertEqual(candidate_data_check[12], candidate_data_model.candidates[0].is_sorting)
        
        self.unit_test.assertEqual(candidate_data_check[13], candidate_data_model.deputies[0].sexe)
        self.unit_test.assertEqual(candidate_data_check[14], candidate_data_model.deputies[0].last_name)
        self.unit_test.assertEqual(candidate_data_check[15], candidate_data_model.deputies[0].first_name)
        self.unit_test.assertTrue(candidate_data_check[16] == candidate_data_model.deputies[0].birthdate)
        self.unit_test.assertEqual(candidate_data_check[17], candidate_data_model.deputies[0].is_sorting)
        self.unit_test.assertEqual(candidate_data_check[6], candidate_data_model.deputies[0].candidate.last_name)
        self.unit_test.assertEqual(candidate_data_check[7], candidate_data_model.deputies[0].candidate.first_name)
        
        
    #TODO after name change remove data in names
    def assert_election_data_model_with_all_infos(self, election_data_check, election_data_model) : 
        department_data_check = election_data_check[0 : 2]
        self.__assert_candidate_department_data_first_round_election(department_data_check, election_data_model.department)
        district_data_check = election_data_check[2 : 4]
        self.__assert_candidate_district_data_first_round_election(district_data_check, election_data_model.district)
        candidate_data_check = election_data_check[4 : 14]
        self.__assert_all_candidates_data(candidate_data_check, election_data_model.candidates[0])
        deputy_data_check = election_data_check[14:19]
        self.__assert_basic_deputy_infos(deputy_data_check, election_data_model.deputies[0])
        result_data_check = election_data_check[19 : 34]
        self.assert_election_data_first_round_election(result_data_check, election_data_model.election)
        
    def __assert_all_candidates_data(self, candidate_context_check, candidate_model) : 
        self.unit_test.assertEqual(candidate_context_check[0], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context_check[1], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context_check[2], candidate_model.birthdate)
        self.unit_test.assertEqual(candidate_context_check[3], candidate_model.job)
        self.unit_test.assertEqual(candidate_context_check[4], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context_check[5], candidate_model.is_sorting)
        self.unit_test.assertEqual(candidate_context_check[6], candidate_model.party_id)
        self.unit_test.assertEqual(candidate_context_check[7], candidate_model.vote)
        self.unit_test.assertEqual(candidate_context_check[8], candidate_model.rate_vote_registered)
        self.unit_test.assertEqual(candidate_context_check[9], candidate_model.rate_vote_expressed)
        
    
    def assert_candidate_data_model_from_first_round_election(self, candidate_data_check, candidate_data_model) :
        department_data_check = candidate_data_check[0 : 2]
        self.__assert_candidate_department_data_first_round_election(department_data_check, candidate_data_model.department)
        district_data_check = candidate_data_check[2 : 4]
        self.__assert_candidate_district_data_first_round_election(district_data_check, candidate_data_model.district)
        election_data_check = candidate_data_check[4 : 19]
        self.assert_election_data_first_round_election(election_data_check, candidate_data_model.election)
        limit_candidate = 19 + self.candidates_number * 9
        candidates_data_check = candidate_data_check[19 : limit_candidate]
        self.__assert_candidates_data_first_round_election(candidates_data_check, candidate_data_model.candidates)
        
        
    def __assert_candidate_department_data_first_round_election(self, department_data_context_check, department_model) :
        self.unit_test.assertTrue(department_model != None)
        self.unit_test.assertEqual(department_data_context_check[0], department_model.number)
        self.unit_test.assertEqual(department_data_context_check[1], department_model.name)
        
        
    def __assert_candidate_district_data_first_round_election(self, district_data_context_check, district_model) : 
        self.unit_test.assertTrue(district_model != None)
        self.unit_test.assertEqual(district_data_context_check[0], district_model.number)
        self.unit_test.assertEqual(district_data_context_check[1], district_model.name)
        
    
    #TODO find better names
    def __assert_candidates_data_first_round_election(self, candidates_context_check, candidates_model):
        self.unit_test.assertEqual(len(candidates_model), self.candidates_number)
        index = 0
        for candidate_model in candidates_model : 
            #récupérer les bonnes datas
            start_index = index * 9
            candidate_context_check = candidates_context_check[start_index : start_index + 9]
            self.assert_candidate_data_first_round_election(candidate_context_check, candidate_model)
            index += 1
            
            
    #TODO find better names          
    def assert_candidate_data_first_round_election(self, candidate_context_check, candidate_model) :
        self.unit_test.assertEqual(candidate_context_check[1], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context_check[2], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context_check[3], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context_check[5], candidate_model.vote)
        self.unit_test.assertEqual(candidate_context_check[6], candidate_model.rate_vote_registered)
        self.unit_test.assertEqual(candidate_context_check[7], candidate_model.rate_vote_expressed)
        
        
    def assert_election_data_first_round_election(self, election_context_check, election_model) :
        self.unit_test.assertEqual(election_context_check[0], election_model.state_compute)
        self.unit_test.assertEqual(election_context_check[1], election_model.registered)
        self.unit_test.assertEqual(election_context_check[2], election_model.abstaining)
        self.unit_test.assertEqual(election_context_check[3], election_model.rate_abstaining)
        self.unit_test.assertEqual(election_context_check[4], election_model.voting)
        self.unit_test.assertEqual(election_context_check[5], election_model.rate_voting)  
        self.unit_test.assertEqual(election_context_check[6], election_model.blank_balot)    
        self.unit_test.assertEqual(election_context_check[7], election_model.rate_blank_registered)   
        self.unit_test.assertEqual(election_context_check[8], election_model.rate_blank_voting)       
        self.unit_test.assertEqual(election_context_check[9], election_model.null_ballot)  
        self.unit_test.assertEqual(election_context_check[10], election_model.rate_null_registered)  
        self.unit_test.assertEqual(election_context_check[11], election_model.rate_null_voting)  
        self.unit_test.assertEqual(election_context_check[12], election_model.expressed)  
        self.unit_test.assertEqual(election_context_check[13], election_model.rate_express_registered)  
        self.unit_test.assertEqual(election_context_check[14], election_model.rate_express_voting)    
        
        
    def assert_candidate_model_identity(self, candidate_context, candidate_model): 
        self.unit_test.assertEqual(candidate_context[0], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context[1], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context[2], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context[3], candidate_model.party_id)
        self.unit_test.assertEqual(candidate_context[4], candidate_model.job)
        self.unit_test.assertEqual(candidate_context[5], candidate_model.birthdate)
        self.unit_test.assertEqual(candidate_context[6], candidate_model.is_sorting)
        
    
    def  assert_deputy_model(self, deputy_data_check, deputy_model) :
        self.__assert_basic_deputy_infos(deputy_data_check[0 : 5], deputy_model)
        self.unit_test.assertEqual(deputy_data_check[5], deputy_model.candidate.last_name)
        self.unit_test.assertEqual(deputy_data_check[6], deputy_model.candidate.first_name)
        
        
    def __assert_basic_deputy_infos(self, deputy_data_check, deputy_model) : 
        self.unit_test.assertEqual(deputy_data_check[0], deputy_model.last_name)
        self.unit_test.assertEqual(deputy_data_check[1], deputy_model.first_name)
        self.unit_test.assertEqual(deputy_data_check[2], deputy_model.sexe)
        self.unit_test.assertTrue(deputy_data_check[3] == deputy_model.birthdate)
        self.unit_test.assertEqual(deputy_data_check[4], deputy_model.is_sorting)
        