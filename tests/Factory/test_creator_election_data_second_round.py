import unittest

from src.Factory.CreatorElectionDataSecondRound import CreatorElectionDataSecondRound

from tests.assert_test import AssertTest


class CreatorElectionDataSecondRoundTest(unittest.TestCase) : 
    def test_creator_result_city_second_round_first_line(self) : 
        creator = CreatorElectionDataSecondRound(None)
        
        election_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146, 44.65, 94.19, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 43, 13.15, 29.45, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 103, 31.5, 70.55, 'nan', 'nan']
        assert_test = AssertTest(self, 1)
        assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data) 
        
        
    def test_creator_result_city_second_round_cantal_district_line(self) : 
        creator = CreatorElectionDataSecondRound(None)
        
        election_data = creator.factory_method("['15' 'Cantal' 2 '2ème circonscription' 69 'Ferrières-Saint-Mary' 'Complet' 242 107 '44.21' 135 '55.79' 11 '4.55' '8.15' 2 '0.83' '1.48' 122 '50.41' '90.37' 2 'F' 'GUIBERT' 'Martine' 'ENS' 39 '16.12' '31.97' '1.0' 'M' 'BONY' 'Jean-Yves' 'LR' '83.0' '34.3' '68.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        election_data_check = [15, 'Cantal', 2, '2ème circonscription', 'Complet', 242, 107, 44.21, 135, 55.79, 11, 4.55, 8.15, 2, 0.83, 1.48, 122, 50.41, 90.37, 2, 'F', 'GUIBERT', 'Martine', 'ENS', 39, 16.12, 31.97, 'nan', '1.0', 'M', 'BONY', 'Jean-Yves', 'LR', 83, 34.3, 68.03, 'nan', 'nan']
        assert_test = AssertTest(self, 1)
        assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data) 