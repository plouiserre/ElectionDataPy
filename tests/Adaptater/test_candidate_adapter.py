import unittest
import datetime
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager
from src.Adapter.CandidateAdapter import CandidateAdapter
from src.Services.PartyServices import PartyServices
from src.Repository.mydb import MyDb
from src.Repository.PartyRepository import PartyRepository

from tests.helper_test import HelperTest
from tests.base_unit_test import BaseUnitTest

class CandidateAdapterTest(BaseUnitTest):
    
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
        candidates = adapter.extracts_datas_from_files()
         
        first_candidate_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False, 'F', 'LEGRAND', 'Estelle', datetime.datetime(1968, 10, 2, 0, 0), False]             
        second_candidate_data_check = [59, "Nord", 13, "13ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False, 'M', 'WARINGHEM', 'Jean-Luc', datetime.datetime(1957, 3, 26, 0, 0), False]     
        
        self.assertEqual(2, len(candidates))
        self.assert_candidate_model(first_candidate_data_check, candidates[0])
        self.assert_candidate_model(second_candidate_data_check, candidates[1])
        
        
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
        candidates = adapter.extracts_datas_from_files()
        
        first_candidate_data_check = [1, "Ain", 1, "1ère circonscription", 1, "Ain", "BELLON", "Julien", "M", 14, '"Cadre administratif et commercial d\'entreprise"',  datetime.datetime(1978,6,11), False, 'F', 'JEAN-LOUIS', 'Fabienne', datetime.datetime(1954, 7, 13, 0, 0), False]     
        second_candidate_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False, 'F', 'LEGRAND', 'Estelle', datetime.datetime(1968, 10, 2, 0, 0), False]     
        third_candidate_data_check = [4, "Alpes-de-Haute-Provence", 2, "2ème circonscription", 4, "Alpes-de-Haute-Provence", "WALTER", "Léo", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1972,4,14), False, 'F', 'ALLAMEL', 'Alice', datetime.datetime(1993, 8, 23, 0, 0), False]     
        fourth_candidate_data_check = [6, "Alpes-Maritimes", 6, "6ème circonscription", 6, "Alpes-Maritimes", "TRASTOUR-ISNART", "Laurence", "F", 11, "Cadre de la fonction publique",  datetime.datetime(1972,3,6), True, 'M', 'COANUS', 'Christophe', datetime.datetime(1978, 12, 1, 0, 0), False]     
        fifth_candidate_data_check = [10, "Aube", 1, "1ère circonscription", 10, "Aube", "GUITTON", "Jordan", "M", 15, "Profession intermédiaire administrative de la fonction publique",  datetime.datetime(1995,1,30), False, 'F', 'DA ROCHA', 'Katia', datetime.datetime(1974, 3, 31, 0, 0), False]     
        sixth_candidate_data_check = [59, "Nord", 13, "13ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False, 'M', 'WARINGHEM', 'Jean-Luc', datetime.datetime(1957, 3, 26, 0, 0), False]     
        
        self.assertEqual(6, len(candidates))
        self.assert_candidate_model(first_candidate_data_check, candidates[0])
        self.assert_candidate_model(second_candidate_data_check, candidates[1])
        self.assert_candidate_model(third_candidate_data_check, candidates[2])
        self.assert_candidate_model(fourth_candidate_data_check, candidates[3])
        self.assert_candidate_model(fifth_candidate_data_check, candidates[4])
        self.assert_candidate_model(sixth_candidate_data_check, candidates[5])
        
        
    if __name__ == "__main__":
        unittest.main()