import datetime

from src.Models.DepartmentModel import DepartmentModel
from src.Models.DeputyModel import DeputyModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionDataModel import ElectionDataModel
from src.Models.CandidateModel import CandidateModel
from src.Models.PartyModel import PartyModel
from src.Models.ResultModel import ResultModel

class HelperTest : 
    def __init__(self) :
        pass    
    
    def get_two_candidates(self) : 
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        second_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Non']"
        candidates = [first_candidate, second_candidate]
        return candidates     
    
    
    def get_two_candidates_same_districts(self) : 
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Oui' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Oui']"
        candidates = [first_candidate, second_candidate]
        return candidates      
    
    
    def get_three_candidates_same_districts(self) : 
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Oui' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Oui']"
        third_candidate = "['02' 'Aisne' '04' '4ème circonscription' 12 18 'M'\n 'WALTER' 'Léo'  '1972-04-14 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' '1993-08-23 00:00:00' 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate]
        return candidates     
    
    
    def get_six_candidates(self) : 
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n  \'1978-06-11 00:00:00\' \'REC\'\n \'Cadre administratif et commercial d entreprise\' \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' \'1954-07-13 00:00:00\' \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo'  '1972-04-14 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' '1993-08-23 00:00:00' 'Non']"
        fourth_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence'  '1972-03-06 00:00:00' 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n '1978-12-01 00:00:00' 'Non']"
        fifth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n  '1995-01-30 00:00:00' 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' '1974-03-31 00:00:00' 'Non']"
        sixth_candidate = "['10' 'Aube' '01' '1ère circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        return candidates
    
        
    def get_six_departments(self) : 
        first_department = self.get_department("Ain",1)
        first_department.id = 65
        second_department = self.get_department("Aisne",2)
        second_department.id = 66
        third_department = self.get_department("Alpes-de-Haute-Provence",4)
        third_department.id = 67
        fourth_department = self.get_department("Alpes-Maritimes",6)
        fourth_department.id = 68
        fifth_department =self.get_department("Aube",10)
        fifth_department.id = 69
        sixth_department = self.get_department("Nord",59)
        sixth_department.id = 70
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        departments.update({third_department.number : third_department}) 
        departments.update({fourth_department.number : fourth_department})
        departments.update({fifth_department.number : fifth_department}) 
        departments.update({sixth_department.number : sixth_department})
        return departments
    
    
    def get_two_elections_data_model(self) :
        first_department = self.get_department("Aisne",2)
        first_district = self.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_election = self.get_candidate("Wednesday", datetime.datetime(2002,9,27), False, "Student", "Addams", 3, "F")
        first_deputy = self.get_deputy("Enid", "Sinclair",datetime.datetime(2002, 4, 2), "F", False) 
        first_election_data = ElectionDataModel()
        first_election_data.department = first_department
        first_election_data.district = first_district
        first_election_data.candidates.append(first_election)
        first_election_data.deputies.append(first_deputy)
        
        second_department = self.get_department("Nord",59)
        second_district = self.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_election = self.get_candidate("Thomas", datetime.datetime(1976,5,25), True, "Gangster", "Shelby", 6, "M")
        second_deputy = self.get_deputy("Polly", "Gray", datetime.datetime(1968, 8,17), "F", True) 
        second_election_data = ElectionDataModel()
        second_election_data.department = second_department
        second_election_data.district = second_district
        second_election_data.candidates.append(second_election)
        second_election_data.deputies.append(second_deputy)
        
        elections = [first_election_data, second_election_data]
        
        return elections    
    
    def get_two_candidates_model(self) : 
        first_candidate = self.get_candidate("Wednesday", datetime.datetime(2002,9,27), False, "Student", "Addams", 3, "F")
        first_candidate.id = 1
        
        second_candidate = self.get_candidate("Thomas", datetime.datetime(1976,5,25), True, "Gangster", "Shelby", 6, "M")
        second_candidate.id = 2
        
        candidates = [first_candidate, second_candidate]
        
        return candidates
    
    
    def get_two_corsica_elections_data_model(self) :
        first_election_data = ElectionDataModel()
        first_election_data.department = self.get_department("Corse-du-Sud",20)
        first_election_data.district = self.get_district("4ème circonscription", 4)   
        first_election_data.district.department = first_election_data.department
        
        second_election_data = ElectionDataModel()
        second_election_data.department = self.get_department("Haute-Corse",20)
        second_election_data.district =  self.get_district("13ème circonscription", 13)   
        second_election_data.district.department = second_election_data.department
        
        candidates = [first_election_data, second_election_data]
        
        return candidates
    
    
    def get_six_elections_data_model(self) : 
        first_election_data = ElectionDataModel()
        first_election_data.department = self.get_department("Ain",1)
        first_election_data.district.name = self.get_district("1ère circonscription", 1)        
        
        second_election_data = ElectionDataModel()
        second_election_data.department = self.get_department("Aisne",2)
        second_election_data.district.name = self.get_district("4ème circonscription", 4)
        
        third_election_data = ElectionDataModel()
        third_election_data.department = self.get_department("Alpes-de-Haute-Provence",4)
        third_election_data.district.name = self.get_district("2ème circonscription", 2)
        
        fourth_election_data = ElectionDataModel()
        fourth_election_data.department = self.get_department("Alpes-Maritimes",6)
        fourth_election_data.district = self.get_district("6ème circonscription", 6)
        
        fifth_election_data = ElectionDataModel()
        fifth_election_data.department = self.get_department("Aube",10)
        fifth_election_data.district = self.get_district("1ère circonscription", 1) 
        
        sixth_election_data = ElectionDataModel()
        sixth_election_data.department =  self.get_department("Nord",59)
        sixth_election_data.district = self.get_district("13ème circonscription", 13)
        
        candidates = [first_election_data, second_election_data, third_election_data, fourth_election_data, fifth_election_data, sixth_election_data]
        
        return candidates
    
    
    def get_eight_candidates_data_model(self) : 
        first_election_data = ElectionDataModel()
        first_election_data.department = self.get_department("Ain",1)
        first_election_data.district = self.get_district("1ère circonscription", 1)
        first_election_data.district.department = first_election_data.department
        
        second_election_data = ElectionDataModel()
        second_election_data.department = self.get_department("Aisne",2)
        second_election_data.district = self.get_district("4ème circonscription", 4)
        second_election_data.district.department = second_election_data.department
        
        third_election_data = ElectionDataModel()
        third_election_data.department =  self.get_department("Alpes-de-Haute-Provence",4)
        third_election_data.district = self.get_district("2ème circonscription", 2)
        third_election_data.district.department = third_election_data.department
        
        fourth_election_data = ElectionDataModel()
        fourth_election_data.department =  self.get_department("Alpes-Maritimes",6)
        fourth_election_data.district = self.get_district("6ème circonscription", 6)
        fourth_election_data.district.department = fourth_election_data.department
        
        fifth_election_data = ElectionDataModel()
        fifth_election_data.department =  self.get_department("Alpes-Maritimes",6)
        fifth_election_data.district = self.get_district("6ème circonscription", 6)
        fifth_election_data.district.department = fifth_election_data.department
        
        sixth_election_data = ElectionDataModel()
        sixth_election_data.department =  self.get_department("Aube",10)
        sixth_election_data.district = self.get_district("1ère circonscription", 1)
        sixth_election_data.district.department = sixth_election_data.department
        
        seven_election_data = ElectionDataModel()
        seven_election_data.department = self.get_department("Aube",10)
        seven_election_data.district = self.get_district("1ère circonscription", 1)
        seven_election_data.district.department = seven_election_data.department
        
        eigth_election_data = ElectionDataModel()
        eigth_election_data.department = self.get_department("Nord",59)
        eigth_election_data.district = self.get_district("13ème circonscription", 13)
        eigth_election_data.district.department = eigth_election_data.department
        
        elections = [first_election_data, second_election_data, third_election_data, fourth_election_data, fifth_election_data, sixth_election_data, seven_election_data, eigth_election_data]
        
        return elections
    
    
    def get_department(self, department_name, department_number) : 
        dept = DepartmentModel()
        dept.name = department_name
        dept.number = department_number
        return dept
    
    
    def get_district(self, district_name, district_number) : 
        dist = DistrictModel()
        dist.name = district_name
        dist.number = district_number
        return dist
    
    
    def get_candidate(self, first_name, birthdate, is_sorting, job, last_name, party_id, sexe):
        candidate = CandidateModel()
        candidate.first_name = first_name
        candidate.birthdate = birthdate
        candidate.is_sorting = is_sorting
        candidate.job = job
        candidate.last_name = last_name
        candidate.party_id = party_id
        candidate.sexe = sexe
        return candidate
    
    
    def get_deputy(self, first_name, last_name, birthdate, sexe, is_sorting):
        deputy = DeputyModel()
        deputy.birthdate = birthdate
        deputy.first_name = first_name
        deputy.is_sorting = is_sorting
        deputy.last_name = last_name
        deputy.sexe = sexe
        return deputy
        
    
    def get_parties(self) : 
        first_party = PartyModel(1, "Divers extrême gauche", "DXG")
        second_party = PartyModel(2, "Parti radical de gauche", "RDG")
        third_party = PartyModel(3, "Nouvelle union populaire écologique et sociale", "NUP")
        fourth_party = PartyModel(4, "Divers gauche", "DVG")
        fifth_party = PartyModel(5, "Ecologistes", "ECO")
        sixth_party = PartyModel(6, "Regionaliste", "REG")
        seventh_party = PartyModel(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        eighth_party = PartyModel(8, "Divers Centre", "DVC")
        nineth_party = PartyModel(9, "Divers", "DIV")
        tenth_party = PartyModel(10, "Union des Démocrates et des Indépendants", "UDI")
        eleventh_party = PartyModel(11, "Les Républicains", "LR")
        twelfth_party = PartyModel(12, "Divers droite", "DVD")
        thirteenth_party = PartyModel(13, "Droite souverainiste", "DSV")
        fourteenth_party = PartyModel(14, "Reconquête !", "REC")
        fifteenth_party = PartyModel(15, "Rassemblement National", "RN")
        sixteenth_party = PartyModel(16, "Divers extrême droite", "DXD")
        parties = [first_party, second_party, third_party, fourth_party, fifth_party, sixth_party, seventh_party,
                   eighth_party, nineth_party, tenth_party, eleventh_party, twelfth_party, thirteenth_party,
                   fourteenth_party, fifteenth_party, sixteenth_party]
        return parties
    
    
    def get_first_department_first_district_last_election_data_model(self) : 
        last_elections = []
        last_election = self.__get_first_last_election_datas()
        last_elections.append(last_election)
        return last_elections
    
    
    def get_two_cities_data_first_department_first_district_last_election_data_model(self) :
        first_last_election = self.__get_first_last_election_datas()
       
        second_last_election = ElectionDataModel()
        second_last_election.department = DepartmentModel()
        second_last_election.department.name = "Ain"
        second_last_election.department.number = 1
        second_last_election.district = DistrictModel()
        second_last_election.district.number = 1
        second_last_election.district.name = "1ère circonscription"
        second_last_election.second_result = self.get_result("Complet", 2, 604, 317, 52.48, 287, 47.52, 6, 0.99, 2.09, 6, 
                       0.99, 2.09, 275, 45.53, 95.82) 
        third_candidate = CandidateModel()
        third_candidate.last_name = 'GUÉRAUD'
        third_candidate.first_name = 'Sébastien'
        third_candidate.sexe = 'M'
        third_candidate.party_id = 3
        third_candidate.vote_second_round = 108
        third_candidate.rate_vote_registered_second_round = 17.88
        third_candidate.rate_vote_expressed_second_round = 39.27
        fourth_candidate = CandidateModel()
        fourth_candidate.last_name = 'BRETON'
        fourth_candidate.first_name = 'Xavier'
        fourth_candidate.sexe = 'M'
        fourth_candidate.party_id = 11
        fourth_candidate.vote_second_round = 167
        fourth_candidate.rate_vote_registered_second_round = 27.65
        fourth_candidate.rate_vote_expressed_second_round = 60.73
        second_last_election.candidates = [third_candidate, fourth_candidate]
        
        last_election_datas = [first_last_election, second_last_election]
        return last_election_datas
    
    
    def __get_first_last_election_datas(self) :
        last_election = ElectionDataModel()
        last_election.department = DepartmentModel()
        last_election.department.name = "Ain"
        last_election.department.number = 1
        last_election.district = DistrictModel()
        last_election.district.number = 1
        last_election.district.name = "1ère circonscription"
        last_election.second_result = self.get_result("Complet", 2, 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 
                       1.53, 3.23, 146, 44.65, 94.19) 
        first_candidate = CandidateModel()
        first_candidate.last_name = 'GUÉRAUD'
        first_candidate.first_name = 'Sébastien'
        first_candidate.sexe = 'M'
        first_candidate.party_id = 3
        first_candidate.vote_second_round = 43
        first_candidate.rate_vote_registered_second_round = 13.15
        first_candidate.rate_vote_expressed_second_round = 29.45
        second_candidate = CandidateModel()
        second_candidate.last_name = 'BRETON'
        second_candidate.first_name = 'Xavier'
        second_candidate.sexe = 'M'
        second_candidate.party_id = 11
        second_candidate.vote_second_round = 103
        second_candidate.rate_vote_registered_second_round = 31.5
        second_candidate.rate_vote_expressed_second_round = 70.55
        candidates = [first_candidate, second_candidate]
        last_election.candidates = candidates
        return last_election
        

    def get_result(self, state_compute, round_number, registered, abstaining, rate_abstaining, voting, rate_voting, blank_balot, rate_blank_registered, rate_blank_voting, null_ballot, 
                       rate_null_registered, rate_null_voting, expressed, rate_express_registered, rate_express_voting) : 
        result = ResultModel()
        result.state_compute = state_compute
        result.round_number = round_number
        result.registered = registered
        result.abstaining = abstaining
        result.rate_abstaining = rate_abstaining
        result.voting = voting
        result.rate_voting = rate_voting
        result.blank_balot = blank_balot
        result.rate_blank_registered = rate_blank_registered
        result.rate_blank_voting = rate_blank_voting
        result.null_ballot = null_ballot
        result.rate_null_registered = rate_null_registered
        result.rate_null_voting = rate_null_voting
        result.expressed = expressed
        result.rate_express_registered = rate_express_registered
        result.rate_express_voting = rate_express_voting
        return result
    
    
    def get_election_data_from_first_round_adapter_two_candidates(self) :        
        first_department = self.get_department("Aisne",2)
        first_district = self.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_candidate = self.get_candidate("Wednesday", None, None, None, "Addams", 0, "F")
        first_candidate.vote_first_round = 5463213
        first_candidate.rate_vote_registered_first_round = 12.65
        first_candidate.rate_vote_expressed_first_round = 9.24
        first_election_data = ElectionDataModel()
        first_election_data.department = first_department
        first_election_data.district = first_district
        first_election_data.candidates.append(first_candidate)
        first_election_data.first_result = self.get_result("Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042)        
        second_department = self.get_department("Nord",59)
        second_district = self.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_candidate = self.get_candidate("Thomas",  None, None, None, "Shelby", 0, "M")
        second_candidate.vote_first_round = 614651432
        second_candidate.rate_vote_registered_first_round = 37.95
        second_candidate.rate_vote_expressed_first_round = 35.57  
        second_election_data = ElectionDataModel()
        second_election_data.department = second_department
        second_election_data.district = second_district
        second_election_data.candidates.append(second_candidate)
        second_election_data.first_result = self.get_result("Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032)
        
        candidates = [first_election_data, second_election_data]
        
        return candidates
    
    
    def get_election_data_from_second_round_adapter_two_candidates(self) :
        first_department = self.get_department("Aisne",2)
        first_district = self.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_candidate = self.get_candidate("Wednesday", None, None, None, "Addams", 0, "F")
        first_candidate.vote_second_round = 21463213
        first_candidate.rate_vote_registered_second_round = 36.65
        first_candidate.rate_vote_expressed_second_round = 19.24
        first_election_data = ElectionDataModel()
        first_election_data.department = first_department
        first_election_data.district = first_district
        first_election_data.candidates.append(first_candidate)
        first_election_data.second_result = self.get_result("Completed", 2, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042)        
        
        second_department = self.get_department("Nord",59)
        second_district = self.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_candidate = self.get_candidate("Thomas",  None, None, None, "Shelby", 0, "M")
        second_candidate.vote_second_round = 9014651432
        second_candidate.rate_vote_registered_second_round = 63.05
        second_candidate.rate_vote_expressed_second_round = 38.57  
        second_election_data = ElectionDataModel()
        second_election_data.department = second_department
        second_election_data.district = second_district
        second_election_data.candidates.append(second_candidate)
        second_election_data.second_result = self.get_result("Completed", 2, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01,  9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032)
        
        candidates = [first_election_data, second_election_data]
        
        return candidates
    
    
    def get_election_data_from_candidate_adapter_four_candidates(self) : 
        candidates = self.get_two_elections_data_model()
        
        third_election_data = ElectionDataModel()
        third_department = self.get_department("Gironde", 33)
        third_district = self.get_district("6ème circonscription", 6)
        third_candidate = self.get_candidate("Penny", datetime.datetime(1985,11,30), True, "Sales", "Hofstadter", 5, "F")
        third_deputy = self.get_deputy("Sheldon", "Cooper", datetime.datetime(1974,3,24),"M",False)
        third_election_data.candidates.append(third_candidate)
        third_election_data.department = third_department
        third_election_data.deputies.append(third_deputy)
        third_election_data.district = third_district
        
        fourth_election_data = ElectionDataModel()
        fourth_department = self.get_department("Hautes Seine", 92)
        fourth_district = self.get_district("8ème circonscription", 8)
        fourth_candidate = self.get_candidate("Robin", datetime.datetime(1982,4,3), False, "Journaliste", "Scherbatsky", 4, "F")
        fourth_deputy = self.get_deputy("Lily", "Aldrin", datetime.datetime(1974,3,24),"F",False)
        fourth_election_data.candidates.append(fourth_candidate)
        fourth_election_data.department = fourth_department
        fourth_election_data.deputies.append(fourth_deputy)
        fourth_election_data.district = fourth_district
        
        candidates.append(third_election_data)
        candidates.append(fourth_election_data)
        
        return candidates
    
    
    def get_election_data_from_first_round_adapter_four_candidates(self) : 
        candidates = self.get_election_data_from_first_round_adapter_two_candidates()
        
        third_department = self.get_department("Gironde", 33)
        third_district = self.get_district("6ème circonscription", 6)
        third_district.department = third_department
        third_candidate = self.get_candidate("Penny", None, None, None, "Hofstadter", 0, "F")
        third_candidate.vote_first_round = 46513465
        third_candidate.rate_vote_registered_first_round = 65.65
        third_candidate.rate_vote_expressed_first_round = 5624
        third_election_data = ElectionDataModel()
        third_election_data.department = third_department
        third_election_data.district = third_district
        third_election_data.candidates.append(third_candidate)
        third_election_data.first_result = self.get_result("Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052)
        
        fourth_department = self.get_department("Hautes Seine", 92)
        fourth_district = self.get_district("8ème circonscription", 8) 
        fourth_district.department = fourth_department
        fourth_candidate = self.get_candidate("Robin",  None, None, None, "Scherbatsky", 0, "F")
        fourth_candidate.vote_first_round = 96513465
        fourth_candidate.rate_vote_registered_first_round = 91.05
        fourth_candidate.rate_vote_expressed_first_round = 46.512
        fourth_election_data = ElectionDataModel()
        fourth_election_data.department = fourth_department
        fourth_election_data.district = fourth_district
        fourth_election_data.candidates.append(fourth_candidate)
        fourth_election_data.first_result = self.get_result("Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01,  19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032)
        
        candidates.append(third_election_data)
        candidates.append(fourth_election_data)
        
        return candidates
    
    
    def get_election_data_from_second_round_adapter_four_candidates(self) : 
        elections_data = self.get_election_data_from_second_round_adapter_two_candidates()
        
        third_department = self.get_department("Gironde", 33)
        third_district = self.get_district("6ème circonscription", 6)
        third_district.department = third_department
        third_candidate = self.get_candidate("Penny", None, None, None, "Hofstadter", 0, "F")
        third_candidate.vote_second_round = 46513465
        third_candidate.rate_vote_registered_second_round = 65.65
        third_candidate.rate_vote_expressed_second_round = 5624
        third_election_data = ElectionDataModel()
        third_election_data.department = third_department
        third_election_data.district = third_district
        third_election_data.candidates.append(third_candidate)
        third_election_data.first_result = self.get_result("Completed", 1, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052)
        third_election_data.second_result = self.get_result("Completed", 2, 15132134, 46123, 30.5, 2561234, 75.5, 666, 20.1, 8.15, 113, 0.71, 0.85, 8456, 0.245, 0.052)
        
        fourth_department = self.get_department("Hautes Seine", 92)
        fourth_district = self.get_district("8ème circonscription", 8) 
        fourth_district.department = fourth_department
        fourth_candidate = self.get_candidate("Robin",  None, None, None, "Scherbatsky", 0, "F")
        fourth_candidate.vote_second_round = 96513465
        fourth_candidate.rate_vote_registered_second_round = 91.05
        fourth_candidate.rate_vote_expressed_second_round = 46.512
        fourth_election_data = ElectionDataModel()
        fourth_election_data.department = fourth_department
        fourth_election_data.district = fourth_district
        fourth_election_data.candidates.append(fourth_candidate)
        fourth_election_data.first_result = self.get_result("Completed", 1, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01,  19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032)
        fourth_election_data.second_result = self.get_result("Completed", 2, 4635123, 45646, 19.5, 646543, 66.4, 234, 5.01,  19.15, 93, 1.91, 0.55, 5456, 0.235, 0.032)
        
        elections_data.append(third_election_data)
        elections_data.append(fourth_election_data)
        
        return elections_data