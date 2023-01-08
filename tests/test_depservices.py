import unittest
from unittest.mock import patch

from src.Services.DepartmentServices import DepartmentServices

from src.Repository.DepartmentRepository import DepartmentRepository

#mutualise some code (declaration)

class DepartmentServicesTest(unittest.TestCase):
    
    def test_construct_departments_two_candidates(self) :
        first_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        second_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate]
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        departments = dep.manage_departments(candidates, dep_repo)
        
        self.assertEqual(2, len(departments))
        self.assertEqual(2, departments[0].number)
        self.assertEqual("Aisne", departments[0].name)
        self.assertEqual(59, departments[1].number)
        self.assertEqual("Nord", departments[1].name)
        
        
    def test_construct_departments_many_candidates(self) :
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n datetime.datetime(1978, 6, 11, 0, 0) \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' datetime.datetime(1954, 7, 13, 0, 0) \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo' datetime.datetime(1972, 4, 14, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' datetime.datetime(1993, 8, 23, 0, 0) 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence' datetime.datetime(1972, 3, 6, 0, 0) 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n datetime.datetime(1978, 12, 1, 0, 0) 'Non']"
        fifth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n datetime.datetime(1995, 1, 30, 0, 0) 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' datetime.datetime(1974, 3, 31, 0, 0) 'Non']"
        sixth_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        departments = dep.manage_departments(candidates, dep_repo)
        
        self.assertEqual(6, len(candidates))
        self.assertEqual(1, departments[0].number)
        self.assertEqual("Ain", departments[0].name)
        self.assertEqual(2, departments[1].number)
        self.assertEqual("Aisne", departments[1].name)
        self.assertEqual(4, departments[2].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[2].name)
        self.assertEqual(6, departments[3].number)
        self.assertEqual("Alpes-Maritimes", departments[3].name)
        self.assertEqual(10, departments[4].number)
        self.assertEqual("Aube", departments[4].name)
        self.assertEqual(59, departments[5].number)
        self.assertEqual("Nord", departments[5].name)
        
    def test_construct_departments_neighbourg_candidates(self) :
        first_candidate = '[\'01\' \'Ain\' \'01\' \'1ère circonscription\' 6 22 \'M\' \'BELLON\' \'Julien\'\n datetime.datetime(1978, 6, 11, 0, 0) \'REC\'\n "Cadre administratif et commercial d\'entreprise" \'Non\' \'F\' \'JEAN-LOUIS\'\n \'Fabienne\' datetime.datetime(1954, 7, 13, 0, 0) \'Non\']'
        second_candidate = "['02' 'Aisne' '04' '4ème circonscription' 2 13 'M' 'GALL' 'Aurélien'\n datetime.datetime(1982, 6, 30, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'LEGRAND'\n 'Estelle' datetime.datetime(1968, 10, 2, 0, 0) 'Non']"
        third_candidate = "['04' 'Alpes-de-Haute-Provence' '02' '2ème circonscription' 12 18 'M'\n 'WALTER' 'Léo' datetime.datetime(1972, 4, 14, 0, 0) 'NUP'\n 'Professeur des écoles, instituteur et assimilé' 'Non' 'F' 'ALLAMEL'\n 'Alice' datetime.datetime(1993, 8, 23, 0, 0) 'Non']"
        fourth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 2 79 'F'\n 'TRASTOUR-ISNART' 'Laurence' datetime.datetime(1972, 3, 6, 0, 0) 'LR'\n 'Cadre de la fonction publique' 'Oui' 'M' 'COANUS' 'Christophe'\n datetime.datetime(1978, 12, 1, 0, 0) 'Non']"
        fifth_candidate = "['06' 'Alpes-Maritimes' '06' '6ème circonscription' 4 21 'F' 'MAZZELLA'\n 'Nicole' datetime.datetime(1952, 9, 11, 0, 0) 'NUP' 'Ancien cadre' 'Non'\n 'M' 'BOUHACHI' 'Laury' datetime.datetime(1978, 10, 28, 0, 0) 'Non']"
        sixth_candidate = "['10' 'Aube' '01' '1ère circonscription' 3 5 'M' 'GUITTON' 'Jordan'\n datetime.datetime(1995, 1, 30, 0, 0) 'RN'\n 'Profession intermédiaire administrative de la fonction publique' 'Non'\n 'F' 'DA ROCHA' 'Katia' datetime.datetime(1974, 3, 31, 0, 0) 'Non']"
        seventh_candidate = "['10' 'Aube' '01' '1ère circonscription' 7 20 'M' 'SPAGNESI' 'Laurent'\n datetime.datetime(1956, 10, 12, 0, 0) 'NUP' 'Ancien cadre' 'Non' 'F'\n 'CORDEUIL' 'Annick' datetime.datetime(1955, 2, 5, 0, 0) 'Non']"
        eight_candidate = "['59' 'Nord' '13' '13ème circonscription' 2 43 'M' 'BÉZINE' 'Clément'\n datetime.datetime(1983, 12, 22, 0, 0) 'DXG'\n 'Professeur, profession scientifique' 'Non' 'M' 'WARINGHEM' 'Jean-Luc'\n datetime.datetime(1957, 3, 26, 0, 0) 'Non']"
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate,seventh_candidate, eight_candidate]
        
        dep_repo = DepartmentRepository()
        dep = DepartmentServices()
        departments = dep.manage_departments(candidates, dep_repo)
        
        self.assertEqual(6, len(departments ))
        self.assertEqual(1, departments[0].number)
        self.assertEqual("Ain", departments[0].name)
        self.assertEqual(2, departments[1].number)
        self.assertEqual("Aisne", departments[1].name)
        self.assertEqual(4, departments[2].number)
        self.assertEqual("Alpes-de-Haute-Provence", departments[2].name)
        self.assertEqual(6, departments[3].number)
        self.assertEqual("Alpes-Maritimes", departments[3].name)
        self.assertEqual(10, departments[4].number)
        self.assertEqual("Aube", departments[4].name)
        self.assertEqual(59, departments[5].number)
        self.assertEqual("Nord", departments[5].name)
        
        
    @patch.object(DepartmentRepository,'save_departments')
    def test_deparments_repository_save_departments_called(self, mock_departmentrepository) : 
        dep_repo = DepartmentRepository()
        department_services = DepartmentServices()
        
        department_services.manage_departments([], dep_repo)
        
        self.assertTrue(mock_departmentrepository.called)