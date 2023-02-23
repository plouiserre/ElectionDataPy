from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.CandidateDataModel import CandidateDataModel


class HelperTest : 
    def __init__(self) :
        pass
    
    def get_two_candidates(self) : 
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        second_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate]
        return candidates
        
    def get_six_candidates(self) : 
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n datetime.datetime(1978, 6, 11, 0, 0) \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' datetime.datetime(1954, 7, 13, 0, 0) \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo' datetime.datetime(1972, 4, 14, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' datetime.datetime(1993, 8, 23, 0, 0) 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence' datetime.datetime(1972, 3, 6, 0, 0) 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n datetime.datetime(1978, 12, 1, 0, 0) 'Non']"
        fifth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n datetime.datetime(1995, 1, 30, 0, 0) 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' datetime.datetime(1974, 3, 31, 0, 0) 'Non']"
        sixth_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        return candidates
        
    def get_eigth_candidates(self) : 
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n datetime.datetime(1978, 6, 11, 0, 0) \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' datetime.datetime(1954, 7, 13, 0, 0) \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo' datetime.datetime(1972, 4, 14, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' datetime.datetime(1993, 8, 23, 0, 0) 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence' datetime.datetime(1972, 3, 6, 0, 0) 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n datetime.datetime(1978, 12, 1, 0, 0) 'Non']"
        fifth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 4 21 'F' 'MAZZELLA'\n 'Nicole' datetime.datetime(1952, 9, 11, 0, 0) 'NUP' 'Ancien cadre' 'Non'\n 'M' 'BOUHACHI' 'Laury' datetime.datetime(1978, 10, 28, 0, 0) 'Non']"
        sixth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n datetime.datetime(1995, 1, 30, 0, 0) 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' datetime.datetime(1974, 3, 31, 0, 0) 'Non']"
        seventh_candidate = "['10' 'Aube' '01' '1ère circonscription' 7 20 'M' 'SPAGNESI' 'Laurent'\n datetime.datetime(1956, 10, 12, 0, 0) 'NUP' 'Ancien cadre' 'Non' 'F'\n 'CORDEUIL' 'Annick' datetime.datetime(1955, 2, 5, 0, 0) 'Non']"
        eight_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate,seventh_candidate, eight_candidate]
        return candidates
        
    def get_two_corsica_candidates(self) : 
        first_candidate = "['2A' 'Corse-du-Sud' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        second_candidate = "['2B' 'Haute-Corse' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate]
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
    
    
    def get_one_candidate_data_model(self) : 
        candidate_data = CandidateDataModel()
        candidate_data.department_name = "Gironde"
        candidate_data.department_number = 33
        candidate_data.district_name = "1 ère circonscription"
        candidate_data.district.number = 1
        candidate_data.candidate_first_name = "Thomas"
        candidate_data.candidate_last_name = "Cazenave"
        candidate_data.candidate_is_sorting = False
        candidate_data.candidate_job = "Cadre de la fonction publique"
        candidate_data.candidate_party = "ENS"
        candidate_data.candidate_sexe = "M"
        candidate_data.candidate_birth_date = "06/03/1978"
        return candidate_data
    
    
    def get_two_candidates_data_model(self) :
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = DepartmentModel()
        first_candidate_data.department.name = "Aisne"
        first_candidate_data.department.number = 2
        #first_candidate_data.department.id = 66
        first_candidate_data.district = DistrictModel()
        first_candidate_data.district.name = "4ème circonscription"
        first_candidate_data.district.number = 4
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Nord"
        second_candidate_data.department.number = 59
        #second_candidate_data.department.id = 67
        second_candidate_data.district = DistrictModel()
        second_candidate_data.district.name = "13ème circonscription"
        second_candidate_data.district.number = 13
        second_candidate_data.district.department = second_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data]
        
        return candidates    
    
    
    def get_two_corsica_candidates_data_model(self) :
        first_candidate_data = CandidateDataModel()
        first_candidate_data.department = DepartmentModel()
        first_candidate_data.department.name = "Corse-du-Sud"
        first_candidate_data.department.number = 20
        #first_candidate_data.department.id = 65
        first_candidate_data.district = DistrictModel()
        first_candidate_data.district.name = "4ème circonscription"
        first_candidate_data.district.number = 4
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Haute-Corse"
        second_candidate_data.department.number = 20
        #second_candidate_data.department.id = 65
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
        #first_candidate_data.department.id = 65
        first_candidate_data.district = DistrictModel()
        first_candidate_data.district.name = "1ère circonscription"
        first_candidate_data.district.number = 1
        first_candidate_data.district.department = first_candidate_data.department
        
        second_candidate_data = CandidateDataModel()
        second_candidate_data.department = DepartmentModel()
        second_candidate_data.department.name = "Aisne"
        second_candidate_data.department.number = 2
        #second_candidate_data.department.id = 66
        second_candidate_data.district = DistrictModel()
        second_candidate_data.district.name = "4ème circonscription"
        second_candidate_data.district.number = 4
        second_candidate_data.district.department = second_candidate_data.department
        
        third_candidate_data = CandidateDataModel()
        third_candidate_data.department = DepartmentModel()
        third_candidate_data.department.name = "Alpes-de-Haute-Provence"
        third_candidate_data.department.number = 4
        #third_candidate_data.department.id = 67
        third_candidate_data.district = DistrictModel()
        third_candidate_data.district.name = "2ème circonscription"
        third_candidate_data.district.number = 2
        third_candidate_data.district.department = third_candidate_data.department
        
        fourth_candidate_data = CandidateDataModel()
        fourth_candidate_data.department = DepartmentModel()
        fourth_candidate_data.department.name = "Alpes-Maritimes"
        fourth_candidate_data.department.number = 6
        #fourth_candidate_data.department.id = 68
        fourth_candidate_data.district = DistrictModel()
        fourth_candidate_data.district.name = "6ème circonscription"
        fourth_candidate_data.district.number = 6
        fourth_candidate_data.district.department = fourth_candidate_data.department
        
        fifth_candidate_data = CandidateDataModel()
        fifth_candidate_data.department = DepartmentModel()
        fifth_candidate_data.department.name = "Alpes-Maritimes"
        fifth_candidate_data.department.number = 6
        #fifth_candidate_data.department.id = 68
        fifth_candidate_data.district = DistrictModel()
        fifth_candidate_data.district.name = "6ème circonscription"
        fifth_candidate_data.district.number = 6
        fifth_candidate_data.district.department = fifth_candidate_data.department
        
        sixth_candidate_data = CandidateDataModel()
        sixth_candidate_data.department = DepartmentModel()
        sixth_candidate_data.department.name = "Aube"
        sixth_candidate_data.department.number = 10
        #sixth_candidate_data.department.id = 69
        sixth_candidate_data.district = DistrictModel()
        sixth_candidate_data.district.name = "1ère circonscription"
        sixth_candidate_data.district.number = 1
        sixth_candidate_data.district.department = sixth_candidate_data.department
        
        seven_candidate_data = CandidateDataModel()
        seven_candidate_data.department = DepartmentModel()
        seven_candidate_data.department.name = "Aube"
        seven_candidate_data.department.number = 10
        #seven_candidate_data.department.id = 69
        seven_candidate_data.district = DistrictModel()
        seven_candidate_data.district.name = "1ère circonscription"
        seven_candidate_data.district.number = 1
        seven_candidate_data.district.department = seven_candidate_data.department
        
        eigth_candidate_data = CandidateDataModel()
        eigth_candidate_data.department = DepartmentModel()
        eigth_candidate_data.department.name = "Nord"
        eigth_candidate_data.department.number = 59
        #eigth_candidate_data.department.id = 70
        eigth_candidate_data.district = DistrictModel()
        eigth_candidate_data.district.name = "13ème circonscription"
        eigth_candidate_data.district.number = 13
        eigth_candidate_data.district.department = eigth_candidate_data.department
        
        candidates = [first_candidate_data, second_candidate_data, third_candidate_data, fourth_candidate_data, fifth_candidate_data, sixth_candidate_data, seven_candidate_data, eigth_candidate_data]
        
        return candidates