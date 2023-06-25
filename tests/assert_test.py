class AssertTest : 

    #SUBDIVISE THIS CLASS
    def __init__(self, unit_test, candidates_number) :
        self.unit_test = unit_test
        self.candidates_number = candidates_number
        
        
    def assert_all_candidates_infos_with_deputy(self, election_data_check, election_data_model) :
        self.unit_test.assertEqual(election_data_check[0], election_data_model.department.number)
        self.unit_test.assertEqual(election_data_check[1], election_data_model.department.name)
        self.unit_test.assertEqual(election_data_check[2], election_data_model.district.number)
        self.unit_test.assertEqual(election_data_check[3], election_data_model.district.name)
        self.unit_test.assertEqual(election_data_check[4], election_data_model.district.department.number)
        self.unit_test.assertEqual(election_data_check[5], election_data_model.district.department.name)
        self.unit_test.assertEqual(election_data_check[6], election_data_model.candidates[0].last_name)
        self.unit_test.assertEqual(election_data_check[7], election_data_model.candidates[0].first_name)
        self.unit_test.assertEqual(election_data_check[8], election_data_model.candidates[0].sexe)
        self.unit_test.assertEqual(election_data_check[9], election_data_model.candidates[0].party_id)
        self.unit_test.assertEqual(election_data_check[10], election_data_model.candidates[0].job)
        self.unit_test.assertTrue(election_data_check[11] == election_data_model.candidates[0].birthdate)
        self.unit_test.assertEqual(election_data_check[12], election_data_model.candidates[0].is_sorting)
        
        self.unit_test.assertEqual(election_data_check[13], election_data_model.deputies[0].sexe)
        self.unit_test.assertEqual(election_data_check[14], election_data_model.deputies[0].last_name)
        self.unit_test.assertEqual(election_data_check[15], election_data_model.deputies[0].first_name)
        self.unit_test.assertTrue(election_data_check[16] == election_data_model.deputies[0].birthdate)
        self.unit_test.assertEqual(election_data_check[17], election_data_model.deputies[0].is_sorting)
        self.unit_test.assertEqual(election_data_check[6], election_data_model.deputies[0].candidate.last_name)
        self.unit_test.assertEqual(election_data_check[7], election_data_model.deputies[0].candidate.first_name)
        
        
    def assert_result_data_model_with_infos_from_list_first_round(self, result_data_check, result_data_model) : 
        department_data_check = result_data_check[0 : 2]
        self.__assert_candidate_department_first_round_result(department_data_check, result_data_model.department)
        district_data_check = result_data_check[2 : 4]
        self.__assert_candidate_district_first_round_result(district_data_check, result_data_model.district)
        election_data_check = result_data_check[4 : 14]
        self.__assert_all_candidates(election_data_check, result_data_model.candidates[0])
        deputy_data_check = result_data_check[14:19]
        self.__assert_basic_deputy_infos(deputy_data_check, result_data_model.deputies[0])
        result_data_check = result_data_check[19 : 35]
        self.assert_result_data_rounds_result(result_data_check, result_data_model.first_result)
        
        
    def __assert_all_candidates(self, candidate_context_check, candidate_model) : 
        self.unit_test.assertEqual(candidate_context_check[0], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context_check[1], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context_check[2], candidate_model.birthdate)
        self.unit_test.assertEqual(candidate_context_check[3], candidate_model.job)
        self.unit_test.assertEqual(candidate_context_check[4], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context_check[5], candidate_model.is_sorting)
        self.unit_test.assertEqual(candidate_context_check[6], candidate_model.party_id)
        self.unit_test.assertEqual(candidate_context_check[7], candidate_model.vote_first_round)
        self.unit_test.assertEqual(candidate_context_check[8], candidate_model.rate_vote_registered_first_round)
        self.unit_test.assertEqual(candidate_context_check[9], candidate_model.rate_vote_expressed_first_round)
        
        
    def assert_result_data_model_with_all_infos(self, result_data_check, result_data_model) : 
        department_data_check = result_data_check[0 : 2]
        self.__assert_candidate_department_first_round_result(department_data_check, result_data_model.department)
        district_data_check = result_data_check[2 : 4]
        self.__assert_candidate_district_first_round_result(district_data_check, result_data_model.district)
        election_data_check = result_data_check[4 : 17]
        self.__assert_all_candidates_all_infos(election_data_check, result_data_model.candidates[0])
        deputy_data_check = result_data_check[17:22]
        self.__assert_basic_deputy_infos(deputy_data_check, result_data_model.deputies[0])
        first_result_data_check = result_data_check[22 : 38]
        self.assert_result_data_rounds_result(first_result_data_check, result_data_model.first_result)
        second_result_data_check = result_data_check[38 : 54]
        self.assert_result_data_rounds_result(second_result_data_check, result_data_model.second_result)
        
        
    def __assert_all_candidates_all_infos(self, candidate_context_check, candidate_model) : 
        candidate_context_check_without_second_round = candidate_context_check[0 : 10]
        self.__assert_all_candidates(candidate_context_check_without_second_round, candidate_model)
        self.unit_test.assertEqual(candidate_context_check[10], candidate_model.vote_second_round)
        self.unit_test.assertEqual(candidate_context_check[11], candidate_model.rate_vote_registered_second_round)
        self.unit_test.assertEqual(candidate_context_check[12], candidate_model.rate_vote_expressed_second_round)
        
        
    def assert_election_data_model_first_round_result(self, election_data_check, election_data_model) :
        candidates_data_check = self.__assert_election_data_model_from_rounds_result_with_candidates_data_check(election_data_check, election_data_model)
        self.__assert_candidates_from_first_round_result(candidates_data_check, election_data_model.candidates)
    
    
    def assert_election_data_model_second_round_result(self, election_data_check, election_data_model) :
        candidates_data_check = self.__assert_election_data_model_from_rounds_result_with_candidates_data_check(election_data_check, election_data_model)
        self.__assert_candidates_from_second_round_result(candidates_data_check, election_data_model.candidates)
          
        
    def __assert_election_data_model_from_rounds_result_with_candidates_data_check(self, election_data_check, election_data_model) :
        department_data_check = election_data_check[0 : 2]
        self.__assert_candidate_department_first_round_result(department_data_check, election_data_model.department)
        district_data_check = election_data_check[2 : 4]
        self.__assert_candidate_district_first_round_result(district_data_check, election_data_model.district)
        result_data_check = election_data_check[4 : 20]
        if election_data_model.first_result != None and election_data_model.first_result.state_compute != '':
            self.assert_result_data_rounds_result(result_data_check, election_data_model.first_result)
        else : 
            self.assert_result_data_rounds_result(result_data_check, election_data_model.second_result)            
        limit_candidate = 19 + self.candidates_number * 9
        candidates_data_check = election_data_check[20 : limit_candidate]
        return candidates_data_check
        
        
    def __assert_candidate_department_first_round_result(self, department_data_context_check, department_model) :
        self.unit_test.assertTrue(department_model != None)
        self.unit_test.assertEqual(department_data_context_check[0], department_model.number)
        self.unit_test.assertEqual(department_data_context_check[1], department_model.name)
        
        
    def __assert_candidate_district_first_round_result(self, district_data_context_check, district_model) : 
        self.unit_test.assertTrue(district_model != None)
        self.unit_test.assertEqual(district_data_context_check[0], district_model.number)
        self.unit_test.assertEqual(district_data_context_check[1], district_model.name)
        
    def __assert_candidates_from_first_round_result(self, candidates_context_check, candidates_model):
        self.unit_test.assertEqual(len(candidates_model), self.candidates_number)
        index = 0
        for candidate_model in candidates_model : 
            start_index = index * 9
            candidate_context_check = candidates_context_check[start_index : start_index + 9]
            self.assert_election_data_first_round_result(candidate_context_check, candidate_model)
            index += 1
            
            
    def assert_election_data_first_round_result(self, candidate_context_check, candidate_model) :
        self.unit_test.assertEqual(candidate_context_check[1], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context_check[2], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context_check[3], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context_check[5], candidate_model.vote_first_round)
        self.unit_test.assertEqual(candidate_context_check[6], candidate_model.rate_vote_registered_first_round)
        self.unit_test.assertEqual(candidate_context_check[7], candidate_model.rate_vote_expressed_first_round)
        
        
    def __assert_candidates_from_second_round_result(self, candidates_context_check, candidates_model):
        self.unit_test.assertEqual(len(candidates_model), self.candidates_number)
        index = 0
        for candidate_model in candidates_model : 
            start_index = index * 9
            candidate_context_check = candidates_context_check[start_index : start_index + 9]
            self.assert_election_data_second_round_result(candidate_context_check, candidate_model)
            index += 1
            
            
    def assert_election_data_second_round_result(self, candidate_context_check, candidate_model) :
        self.unit_test.assertEqual(candidate_context_check[1], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context_check[2], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context_check[3], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context_check[5], candidate_model.vote_second_round)
        self.unit_test.assertEqual(candidate_context_check[6], candidate_model.rate_vote_registered_second_round)
        self.unit_test.assertEqual(candidate_context_check[7], candidate_model.rate_vote_expressed_second_round)
        
        
    def assert_result_data_rounds_result(self, result_context_check, result_model) :
        self.unit_test.assertEqual(result_context_check[0], result_model.state_compute)
        self.unit_test.assertEqual(result_context_check[1], result_model.round_number)
        self.unit_test.assertEqual(result_context_check[2], result_model.registered)
        self.unit_test.assertEqual(result_context_check[3], result_model.abstaining)
        self.unit_test.assertEqual(result_context_check[4], result_model.rate_abstaining)
        self.unit_test.assertEqual(result_context_check[5], result_model.voting)
        self.unit_test.assertEqual(result_context_check[6], result_model.rate_voting)  
        self.unit_test.assertEqual(result_context_check[7], result_model.blank_balot)    
        self.unit_test.assertEqual(result_context_check[8], result_model.rate_blank_registered)   
        self.unit_test.assertEqual(result_context_check[9], result_model.rate_blank_voting)       
        self.unit_test.assertEqual(result_context_check[10], result_model.null_ballot)  
        self.unit_test.assertEqual(result_context_check[11], result_model.rate_null_registered)  
        self.unit_test.assertEqual(result_context_check[12], result_model.rate_null_voting)  
        self.unit_test.assertEqual(result_context_check[13], result_model.expressed)  
        self.unit_test.assertEqual(result_context_check[14], result_model.rate_express_registered)  
        self.unit_test.assertEqual(result_context_check[15], result_model.rate_express_voting)     
        
        
    def assert_candidate_model_basic(self, candidate_context, candidate_model): 
        self.unit_test.assertEqual(candidate_context[0], candidate_model.last_name)
        self.unit_test.assertEqual(candidate_context[1], candidate_model.first_name)
        self.unit_test.assertEqual(candidate_context[2], candidate_model.sexe)
        self.unit_test.assertEqual(candidate_context[3], candidate_model.party_id)
        self.unit_test.assertEqual(candidate_context[4], candidate_model.job)
        self.unit_test.assertEqual(candidate_context[5], candidate_model.birthdate)
        self.unit_test.assertEqual(candidate_context[6], candidate_model.is_sorting)
        
    
    def assert_deputy_model(self, deputy_data_check, deputy_model) :
        self.__assert_basic_deputy_infos(deputy_data_check[0 : 5], deputy_model)
        self.unit_test.assertEqual(deputy_data_check[5], deputy_model.candidate.last_name)
        self.unit_test.assertEqual(deputy_data_check[6], deputy_model.candidate.first_name)
        
        
    def __assert_basic_deputy_infos(self, deputy_data_check, deputy_model) : 
        self.unit_test.assertEqual(deputy_data_check[0], deputy_model.last_name)
        self.unit_test.assertEqual(deputy_data_check[1], deputy_model.first_name)
        self.unit_test.assertEqual(deputy_data_check[2], deputy_model.sexe)
        self.unit_test.assertTrue(deputy_data_check[3] == deputy_model.birthdate)
        self.unit_test.assertEqual(deputy_data_check[4], deputy_model.is_sorting)
        
        
    def assert_elections_model(self, elections_data_check, elections_data_model) :
        for index in range(len(elections_data_check)) :
            election_data_check = elections_data_check[index]
            department_data_check = election_data_check[0 : 2]
            self.__assert_candidate_department_first_round_result(department_data_check, elections_data_model[index].department)
            district_data_check = election_data_check[2 : 4]
            self.__assert_candidate_district_first_round_result(district_data_check, elections_data_model[index].district)
            candidates_deputies_number = self.candidates_number
            j = 0
            while j < candidates_deputies_number :
                candidate_data_check = election_data_check[4][j]
                self.assert_candidate_model_basic(candidate_data_check, elections_data_model[index].candidates[j])
                deputy_data_check = election_data_check[5][j]
                self.__assert_basic_deputy_infos(deputy_data_check, elections_data_model[index].deputies[j])
                j += 1    
                
                
    def assert_last_election_data_created(self, last_election_data_created, election_data_model) : 
        self.unit_test.assertEqual(last_election_data_created.department.name, election_data_model.department.name)
        self.unit_test.assertEqual(last_election_data_created.department.number, election_data_model.department.number)
        self.unit_test.assertEqual(last_election_data_created.district.name, election_data_model.district.name)
        self.unit_test.assertEqual(last_election_data_created.district.number, election_data_model.district.number)
        self.unit_test.assertEqual(len(last_election_data_created.candidates), len(election_data_model.candidates))
        
        for index in range(len(election_data_model.candidates)) : 
            self.unit_test.assertEqual(last_election_data_created.candidates[index].last_name, election_data_model.candidates[index].last_name)
            self.unit_test.assertEqual(last_election_data_created.candidates[index].first_name, election_data_model.candidates[index].first_name)
            self.unit_test.assertTrue(last_election_data_created.candidates[index].birthdate == election_data_model.candidates[index].birthdate)
            self.unit_test.assertEqual(last_election_data_created.candidates[index].party_id, election_data_model.candidates[index].party_id)
            self.unit_test.assertEqual(last_election_data_created.candidates[index].job, election_data_model.candidates[index].job)
            self.unit_test.assertEqual(last_election_data_created.candidates[index].sexe, election_data_model.candidates[index].sexe)
        
        for index in range(len(election_data_model.deputies)) : 
            self.unit_test.assertEqual(last_election_data_created.deputies[index].last_name, election_data_model.deputies[index].last_name)
            self.unit_test.assertEqual(last_election_data_created.deputies[index].first_name, election_data_model.deputies[index].first_name)
            self.unit_test.assertTrue(last_election_data_created.deputies[index].birthdate == election_data_model.deputies[index].birthdate)
            self.unit_test.assertEqual(last_election_data_created.deputies[index].sexe, election_data_model.deputies[index].sexe)