import unittest
import datetime
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager
from src.Adapter.CandidateAdapter import CandidateAdapter

from tests.helper_test import HelperTest
from tests.base_unit_test import BaseUnitTest

class CandidateAdapterTest(BaseUnitTest):
    
    def get_two_candidates_data(self, *args)  : 
        helper = HelperTest()        
        candidates = helper.get_two_candidates()
        return candidates
        
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_two_candidates_data)
    def test_get_two_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        adapter = CandidateAdapter(pd, ExcelManager)
        
        candidates = adapter.get_candidates(parties)
        
        first_candidate_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False]     
        second_candidate_data_check = [59, "Nord", 13, "13ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False]     
        
        self.assertEqual(2, len(candidates))
        self.assert_candidate_model(first_candidate_data_check, candidates[0])
        self.assert_candidate_model(second_candidate_data_check, candidates[1])
        
        
    def get_six_candidates_data(*args)  : 
        helper = HelperTest()        
        candidates = helper.get_six_candidates()
        return candidates    
    
        
    #TODO repasser par ce test pour le job du premier candidat
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_six_candidates_data)
    def test_get_six_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        helper = HelperTest()        
        parties = helper.get_parties()
        pd = Mock()
        adapter = CandidateAdapter(pd, ExcelManager)
        
        candidates = adapter.get_candidates(parties)
         
        first_candidate_data_check = [1, "Ain", 1, "1ère circonscription", 1, "Ain", "BELLON", "Julien", "M", 15, '"Cadre administratif et commercial d\'entreprise"',  datetime.datetime(1978,6,11), False]     
        second_candidate_data_check = [2, "Aisne", 4, "4ème circonscription", 2, "Aisne", "GALL", "Aurélien", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1982,6,30), False]     
        third_candidate_data_check = [4, "Alpes-de-Haute-Provence", 2, "2ème circonscription", 4, "Alpes-de-Haute-Provence", "WALTER", "Léo", "M", 3, "Professeur des écoles, instituteur et assimilé",  datetime.datetime(1972,4,14), False]     
        fourth_candidate_data_check = [6, "Alpes-Maritimes", 6, "6ème circonscription", 6, "Alpes-Maritimes", "TRASTOUR-ISNART", "Laurence", "F", 12, "Cadre de la fonction publique",  datetime.datetime(1972,3,6), True]     
        fifth_candidate_data_check = [10, "Aube", 1, "1ère circonscription", 10, "Aube", "GUITTON", "Jordan", "M", 16, "Profession intermédiaire administrative de la fonction publique",  datetime.datetime(1995,1,30), False]     
        sixth_candidate_data_check = [59, "Nord", 13, "13ème circonscription", 59, "Nord", "BÉZINE", "Clément", "M", 1, "Professeur, profession scientifique",  datetime.datetime(1983,12,22), False]     
        
        self.assertEqual(6, len(candidates))
        self.assert_candidate_model(first_candidate_data_check, candidates[0])
        self.assert_candidate_model(second_candidate_data_check, candidates[1])
        self.assert_candidate_model(third_candidate_data_check, candidates[2])
        self.assert_candidate_model(fourth_candidate_data_check, candidates[3])
        self.assert_candidate_model(fifth_candidate_data_check, candidates[4])
        self.assert_candidate_model(sixth_candidate_data_check, candidates[5])
        
        
    if __name__ == "__main__":
        unittest.main()