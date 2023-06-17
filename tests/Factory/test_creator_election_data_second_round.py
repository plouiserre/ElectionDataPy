import unittest
import datetime

from src.Factory.CreatorElectionDataSecondRound import CreatorElectionDataSecondRound
from src.Models.CandidateModel import CandidateModel
from src.Models.ElectionDataModel import ElectionDataModel
from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ResultModel import ResultModel

from tests.assert_test import AssertTest
from tests.helper_test import HelperTest


class CreatorElectionDataSecondRoundTest(unittest.TestCase) : 
    def test_creator_result_city_first_line(self) : 
        creator = CreatorElectionDataSecondRound(None, None)
        
        election_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146, 44.65, 94.19, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 43, 13.15, 29.45, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 103, 31.5, 70.55, 'nan', 'nan']
        assert_test = AssertTest(self, 2)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data) 
        
        
    def test_creator_result_city_cantal_district_line(self) : 
        creator = CreatorElectionDataSecondRound(None, None)
        
        election_data = creator.factory_method("['15' 'Cantal' 2 '2ème circonscription' 69 'Ferrières-Saint-Mary' 'Complet' 242 107 '44.21' 135 '55.79' 11 '4.55' '8.15' 2 '0.83' '1.48' 122 '50.41' '90.37' 2 'F' 'GUIBERT' 'Martine' 'ENS' 39 '16.12' '31.97' '1.0' 'M' 'BONY' 'Jean-Yves' 'LR' '83.0' '34.3' '68.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        election_data_check = [15, 'Cantal', 2, '2ème circonscription', 'Complet', 242, 107, 44.21, 135, 55.79, 11, 4.55, 8.15, 2, 0.83, 1.48, 122, 50.41, 90.37, 2, 'F', 'GUIBERT', 'Martine', 'ENS', 39, 16.12, 31.97, 'nan', '1.0', 'M', 'BONY', 'Jean-Yves', 'LR', 83, 34.3, 68.03, 'nan', 'nan']
        assert_test = AssertTest(self, 2)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data) 
        
        
    def test_creator_result_city_with_last_election_data_created_same_district(self) : 
        helper = HelperTest()
        last_election_data_created = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorElectionDataSecondRound(None, last_election_data_created)
        
        election_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 931, 489, 52.54, 442, 47.46, 10, 1.105, 2.335, 11, 1.26, 2.66, 421, 45.09, 95.005, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 151, 15.515, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 270, 29.575, 65.64, 'nan', 'nan']
        assert_test = AssertTest(self, 2)                                                                                                                                                                                                                               
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data)