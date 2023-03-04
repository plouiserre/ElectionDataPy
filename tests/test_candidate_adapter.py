import unittest
import datetime
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager
from src.Adapter.CandidateAdapter import CandidateAdapter

from tests.helper_test import HelperTest


#TODO add candidate part    
class CandidateAdapterTest(unittest.TestCase) :
    
    def get_two_candidates_data(*args)  : 
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
        
        self.assertEqual(2, len(candidates))
        self.assertEqual(2,candidates[0].department.number)
        self.assertEqual('Aisne',candidates[0].department.name)
        self.assertEqual(4,candidates[0].district.number)
        self.assertEqual('4ème circonscription',candidates[0].district.name)
        self.assertEqual('M', candidates[0].candidate.sexe)
        self.assertEqual('GALL', candidates[0].candidate.last_name)
        self.assertEqual('Aurélien', candidates[0].candidate.first_name)
        self.assertTrue(datetime.datetime(1982,6,30) == candidates[0].candidate.birth_date)
        self.assertEqual(3, candidates[0].candidate.party_id)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', candidates[0].candidate.job)
        self.assertEqual(59,candidates[1].department.number)
        self.assertEqual('Nord',candidates[1].department.name)
        self.assertEqual(13,candidates[1].district.number)
        self.assertEqual('13ème circonscription',candidates[1].district.name)
        self.assertEqual('M', candidates[1].candidate.sexe)
        self.assertEqual('BÉZINE', candidates[1].candidate.last_name)
        self.assertEqual('Clément', candidates[1].candidate.first_name)
        self.assertTrue(datetime.datetime(1983,12,22) == candidates[1].candidate.birth_date)
        self.assertEqual(1, candidates[1].candidate.party_id)
        self.assertEqual('Professeur, profession scientifique', candidates[1].candidate.job)
        
    
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
        
        self.assertEqual(6, len(candidates))
        self.assertEqual(1,candidates[0].department.number)
        self.assertEqual('Ain',candidates[0].department.name)
        self.assertEqual(1,candidates[0].district.number)
        self.assertEqual('1ère circonscription',candidates[0].district.name)
        self.assertEqual('M', candidates[0].candidate.sexe)
        self.assertEqual('BELLON', candidates[0].candidate.last_name)
        self.assertEqual('Julien', candidates[0].candidate.first_name)
        self.assertTrue(datetime.datetime(1978,6,11) == candidates[0].candidate.birth_date)
        self.assertEqual(15, candidates[0].candidate.party_id)
        self.assertEqual('"Cadre administratif et commercial d\'entreprise"', candidates[0].candidate.job)       
        self.assertEqual(2,candidates[1].department.number)
        self.assertEqual('Aisne',candidates[1].department.name)
        self.assertEqual(4,candidates[1].district.number)
        self.assertEqual('4ème circonscription',candidates[1].district.name)
        self.assertEqual('M', candidates[1].candidate.sexe)
        self.assertEqual('GALL', candidates[1].candidate.last_name)
        self.assertEqual('Aurélien', candidates[1].candidate.first_name)
        self.assertTrue(datetime.datetime(1982,6,30) == candidates[1].candidate.birth_date)
        self.assertEqual(3, candidates[1].candidate.party_id)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', candidates[1].candidate.job)       
        self.assertEqual(4,candidates[2].department.number)
        self.assertEqual('Alpes-de-Haute-Provence',candidates[2].department.name)
        self.assertEqual(2,candidates[2].district.number)
        self.assertEqual('2ème circonscription',candidates[2].district.name)
        self.assertEqual('M', candidates[2].candidate.sexe)
        self.assertEqual('WALTER', candidates[2].candidate.last_name)
        self.assertEqual('Léo', candidates[2].candidate.first_name)
        self.assertTrue(datetime.datetime(1972,4,14) == candidates[2].candidate.birth_date)
        self.assertEqual(3, candidates[2].candidate.party_id)
        self.assertEqual('Professeur des écoles, instituteur et assimilé', candidates[2].candidate.job)       
        self.assertEqual(6,candidates[3].department.number)
        self.assertEqual('Alpes-Maritimes',candidates[3].department.name)
        self.assertEqual(6,candidates[3].district.number)
        self.assertEqual('6ème circonscription',candidates[3].district.name)
        self.assertEqual('F', candidates[3].candidate.sexe)
        self.assertEqual('TRASTOUR-ISNART', candidates[3].candidate.last_name)
        self.assertEqual('Laurence', candidates[3].candidate.first_name)
        self.assertTrue(datetime.datetime(1972,3,6) == candidates[3].candidate.birth_date)
        self.assertEqual(12, candidates[3].candidate.party_id)
        self.assertEqual('Cadre de la fonction publique', candidates[3].candidate.job)       
        self.assertEqual(10,candidates[4].department.number)
        self.assertEqual('Aube',candidates[4].department.name)
        self.assertEqual(1,candidates[4].district.number)
        self.assertEqual('1ère circonscription',candidates[4].district.name)
        self.assertEqual('M', candidates[4].candidate.sexe)
        self.assertEqual('GUITTON', candidates[4].candidate.last_name)
        self.assertEqual('Jordan', candidates[4].candidate.first_name)
        self.assertTrue(datetime.datetime(1995,1,30) == candidates[4].candidate.birth_date)
        self.assertEqual(16, candidates[4].candidate.party_id)
        self.assertEqual('Profession intermédiaire administrative de la fonction publique', candidates[4].candidate.job)       
        self.assertEqual(59,candidates[5].department.number)
        self.assertEqual('Nord',candidates[5].department.name)
        self.assertEqual(13,candidates[5].district.number)
        self.assertEqual('13ème circonscription',candidates[5].district.name)
        self.assertEqual('M', candidates[5].candidate.sexe)
        self.assertEqual('BÉZINE', candidates[5].candidate.last_name)
        self.assertEqual('Clément', candidates[5].candidate.first_name)
        self.assertTrue(datetime.datetime(1983,12,22) == candidates[5].candidate.birth_date)
        self.assertEqual(1, candidates[5].candidate.party_id)
        self.assertEqual('Professeur, profession scientifique', candidates[5].candidate.job)
       
    
    
    if __name__ == "__main__":
        unittest.main()