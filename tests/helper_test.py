import datetime

from src.Models.DepartmentModel import DepartmentModel
from src.Models.DeputyModel import DeputyModel
from src.Models.DistrictModel import DistrictModel
from src.Models.CandidateDataModel import CandidateDataModel
from src.Models.CandidateModel import CandidateModel
from src.Models.PartyModel import PartyModel

class HelperTest : 
    def __init__(self) :
        pass    
    
    def get_two_candidates(self) : 
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        second_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate]
        return candidates      
        
    
    def get_six_candidates(self) : 
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n  \'1978-06-11 00:00:00\' \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' datetime.datetime(1954, 7, 13, 0, 0) \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo'  '1972-04-14 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' datetime.datetime(1993, 8, 23, 0, 0) 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence'  '1972-03-06 00:00:00' 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n datetime.datetime(1978, 12, 1, 0, 0) 'Non']"
        fifth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n  '1995-01-30 00:00:00' 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' datetime.datetime(1974, 3, 31, 0, 0) 'Non']"
        sixth_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        return candidates
    
        
    def get_six_departments(self) : 
        first_department = DepartmentModel()
        first_department.id = 65
        first_department.name = "Ain"
        first_department.number = 1
        second_department = DepartmentModel()
        second_department.id = 66
        second_department.name = "Aisne"
        second_department.number = 2
        third_department = DepartmentModel()
        third_department.id = 67
        third_department.name = "Alpes-de-Haute-Provence"
        third_department.number = 4
        fourth_department = DepartmentModel()
        fourth_department.id = 68
        fourth_department.name = "Alpes-Maritimes"
        fourth_department.number = 6
        fifth_department = DepartmentModel()
        fifth_department.id = 69
        fifth_department.name = "Aube"
        fifth_department.number = 10
        sixth_department = DepartmentModel()
        sixth_department.id = 70
        sixth_department.name = "Nord"
        sixth_department.number = 59
        departments = {} 
        departments.update({first_department.number : first_department}) 
        departments.update({second_department.number : second_department})
        departments.update({third_department.number : third_department}) 
        departments.update({fourth_department.number : fourth_department})
        departments.update({fifth_department.number : fifth_department}) 
        departments.update({sixth_department.number : sixth_department})
        return departments
    
    #TODO check using of this method
    def get_two_candidates_data_model(self) :
        first_department = DepartmentModel()
        first_department.name = "Aisne"
        first_department.number = 2
        first_district = DistrictModel()
        first_district.name = "4ème circonscription"
        first_district.number = 4
        first_district.department = first_department
        first_candidate = CandidateModel()
        first_candidate.first_name = "Wednesday"
        first_candidate.birthdate = datetime.datetime(2002,9,27)
        first_candidate.is_sorting = False
        first_candidate.job = "Student"
        first_candidate.last_name = "Addams"
        first_candidate.party_id = 3
        first_candidate.sexe = "F"
        first_deputy = DeputyModel()
        first_deputy.birthdate = datetime.datetime(2002, 4, 2)
        first_deputy.first_name = "Enid"
        first_deputy.is_sorting = False
        first_deputy.last_name = "Sinclair"
        first_deputy.sexe = "F"
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = first_department
        first_candidate_data.district = first_district
        first_candidate_data.candidate = first_candidate
        first_candidate_data.deputy = first_deputy
        
        second_department = DepartmentModel()
        second_department.name = "Nord"
        second_department.number = 59
        second_district = DistrictModel()
        second_district.name = "13ème circonscription"
        second_district.number = 13
        second_district.department = second_department
        second_candidate = CandidateModel()
        second_candidate.birthdate = datetime.datetime(1976,5,25)
        second_candidate.first_name = "Thomas"
        second_candidate.is_sorting = True
        second_candidate.job = "Gangster"
        second_candidate.last_name = "Shelby"
        second_candidate.party_id = 6
        second_candidate.sexe = "M"
        second_deputy = DeputyModel()
        second_deputy.birthdate = datetime.datetime(1968, 8,17)
        second_deputy.first_name = "Polly"
        second_deputy.is_sorting = True
        second_deputy.last_name = "Gray"
        second_deputy.sexe = "F"
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = second_department
        second_candidate_data.district = second_district
        second_candidate_data.candidate = second_candidate
        second_candidate_data.deputy = second_deputy
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates    
    
    #TODO factorize with get_two_candidates_data_model
    def get_two_candidates_model(self) : 
        first_candidate = CandidateModel()
        first_candidate.first_name = "Wednesday"
        first_candidate.birthdate = datetime.datetime(2002,9,27)
        first_candidate.is_sorting = False
        first_candidate.job = "Student"
        first_candidate.last_name = "Addams"
        first_candidate.party_id = 3
        first_candidate.sexe = "F"
        first_candidate.id = 1
        
        second_candidate = CandidateModel()
        second_candidate.birthdate = datetime.datetime(1976,5,25)
        second_candidate.first_name = "Thomas"
        second_candidate.is_sorting = True
        second_candidate.job = "Gangster"
        second_candidate.last_name = "Shelby"
        second_candidate.party_id = 6
        second_candidate.sexe = "M"
        second_candidate.id = 2
        
        candidates = [first_candidate, second_candidate]
        
        return candidates
    
    
    def get_two_corsica_candidates_data_model(self) :
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = DepartmentModel()
        first_candidate_data.department.name = "Corse-du-Sud"
        first_candidate_data.department.number = 20
        first_candidate_data.district = DistrictModel()
        first_candidate_data.district.name = "4ème circonscription"
        first_candidate_data.district.number = 4
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Haute-Corse"
        second_candidate_data.department.number = 20
        second_candidate_data.district = DistrictModel()
        second_candidate_data.district.name = "13ème circonscription"
        second_candidate_data.district.number = 13
        second_candidate_data.district.department = second_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates
    
    
    def get_six_candidates_data_model(self) : 
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = DepartmentModel()
        first_candidate_data.department.name = "Ain"
        first_candidate_data.department.number = 1
        first_candidate_data.district_name = "1ère circonscription"
        first_candidate_data.district.number = 1
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Aisne"
        second_candidate_data.department.number = 2
        second_candidate_data.district_name = "4ème circonscription"
        second_candidate_data.district.number = 4
        
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department = DepartmentModel()
        third_candidate_data.department.name = "Alpes-de-Haute-Provence"
        third_candidate_data.department.number = 4
        third_candidate_data.district_name = "2ème circonscription"
        third_candidate_data.district.number = 2
        
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department = DepartmentModel()
        fourth_candidate_data.department.name = "Alpes-Maritimes"
        fourth_candidate_data.department.number = 6
        fourth_candidate_data.district_name = "6ème circonscription"
        fourth_candidate_data.district.number = 6
        
        fifth_candidate_data = CandidateDataModel()
        fifth_candidate_data.department = DepartmentModel()
        fifth_candidate_data.department.name = "Aube"
        fifth_candidate_data.department.number = 10
        fifth_candidate_data.district_name = "1ère circonscription"
        fifth_candidate_data.district.number = 1
        
        sixth_candidate_data = CandidateDataModel()
        sixth_candidate_data.department = DepartmentModel()
        sixth_candidate_data.department.name = "Nord"
        sixth_candidate_data.department.number = 59
        sixth_candidate_data.district_name = "13ème circonscription"
        sixth_candidate_data.district.number = 13
        
        candidates = [first_candidate_data, second_candidate_data, third_candidate_data, fourth_candidate_data, fifth_candidate_data, sixth_candidate_data]
        
        return candidates
    
    
    def get_eight_candidates_data_model(self) : 
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = DepartmentModel()
        first_candidate_data.department.name = "Ain"
        first_candidate_data.department.number = 1
        first_candidate_data.district = DistrictModel()
        first_candidate_data.district.name = "1ère circonscription"
        first_candidate_data.district.number = 1
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Aisne"
        second_candidate_data.department.number = 2
        second_candidate_data.district = DistrictModel()
        second_candidate_data.district.name = "4ème circonscription"
        second_candidate_data.district.number = 4
        second_candidate_data.district.department = second_candidate_data.department
        
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department = DepartmentModel()
        third_candidate_data.department.name = "Alpes-de-Haute-Provence"
        third_candidate_data.department.number = 4
        third_candidate_data.district = DistrictModel()
        third_candidate_data.district.name = "2ème circonscription"
        third_candidate_data.district.number = 2
        third_candidate_data.district.department = third_candidate_data.department
        
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department = DepartmentModel()
        fourth_candidate_data.department.name = "Alpes-Maritimes"
        fourth_candidate_data.department.number = 6
        fourth_candidate_data.district = DistrictModel()
        fourth_candidate_data.district.name = "6ème circonscription"
        fourth_candidate_data.district.number = 6
        fourth_candidate_data.district.department = fourth_candidate_data.department
        
        fifth_candidate_data = CandidateDataModel()
        fifth_candidate_data.department = DepartmentModel()
        fifth_candidate_data.department.name = "Alpes-Maritimes"
        fifth_candidate_data.department.number = 6
        fifth_candidate_data.district = DistrictModel()
        fifth_candidate_data.district.name = "6ème circonscription"
        fifth_candidate_data.district.number = 6
        fifth_candidate_data.district.department = fifth_candidate_data.department
        
        sixth_candidate_data = CandidateDataModel()
        sixth_candidate_data.department = DepartmentModel()
        sixth_candidate_data.department.name = "Aube"
        sixth_candidate_data.department.number = 10
        sixth_candidate_data.district = DistrictModel()
        sixth_candidate_data.district.name = "1ère circonscription"
        sixth_candidate_data.district.number = 1
        sixth_candidate_data.district.department = sixth_candidate_data.department
        
        seven_candidate_data = CandidateDataModel()
        seven_candidate_data.department = DepartmentModel()
        seven_candidate_data.department.name = "Aube"
        seven_candidate_data.department.number = 10
        seven_candidate_data.district = DistrictModel()
        seven_candidate_data.district.name = "1ère circonscription"
        seven_candidate_data.district.number = 1
        seven_candidate_data.district.department = seven_candidate_data.department
        
        eigth_candidate_data = CandidateDataModel()
        eigth_candidate_data.department = DepartmentModel()
        eigth_candidate_data.department.name = "Nord"
        eigth_candidate_data.department.number = 59
        eigth_candidate_data.district = DistrictModel()
        eigth_candidate_data.district.name = "13ème circonscription"
        eigth_candidate_data.district.number = 13
        eigth_candidate_data.district.department = eigth_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data, third_candidate_data, fourth_candidate_data, fifth_candidate_data, sixth_candidate_data, seven_candidate_data, eigth_candidate_data]
        
        return candidates
        
    
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