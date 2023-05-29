import unittest
import datetime
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager
from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Services.PartyServices import PartyServices
from src.Repository.mydb import MyDb
from src.Repository.PartyRepository import PartyRepository

from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

#TODO rework assert part
class CandidateAdapterTest(unittest.TestCase):
    
    def get_two_candidates_data_same_districts(self, *args)  : 
        helper = HelperTest()        
        candidates = helper.get_two_candidates_same_districts()
        return candidates
        
    #TODO try to use two patch object to mock party_service.load_parties
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_two_candidates_data_same_districts)
    def test_get_two_elections_data_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        party_service = PartyServices()
        mydb = MyDb()        
        party_repository = PartyRepository(mydb)
        adapter = CandidateAdapter(pd, ExcelManager, party_service, party_repository)
        
        #TODO delete this line
        adapter.parties = parties        
        elections_data = adapter.extracts_datas_from_files()
        election_data = elections_data[0]
        
        self.assertEqual(1, len(elections_data))
        self.assertEqual('Aisne', election_data.department.name)
        self.assertEqual(2, election_data.department.number)
        self.assertEqual('4ème circonscription', election_data.district.name)
        self.assertEqual(4, election_data.district.number)
        self.assertEqual(2, len(election_data.candidates))
        self.assertEqual(2, len(election_data.deputies))        
        self.assertEqual('GALL', election_data.candidates[0].last_name)
        self.assertEqual('Aurélien', election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1982,6,30) == election_data.candidates[0].birthdate)
        self.assertEqual('M', election_data.candidates[0].sexe)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', election_data.candidates[0].job)
        self.assertEqual(3, election_data.candidates[0].party_id)
        self.assertFalse(election_data.candidates[0].is_sorting)
        self.assertEqual('LEGRAND', election_data.deputies[0].last_name)
        self.assertEqual('Estelle', election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1968,10,2) == election_data.deputies[0].birthdate)
        self.assertEqual('F', election_data.deputies[0].sexe)
        self.assertFalse(election_data.deputies[0].is_sorting)        
        self.assertEqual('BÉZINE', election_data.candidates[1].last_name)
        self.assertEqual('Clément', election_data.candidates[1].first_name)
        self.assertTrue(datetime.datetime(1983,12,22) == election_data.candidates[1].birthdate)
        self.assertEqual('M', election_data.candidates[1].sexe)
        self.assertEqual('Professeur, profession scientifique', election_data.candidates[1].job)
        self.assertEqual(1, election_data.candidates[1].party_id)
        self.assertTrue(election_data.candidates[1].is_sorting)
        self.assertEqual('WARINGHEM', election_data.deputies[1].last_name)
        self.assertEqual('Jean-Luc', election_data.deputies[1].first_name)
        self.assertTrue(datetime.datetime(1957,3,26) == election_data.deputies[1].birthdate)
        self.assertEqual('M', election_data.deputies[1].sexe)
        self.assertTrue(election_data.deputies[1].is_sorting)
         
        # first_election_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False, 'F', 'LEGRAND', 'Estelle', datetime.datetime(1968, 10, 2, 0, 0), False]             
        # second_election_data_check = [2, "Aisne", 4, "4ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False, 'M', 'WARINGHEM', 'Jean-Luc', datetime.datetime(1957, 3, 26, 0, 0), False]     
        
        # assert_test = AssertTest(self, 0)
        # self.assertEqual(2, len(candidates))
        # assert_test.assert_all_candidates_infos_with_deputy(first_election_data_check, candidates[0])
        # assert_test.assert_all_candidates_infos_with_deputy(second_election_data_check, candidates[1])
        
        
    def get_three_candidates_data_same_districts(self, *args)  : 
        helper = HelperTest()        
        candidates = helper.get_three_candidates_same_districts()
        return candidates
        
    #TODO if too many unit test delete this one     
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_three_candidates_data_same_districts)
    def test_get_three_elections_data_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        party_service = PartyServices()
        mydb = MyDb()        
        party_repository = PartyRepository(mydb)
        adapter = CandidateAdapter(pd, ExcelManager, party_service, party_repository)
        
        #TODO delete this line
        adapter.parties = parties        
        elections_data = adapter.extracts_datas_from_files()
        election_data = elections_data[0]
        
        self.assertEqual(1, len(elections_data))
        self.assertEqual('Aisne', election_data.department.name)
        self.assertEqual(2, election_data.department.number)
        self.assertEqual('4ème circonscription', election_data.district.name)
        self.assertEqual(4, election_data.district.number)
        self.assertEqual(3, len(election_data.candidates))
        self.assertEqual(3, len(election_data.deputies))        
        self.assertEqual('GALL', election_data.candidates[0].last_name)
        self.assertEqual('Aurélien', election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1982,6,30) == election_data.candidates[0].birthdate)
        self.assertEqual('M', election_data.candidates[0].sexe)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', election_data.candidates[0].job)
        self.assertEqual(3, election_data.candidates[0].party_id)
        self.assertFalse(election_data.candidates[0].is_sorting)
        self.assertEqual('LEGRAND', election_data.deputies[0].last_name)
        self.assertEqual('Estelle', election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1968,10,2) == election_data.deputies[0].birthdate)
        self.assertEqual('F', election_data.deputies[0].sexe)
        self.assertFalse(election_data.deputies[0].is_sorting)        
        self.assertEqual('BÉZINE', election_data.candidates[1].last_name)
        self.assertEqual('Clément', election_data.candidates[1].first_name)
        self.assertTrue(datetime.datetime(1983,12,22) == election_data.candidates[1].birthdate)
        self.assertEqual('M', election_data.candidates[1].sexe)
        self.assertEqual('Professeur, profession scientifique', election_data.candidates[1].job)
        self.assertEqual(1, election_data.candidates[1].party_id)
        self.assertTrue(election_data.candidates[1].is_sorting)
        self.assertEqual('WARINGHEM', election_data.deputies[1].last_name)
        self.assertEqual('Jean-Luc', election_data.deputies[1].first_name)
        self.assertTrue(datetime.datetime(1957,3,26) == election_data.deputies[1].birthdate)
        self.assertEqual('M', election_data.deputies[1].sexe)
        self.assertTrue(election_data.deputies[1].is_sorting)    
        self.assertEqual('WALTER', election_data.candidates[2].last_name)
        self.assertEqual('Léo', election_data.candidates[2].first_name)
        self.assertTrue(datetime.datetime(1972,4,14) == election_data.candidates[2].birthdate)
        self.assertEqual('M', election_data.candidates[2].sexe)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', election_data.candidates[2].job)
        self.assertEqual(3, election_data.candidates[2].party_id)
        self.assertFalse(election_data.candidates[2].is_sorting)
        self.assertEqual('ALLAMEL', election_data.deputies[2].last_name)
        self.assertEqual('Alice', election_data.deputies[2].first_name)
        self.assertTrue(datetime.datetime(1993,8,23) == election_data.deputies[2].birthdate)
        self.assertEqual('F', election_data.deputies[2].sexe)
        self.assertFalse(election_data.deputies[2].is_sorting)
    
    
    
    def get_two_candidates_data(self, *args)  : 
        helper = HelperTest()        
        candidates = helper.get_two_candidates()
        return candidates
        
    #TODO try to use two patch object to mock party_service.load_parties
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_two_candidates_data)
    def test_get_two_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        party_service = PartyServices()
        mydb = MyDb()        
        party_repository = PartyRepository(mydb)
        adapter = CandidateAdapter(pd, ExcelManager, party_service, party_repository)
        
        #TODO delete this line
        adapter.parties = parties        
        elections_datas = adapter.extracts_datas_from_files()
         
        first_election_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False, 'F', 'LEGRAND', 'Estelle', datetime.datetime(1968, 10, 2, 0, 0), False]             
        second_election_data_check = [59, "Nord", 13, "13ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False, 'M', 'WARINGHEM', 'Jean-Luc', datetime.datetime(1957, 3, 26, 0, 0), False]     
        
        assert_test = AssertTest(self, 0)
        self.assertEqual(2, len(elections_datas))
        assert_test.assert_all_candidates_infos_with_deputy(first_election_data_check, elections_datas[0])
        assert_test.assert_all_candidates_infos_with_deputy(second_election_data_check, elections_datas[1])
        
        
    def get_six_candidates_data(*args)  : 
        helper = HelperTest()        
        candidates = helper.get_six_candidates()
        return candidates    
    
        
    #TODO try to use two patch object to mock party_service.load_parties
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_six_candidates_data)
    def test_get_six_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        party_service = PartyServices()
        mydb = MyDb()        
        party_repository = PartyRepository(mydb)
        adapter = CandidateAdapter(pd, ExcelManager, party_service, party_repository)
        
        #TODO delete this line
        adapter.parties = parties        
        elections_datas_from_districts = adapter.extracts_datas_from_files()
        
        # first_election_data_check = [1, "Ain", 1, "1ère circonscription", 1, "Ain", "BELLON", "Julien", "M", 14, '"Cadre administratif et commercial d\'entreprise"',  datetime.datetime(1978,6,11), False, 'F', 'JEAN-LOUIS', 'Fabienne', datetime.datetime(1954, 7, 13, 0, 0), False]     
        # second_election_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False, 'F', 'LEGRAND', 'Estelle', datetime.datetime(1968, 10, 2, 0, 0), False]     
        # third_election_data_check = [4, "Alpes-de-Haute-Provence", 2, "2ème circonscription", 4, "Alpes-de-Haute-Provence", "WALTER", "Léo", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1972,4,14), False, 'F', 'ALLAMEL', 'Alice', datetime.datetime(1993, 8, 23, 0, 0), False]     
        # fourth_election_data_check = [4, "Alpes-de-Haute-Provence", 2, "2ème circonscription", 6, "Alpes-Maritimes", "TRASTOUR-ISNART", "Laurence", "F", 11, "Cadre de la fonction publique",  datetime.datetime(1972,3,6), True, 'M', 'COANUS', 'Christophe', datetime.datetime(1978, 12, 1, 0, 0), False]     
        # fifth_election_data_check = [10, "Aube", 1, "1ère circonscription", 10, "Aube", "GUITTON", "Jordan", "M", 15, "Profession intermédiaire administrative de la fonction publique",  datetime.datetime(1995,1,30), False, 'F', 'DA ROCHA', 'Katia', datetime.datetime(1974, 3, 31, 0, 0), False]     
        # sixth_election_data_check = [10, "Aube", 1, "1ère circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False, 'M', 'WARINGHEM', 'Jean-Luc', datetime.datetime(1957, 3, 26, 0, 0), False]     
        
        self.assertEqual(4, len(elections_datas_from_districts))
        
        first_election_data = elections_datas_from_districts[0]
        second_election_data = elections_datas_from_districts[1]
        third_election_data = elections_datas_from_districts[2]
        fourth_election_data = elections_datas_from_districts[3]
        
        self.assertEqual('Ain', first_election_data.department.name)
        self.assertEqual(1, first_election_data.department.number)
        self.assertEqual('1ère circonscription', first_election_data.district.name)
        self.assertEqual(1, first_election_data.district.number)
        self.assertEqual(1, len(first_election_data.candidates))
        self.assertEqual(1, len(first_election_data.deputies))        
        self.assertEqual('BELLON', first_election_data.candidates[0].last_name)
        self.assertEqual('Julien', first_election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1978,6,11) == first_election_data.candidates[0].birthdate)
        self.assertEqual('M', first_election_data.candidates[0].sexe)
        self.assertEqual('Cadre administratif et commercial d entreprise', first_election_data.candidates[0].job)
        self.assertEqual(14, first_election_data.candidates[0].party_id)
        self.assertFalse(first_election_data.candidates[0].is_sorting)
        self.assertEqual('JEAN-LOUIS', first_election_data.deputies[0].last_name)
        self.assertEqual('Fabienne', first_election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1954,7,13) == first_election_data.deputies[0].birthdate)
        self.assertEqual('F', first_election_data.deputies[0].sexe)
        self.assertFalse(first_election_data.deputies[0].is_sorting)        
        
        self.assertEqual('Aisne', second_election_data.department.name)
        self.assertEqual(2, second_election_data.department.number)
        self.assertEqual('4ème circonscription', second_election_data.district.name)
        self.assertEqual(4, second_election_data.district.number)
        self.assertEqual(1, len(second_election_data.candidates))
        self.assertEqual(1, len(second_election_data.deputies))        
        self.assertEqual('GALL', second_election_data.candidates[0].last_name)
        self.assertEqual('Aurélien', second_election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1982,6,30) == second_election_data.candidates[0].birthdate)
        self.assertEqual('M', second_election_data.candidates[0].sexe)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', second_election_data.candidates[0].job)
        self.assertEqual(3, second_election_data.candidates[0].party_id)
        self.assertFalse(second_election_data.candidates[0].is_sorting)
        self.assertEqual('LEGRAND', second_election_data.deputies[0].last_name)
        self.assertEqual('Estelle', second_election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1968,10,2) == second_election_data.deputies[0].birthdate)
        self.assertEqual('F', second_election_data.deputies[0].sexe)
        self.assertFalse(second_election_data.deputies[0].is_sorting)    
        
        self.assertEqual('Alpes-de-Haute-Provence', third_election_data.department.name)
        self.assertEqual(4, third_election_data.department.number)
        self.assertEqual('2ème circonscription', third_election_data.district.name)
        self.assertEqual(2, third_election_data.district.number)
        self.assertEqual(2, len(third_election_data.candidates))
        self.assertEqual(2, len(third_election_data.deputies))        
        self.assertEqual('WALTER', third_election_data.candidates[0].last_name)
        self.assertEqual('Léo', third_election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1972,4,14) == third_election_data.candidates[0].birthdate)
        self.assertEqual('M', third_election_data.candidates[0].sexe)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', third_election_data.candidates[0].job)
        self.assertEqual(3, third_election_data.candidates[0].party_id)
        self.assertFalse(third_election_data.candidates[0].is_sorting)
        self.assertEqual('ALLAMEL', third_election_data.deputies[0].last_name)
        self.assertEqual('Alice', third_election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1993, 8, 23) == third_election_data.deputies[0].birthdate)
        self.assertEqual('F', third_election_data.deputies[0].sexe)
        self.assertFalse(third_election_data.deputies[0].is_sorting)             
        self.assertEqual('TRASTOUR-ISNART', third_election_data.candidates[1].last_name)
        self.assertEqual('Laurence', third_election_data.candidates[1].first_name)
        self.assertTrue(datetime.datetime(1972,3,6) == third_election_data.candidates[1].birthdate)
        self.assertEqual('F', third_election_data.candidates[1].sexe)
        self.assertEqual('Cadre de la fonction publique', third_election_data.candidates[1].job)
        self.assertEqual(11, third_election_data.candidates[1].party_id)
        self.assertTrue(third_election_data.candidates[1].is_sorting)
        self.assertEqual('COANUS', third_election_data.deputies[1].last_name)
        self.assertEqual('Christophe', third_election_data.deputies[1].first_name)
        self.assertTrue(datetime.datetime(1978, 12, 1) == third_election_data.deputies[1].birthdate)
        self.assertEqual('M', third_election_data.deputies[1].sexe)
        self.assertFalse(third_election_data.deputies[1].is_sorting)             
        
        self.assertEqual('Aube', fourth_election_data.department.name)
        self.assertEqual(10, fourth_election_data.department.number)
        self.assertEqual('1ère circonscription', fourth_election_data.district.name)
        self.assertEqual(1, fourth_election_data.district.number)
        self.assertEqual(2, len(fourth_election_data.candidates))
        self.assertEqual(2, len(fourth_election_data.deputies))        
        self.assertEqual('GUITTON', fourth_election_data.candidates[0].last_name)
        self.assertEqual('Jordan', fourth_election_data.candidates[0].first_name)
        self.assertTrue(datetime.datetime(1995,1,30) == fourth_election_data.candidates[0].birthdate)
        self.assertEqual('M', fourth_election_data.candidates[0].sexe)
        self.assertEqual('Profession intermédiaire administrative de la fonction publique', fourth_election_data.candidates[0].job)
        self.assertEqual(15, fourth_election_data.candidates[0].party_id)
        self.assertFalse(fourth_election_data.candidates[0].is_sorting)
        self.assertEqual('DA ROCHA', fourth_election_data.deputies[0].last_name)
        self.assertEqual('Katia', fourth_election_data.deputies[0].first_name)
        self.assertTrue(datetime.datetime(1974, 3, 31) == fourth_election_data.deputies[0].birthdate)
        self.assertEqual('F', fourth_election_data.deputies[0].sexe)
        self.assertFalse(fourth_election_data.deputies[0].is_sorting)                     
        self.assertEqual('BÉZINE', fourth_election_data.candidates[1].last_name)
        self.assertEqual('Clément', fourth_election_data.candidates[1].first_name)
        self.assertTrue(datetime.datetime(1983,12,22) == fourth_election_data.candidates[1].birthdate)
        self.assertEqual('M', fourth_election_data.candidates[1].sexe)
        self.assertEqual('Professeur, profession scientifique', fourth_election_data.candidates[1].job)
        self.assertEqual(1, fourth_election_data.candidates[1].party_id)
        self.assertFalse(fourth_election_data.candidates[1].is_sorting)
        self.assertEqual('WARINGHEM', fourth_election_data.deputies[1].last_name)
        self.assertEqual('Jean-Luc', fourth_election_data.deputies[1].first_name)
        self.assertTrue(datetime.datetime(1957, 3, 26) == fourth_election_data.deputies[1].birthdate)
        self.assertEqual('M', fourth_election_data.deputies[1].sexe)
        self.assertFalse(fourth_election_data.deputies[1].is_sorting)       
        
        
        
    if __name__ == "__main__":
        unittest.main()