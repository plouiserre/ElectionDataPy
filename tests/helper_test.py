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
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        second_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Non']"
        candidates = [first_candidate, second_candidate]
        return candidates      
        
    
    def get_six_candidates(self) : 
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n  \'1978-06-11 00:00:00\' \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' \'1954-07-13 00:00:00\' \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n  '1982-06-30 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' '1968-10-02 00:00:00' 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo'  '1972-04-14 00:00:00' 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' '1993-08-23 00:00:00' 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence'  '1972-03-06 00:00:00' 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n '1978-12-01 00:00:00' 'Non']"
        fifth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n  '1995-01-30 00:00:00' 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' '1974-03-31 00:00:00' 'Non']"
        sixth_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n  '1983-12-22 00:00:00' 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n '1957-03-26 00:00:00' 'Non']"
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
    
    #TODO check using of this method
    def get_two_candidates_data_model(self) :
        first_department = self.get_department("Aisne",2)
        first_district = self.get_district("4ème circonscription", 4) 
        first_district.department = first_department
        first_candidate = self.get_candidate("Wednesday", datetime.datetime(2002,9,27), False, "Student", "Addams", 3, "F")
        first_deputy = self.get_deputy("Enid", "Sinclair",datetime.datetime(2002, 4, 2), "F", False) 
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = first_department
        first_candidate_data.district = first_district
        first_candidate_data.candidates.append(first_candidate)
        first_candidate_data.deputies.append(first_deputy)
        
        second_department = self.get_department("Nord",59)
        second_district = self.get_district("13ème circonscription", 13)   
        second_district.department = second_department
        second_candidate = self.get_candidate("Thomas", datetime.datetime(1976,5,25), True, "Gangster", "Shelby", 6, "M")
        second_deputy = self.get_deputy("Polly", "Gray", datetime.datetime(1968, 8,17), "F", True) 
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = second_department
        second_candidate_data.district = second_district
        second_candidate_data.candidates.append(second_candidate)
        second_candidate_data.deputies.append(second_deputy)
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates    
    
    def get_two_candidates_model(self) : 
        first_candidate = self.get_candidate("Wednesday", datetime.datetime(2002,9,27), False, "Student", "Addams", 3, "F")
        first_candidate.id = 1
        
        second_candidate = self.get_candidate("Thomas", datetime.datetime(1976,5,25), True, "Gangster", "Shelby", 6, "M")
        second_candidate.id = 2
        
        candidates = [first_candidate, second_candidate]
        
        return candidates
    
    
    def get_two_corsica_candidates_data_model(self) :
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = self.get_department("Corse-du-Sud",20)
        first_candidate_data.district = self.get_district("4ème circonscription", 4)   
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = self.get_department("Haute-Corse",20)
        second_candidate_data.district =  self.get_district("13ème circonscription", 13)   
        second_candidate_data.district.department = second_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates
    
    
    def get_six_candidates_data_model(self) : 
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = self.get_department("Ain",1)
        first_candidate_data.district.name = self.get_district("1ère circonscription", 1)        
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = self.get_department("Aisne",2)
        second_candidate_data.district.name = self.get_district("4ème circonscription", 4)
        
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department = self.get_department("Alpes-de-Haute-Provence",4)
        third_candidate_data.district.name = self.get_district("2ème circonscription", 2)
        
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department = self.get_department("Alpes-Maritimes",6)
        fourth_candidate_data.district = self.get_district("6ème circonscription", 6)
        
        fifth_candidate_data = CandidateDataModel()
        fifth_candidate_data.department = self.get_department("Aube",10)
        fifth_candidate_data.district = self.get_district("1ère circonscription", 1) 
        
        sixth_candidate_data = CandidateDataModel()
        sixth_candidate_data.department =  self.get_department("Nord",59)
        sixth_candidate_data.district = self.get_district("13ème circonscription", 13)
        
        candidates = [first_candidate_data, second_candidate_data, third_candidate_data, fourth_candidate_data, fifth_candidate_data, sixth_candidate_data]
        
        return candidates
    
    
    def get_eight_candidates_data_model(self) : 
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = self.get_department("Ain",1)
        first_candidate_data.district = self.get_district("1ère circonscription", 1)
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = self.get_department("Aisne",2)
        second_candidate_data.district = self.get_district("4ème circonscription", 4)
        second_candidate_data.district.department = second_candidate_data.department
        
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department =  self.get_department("Alpes-de-Haute-Provence",4)
        third_candidate_data.district = self.get_district("2ème circonscription", 2)
        third_candidate_data.district.department = third_candidate_data.department
        
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department =  self.get_department("Alpes-Maritimes",6)
        fourth_candidate_data.district = self.get_district("6ème circonscription", 6)
        fourth_candidate_data.district.department = fourth_candidate_data.department
        
        fifth_candidate_data = CandidateDataModel()
        fifth_candidate_data.department =  self.get_department("Alpes-Maritimes",6)
        fifth_candidate_data.district = self.get_district("6ème circonscription", 6)
        fifth_candidate_data.district.department = fifth_candidate_data.department
        
        sixth_candidate_data = CandidateDataModel()
        sixth_candidate_data.department =  self.get_department("Aube",10)
        sixth_candidate_data.district = self.get_district("1ère circonscription", 1)
        sixth_candidate_data.district.department = sixth_candidate_data.department
        
        seven_candidate_data = CandidateDataModel()
        seven_candidate_data.department = self.get_department("Aube",10)
        seven_candidate_data.district = self.get_district("1ère circonscription", 1)
        seven_candidate_data.district.department = seven_candidate_data.department
        
        eigth_candidate_data = CandidateDataModel()
        eigth_candidate_data.department = self.get_department("Nord",59)
        eigth_candidate_data.district = self.get_district("13ème circonscription", 13)
        eigth_candidate_data.district.department = eigth_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data, third_candidate_data, fourth_candidate_data, fifth_candidate_data, sixth_candidate_data, seven_candidate_data, eigth_candidate_data]
        
        return candidates
    
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