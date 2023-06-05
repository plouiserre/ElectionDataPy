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
        elections_data_model = adapter.extracts_datas_from_files()
        #election_data = elections_data[0]
        
        elections_data_check= [[2, 'Aisne', 4, '4ème circonscription',  [['GALL', 'Aurélien', 'M', 3, 'Professeur des écoles, instituteur et assimilé', datetime.datetime(1982,6,30), 
                                False ], ['BÉZINE', 'Clément', 'M', 1, 'Professeur, profession scientifique', datetime.datetime(1983,12,22), True]], [['LEGRAND', 'Estelle', 'F',  
                                datetime.datetime(1968,10,2), False ], ['WARINGHEM', 'Jean-Luc', 'M', datetime.datetime(1957,3,26),  True]]]]
        assert_test = AssertTest(self, 2)
        assert_test.assert_elections_model(elections_data_check, elections_data_model)
        
        
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
        elections_data_model = adapter.extracts_datas_from_files()
        
        elections_data_check= [[2, 'Aisne', 4, '4ème circonscription',  [['GALL', 'Aurélien', 'M', 3, 'Professeur des écoles, instituteur et assimilé', datetime.datetime(1982,6,30), 
                                False ], ['BÉZINE', 'Clément', 'M', 1, 'Professeur, profession scientifique', datetime.datetime(1983,12,22), True], 
                                ['WALTER', 'Léo', 'M', 3, 'Professeur des écoles, instituteur et assimilé', datetime.datetime(1972,4,14), False]], 
                                [['LEGRAND', 'Estelle', 'F', datetime.datetime(1968,10,2), False ], ['WARINGHEM', 'Jean-Luc', 'M', datetime.datetime(1957,3,26),  True], 
                                 ['ALLAMEL', 'Alice', 'F', datetime.datetime(1993,8,23),  False]]]]
        assert_test = AssertTest(self, 3)
        assert_test.assert_elections_model(elections_data_check, elections_data_model)
    
    
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
        
        
        self.assertEqual(4, len(elections_datas_from_districts))
        
        #TODO improve
        first_election_data_model = [elections_datas_from_districts[0]]
        second_election_data_model = [elections_datas_from_districts[1]]
        third_election_data_model = [elections_datas_from_districts[2]]
        fourth_election_data_model = [elections_datas_from_districts[3]]
        
        first_election_data_check= [[1, 'Ain', 1, '1ère circonscription',  [['BELLON', 'Julien', 'M', 14, 'Cadre administratif et commercial d entreprise', datetime.datetime(1978,6,11), False]], 
                                [['JEAN-LOUIS', 'Fabienne', 'F', datetime.datetime(1954,7,13), False ]]]]
        
        assert_test = AssertTest(self, 1)
        assert_test.assert_elections_model(first_election_data_check, first_election_data_model)
        
        second_election_data_check= [[2, 'Aisne', 4, '4ème circonscription',  [['GALL', 'Aurélien', 'M', 3, 'Professeur des écoles, instituteur et assimilé', datetime.datetime(1982,6,30), False]], 
                                [['LEGRAND', 'Estelle', 'F', datetime.datetime(1968,10,2), False ]]]]
        
        assert_test = AssertTest(self, 1)
        assert_test.assert_elections_model(second_election_data_check, second_election_data_model)
        
        third_election_data_check= [[4, 'Alpes-de-Haute-Provence', 2, '2ème circonscription',  [['WALTER', 'Léo', 'M', 3, 'Professeur des écoles, instituteur et assimilé', datetime.datetime(1972,4,14), 
                                False ], ['TRASTOUR-ISNART', 'Laurence', 'F', 11, 'Cadre de la fonction publique', datetime.datetime(1972,3,6), True]], 
                                [['ALLAMEL', 'Alice', 'F', datetime.datetime(1993,8,23),  False], ['COANUS', 'Christophe', 'M', datetime.datetime(1978, 12, 1),  False]]]]
        
        assert_test = AssertTest(self, 2)
        assert_test.assert_elections_model(third_election_data_check, third_election_data_model)
        
        fourth_election_data_check= [[10, 'Aube', 1, '1ère circonscription',  [['GUITTON', 'Jordan', 'M', 15, 'Profession intermédiaire administrative de la fonction publique', 
                                datetime.datetime(1995,1,30), False ], ['BÉZINE', 'Clément', 'M', 1, 'Professeur, profession scientifique', datetime.datetime(1983,12,22), False]], 
                                [['DA ROCHA', 'Katia', 'F', datetime.datetime(1974, 3, 31),  False], ['WARINGHEM', 'Jean-Luc', 'M', datetime.datetime(1957,3,26),  False]]]]
        
        assert_test = AssertTest(self, 2)
        assert_test.assert_elections_model(fourth_election_data_check, fourth_election_data_model)
        
        
    if __name__ == "__main__":
        unittest.main()