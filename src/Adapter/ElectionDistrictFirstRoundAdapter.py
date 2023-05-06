from src.Adapter.Adapter import Adapter

#TODO Delete import below
from src.Models.ElectionDistrictFirstRoundModel import ElectionDistrictFirstRoundModel
from src.Models.ElectionModel import ElectionModel
from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.CandidateModel import CandidateModel

class ElectionDistrictFirstRoundAdapter(Adapter) : 
    def __init__(self, panda_lib, excel_manager):
        self.excel_manager = excel_manager     
        self.panda_lib = panda_lib
        
    
    def get_datas_needed(self): 
        print("hello sweety")
    
    
    def extracts_datas_from_files(self) : 
        self.excel_manager.import_first_round_results_datas(self.panda_lib) 
        first_line_data_election_district_first_round_model = ElectionDistrictFirstRoundModel()
        first_line_department = DepartmentModel()
        first_line_department.number = 1
        first_line_department.name = 'Ain'
        first_line_data_election_district_first_round_model.department = first_line_department
        first_line_district = DistrictModel()
        first_line_district.number = 1
        first_line_district.name = '1ère circonscription'
        first_line_data_election_district_first_round_model.district = first_line_district
        first_line_election = ElectionModel()
        first_line_election.state_compute = 'Complet'
        first_line_election.registered = 86187
        first_line_election.abstaining = 43652
        first_line_election.rate_abstaining = 50.65
        first_line_election.voting = 42535
        first_line_election.rate_voting = 49.35
        first_line_election.blank_balot = 490
        first_line_election.rate_blank_registered = 0.57
        first_line_election.rate_blank_voting = 1.15
        first_line_election.null_ballot = 234
        first_line_election.rate_null_registered = 0.27
        first_line_election.rate_null_voting = 0.55
        first_line_election.expressed = 41811
        first_line_election.rate_express_registered = 48.51
        first_line_election.rate_express_voting = 98.3
        first_line_data_election_district_first_round_model.election = first_line_election
        first_line_first_candidate = self.__get_candidate('M', 'LAHY', 'Éric', 391, 0.45, 0.94)
        first_line_second_candidate = self.__get_candidate('M', 'GUÉRAUD', 'Sébastien', 9982, 11.58, 23.87)
        first_line_third_candidate = self.__get_candidate('F', 'ARMENJON', 'Eliane', 1161, 1.35, 2.78)        
        first_line_fourth_candidate = self.__get_candidate('M', 'GUILLERMIN', 'Vincent', 8071, 9.36, 19.3)    
        first_line_fifth_candidate = self.__get_candidate('M', 'BRETON', 'Xavier', 10599, 12.3, 25.35)   
        first_line_sixth_candidate = self.__get_candidate('M', 'MENDES', 'Michael', 641, 0.74, 1.53)
        first_line_seventh_candidate = self.__get_candidate('M', 'BELLON', 'Julien', 1995, 2.31, 4.77)
        first_line_eigth_candidate = self.__get_candidate('F', 'PIROUX GIANNOTTI', 'Brigitte', 8971, 10.41, 21.46)                
        first_line_data_election_district_first_round_model.candidates = [first_line_first_candidate, first_line_second_candidate, first_line_third_candidate, first_line_fourth_candidate, first_line_fifth_candidate, first_line_sixth_candidate,first_line_seventh_candidate,first_line_eigth_candidate]
        second_line_data_election_district_first_round_model = ElectionDistrictFirstRoundModel()
        second_line_department = DepartmentModel()
        second_line_department.number = 25
        second_line_department.name = 'Doubs'
        second_line_data_election_district_first_round_model.department = second_line_department
        second_line_district = DistrictModel()
        second_line_district.number = 2
        second_line_district.name = '2ème circonscription'
        second_line_data_election_district_first_round_model.district = second_line_district
        second_line_election = ElectionModel()
        second_line_election.state_compute = 'Complet'
        second_line_election.registered = 79162
        second_line_election.abstaining = 37688
        second_line_election.rate_abstaining = 47.61
        second_line_election.voting = 41474
        second_line_election.rate_voting = 52.39
        second_line_election.blank_balot = 821
        second_line_election.rate_blank_registered = 1.04
        second_line_election.rate_blank_voting = 1.98
        second_line_election.null_ballot = 326
        second_line_election.rate_null_registered = 0.41
        second_line_election.rate_null_voting = 0.79
        second_line_election.expressed = 40327
        second_line_election.rate_express_registered = 50.94
        second_line_election.rate_express_voting = 97.23
        second_line_data_election_district_first_round_model.election = second_line_election
        second_line_first_candidate = self.__get_candidate('F', 'VUITTON', 'Brigitte', 779, 0.98, 1.93)
        second_line_second_candidate = self.__get_candidate('M', 'RAVACLEY', 'Stéphane', 13112, 16.56, 32.51)
        second_line_third_candidate = self.__get_candidate('M', 'THOMASSIN', 'Geoffrey', 216, 0.27, 0.54)        
        second_line_fourth_candidate = self.__get_candidate('F', 'MEYER', 'Claudine', 0, 0.0, 0.0)    
        second_line_fifth_candidate = self.__get_candidate('M', 'ALAUZET', 'Eric', 12647, 15.98, 31.36)   
        second_line_sixth_candidate = self.__get_candidate('F', 'KAOULAL', 'Chafia', 4354, 5.5, 10.8)
        second_line_seventh_candidate = self.__get_candidate('M', 'PRENEL', 'Jim', 692, 0.87, 1.72)
        second_line_eigth_candidate = self.__get_candidate('F', 'CARRAU', 'Barbara', 1472, 1.86, 3.65)
        second_line_nineth_candidate = self.__get_candidate('M', 'FUSIS', 'Eric', 7055, 8.91, 17.49)                
        second_line_data_election_district_first_round_model.candidates = [second_line_first_candidate, second_line_second_candidate, second_line_third_candidate, second_line_fourth_candidate, second_line_fifth_candidate, second_line_sixth_candidate,second_line_seventh_candidate,second_line_eigth_candidate, second_line_nineth_candidate]
        datas = [first_line_data_election_district_first_round_model, second_line_data_election_district_first_round_model]
        return datas
        
        
    def __get_candidate(self, sexe, last_name, first_name, vote, rate_vote_registered, rate_vote_expressed):
        candidate = CandidateModel()
        candidate.sexe = sexe
        candidate.last_name = last_name
        candidate.first_name = first_name
        candidate.vote = vote
        candidate.rate_vote_registered = rate_vote_registered
        candidate.rate_vote_expressed = rate_vote_expressed
        return candidate