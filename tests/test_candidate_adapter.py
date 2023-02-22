import unittest
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager
from src.Adapter.CandidateAdapter import CandidateAdapter

from tests.helper_test import HelperTest

class CandidateAdapterTest(unittest.TestCase) :
    
    def get_two_candidates_data(*args)  : 
        helper = HelperTest()        
        candidates = helper.get_two_candidates()
        return candidates
        
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_two_candidates_data)
    def test_get_two_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        pd = Mock()
        adapter = CandidateAdapter(pd, ExcelManager)
        
        candidates = adapter.get_candidates()
        
        self.assertEqual(2, len(candidates))
        self.assertEqual(2,candidates[0].department.number)
        self.assertEqual('Aisne',candidates[0].department.name)
        self.assertEqual(4,candidates[0].district_number)
        self.assertEqual('4ème circonscription',candidates[0].district_name)
        self.assertEqual(59,candidates[1].department.number)
        self.assertEqual('Nord',candidates[1].department.name)
        self.assertEqual(13,candidates[1].district_number)
        self.assertEqual('13ème circonscription',candidates[1].district_name)
        
    
    def get_six_candidates_data(*args)  : 
        helper = HelperTest()        
        candidates = helper.get_six_candidates()
        return candidates    
    
        
    @patch.object(ExcelManager,'import_candidates_datas', side_effect=get_six_candidates_data)
    def test_get_six_candidatedatamodels_from_excel_manager(self, mock_excel_manager) : 
        pd = Mock()
        adapter = CandidateAdapter(pd, ExcelManager)
        
        candidates = adapter.get_candidates()
        
        self.assertEqual(6, len(candidates))
        self.assertEqual(1,candidates[0].department.number)
        self.assertEqual('Ain',candidates[0].department.name)
        self.assertEqual(1,candidates[0].district_number)
        self.assertEqual('1ère circonscription',candidates[0].district_name)
        self.assertEqual(2,candidates[1].department.number)
        self.assertEqual('Aisne',candidates[1].department.name)
        self.assertEqual(4,candidates[1].district_number)
        self.assertEqual('4ème circonscription',candidates[1].district_name)
        self.assertEqual(4,candidates[2].department.number)
        self.assertEqual('Alpes-de-Haute-Provence',candidates[2].department.name)
        self.assertEqual(2,candidates[2].district_number)
        self.assertEqual('2ème circonscription',candidates[2].district_name)
        self.assertEqual(6,candidates[3].department.number)
        self.assertEqual('Alpes-Maritimes',candidates[3].department.name)
        self.assertEqual(6,candidates[3].district_number)
        self.assertEqual('6ème circonscription',candidates[3].district_name)
        self.assertEqual(10,candidates[4].department.number)
        self.assertEqual('Aube',candidates[4].department.name)
        self.assertEqual(1,candidates[4].district_number)
        self.assertEqual('1ère circonscription',candidates[4].district_name)
        self.assertEqual(59,candidates[5].department.number)
        self.assertEqual('Nord',candidates[5].department.name)
        self.assertEqual(13,candidates[5].district_number)
        self.assertEqual('13ème circonscription',candidates[5].district_name)
    
    
    if __name__ == "__main__":
        unittest.main()