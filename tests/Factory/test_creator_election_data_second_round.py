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
        creator = CreatorElectionDataSecondRound(None, [])
        
        election_data_model = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146, 44.65, 94.19, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 43, 13.15, 29.45, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 103, 31.5, 70.55, 'nan', 'nan']
        assert_test = AssertTest(self, 2)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data_model) 
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created) 
        
        
    def test_creator_result_city_cantal_district_line(self) : 
        creator = CreatorElectionDataSecondRound(None, [])
        
        election_data_model = creator.factory_method("['15' 'Cantal' 2 '2ème circonscription' 69 'Ferrières-Saint-Mary' 'Complet' 242 107 '44.21' 135 '55.79' 11 '4.55' '8.15' 2 '0.83' '1.48' 122 '50.41' '90.37' 2 'F' 'GUIBERT' 'Martine' 'ENS' 39 '16.12' '31.97' '1.0' 'M' 'BONY' 'Jean-Yves' 'LR' '83.0' '34.3' '68.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        election_data_check = [15, 'Cantal', 2, '2ème circonscription', 'Complet', 2, 242, 107, 44.21, 135, 55.79, 11, 4.55, 8.15, 2, 0.83, 1.48, 122, 50.41, 90.37, 2, 'F', 'GUIBERT', 'Martine', 'ENS', 39, 16.12, 31.97, 'nan', '1.0', 'M', 'BONY', 'Jean-Yves', 'LR', 83, 34.3, 68.03, 'nan', 'nan']
        assert_test = AssertTest(self, 2)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data_model) 
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    def test_creator_dordogne_first_difficult_data_line(self) : 
        creator = CreatorElectionDataSecondRound(None, [])
        
        election_data_model = creator.factory_method("['24' 'Dordogne' 2 '2ème circonscription' 423 'Saint-Julien-Innocence_Eulalie' 'Complet' 202 83 '41.09' 119 '58.91' 13 '6.44' '10.92' 3 '1.49' '2.52' 103 '50.99' '86.55' 2 'M' 'DELPON' 'Michel' 'ENS' 50 '24.75' '48.54' '3.0' 'M' 'MULLER' 'Serge' 'RN' '53.0' '26.24' '51.46' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        election_data_check = [24, 'Dordogne', 2, '2ème circonscription', 'Complet', 2, 202, 83, 41.09, 119, 58.91, 13, 6.44, 10.92, 3, 1.49, 2.52, 103, 50.99, 86.55, 2, 'M', 'DELPON', 'Michel', 'ENS', 50, 24.75, 48.54, 'nan', '3.0', 'M', 'MULLER', 'Serge', 'RN', 53, 26.24, 51.46, 'nan', 'nan']
        assert_test = AssertTest(self, 2)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data_model) 
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    #rename this test to explain what I test (three candidates and bad end line )
    def test_creator_dordogne_three_candidates_second_round_data_line(self) :
        creator = CreatorElectionDataSecondRound(None, [])
        
        election_data_model = creator.factory_method("['24' 'Dordogne' 3 '3ème circonscription' 1 'Abjat-sur-Bandiat' 'Complet' 474 195 '41.14' 279 '58.86' 4 '0.84' '1.43' 4 '0.84' '1.43' 271 '57.17' '97.13' 3 'M' 'GIRARDEAU' 'Cyril' 'NUP' 110 '23.21' '40.59' '10.0' 'M' 'CUBERTAFON' 'Jean-Pierre' 'ENS' '90.0' '18.99' '33.21' '7.0' 'F' 'JOUBERT' 'Florence' 'RN' '71.0' '14.98' '26.2']")
        last_candidate_model_created = creator.last_element_created
        
        election_data_check = [24, 'Dordogne', 3, '3ème circonscription', 'Complet', 2, 474, 195, 41.14, 279, 58.86, 4, 0.84, 1.43, 4, 0.84, 1.43, 271, 57.17, 97.13, 3, 'M', 'GIRARDEAU', 'Cyril', 'NUP', 110, 23.21, 40.59, 'nan', '10.0', 'M', 'CUBERTAFON', 'Jean-Pierre', 'ENS', 90, 18.99, 33.21, 'nan', '7.0', 'F', 'JOUBERT', 'Florence', 'RN', 71, 14.98, 26.2, 'nan', 'nan', 'nan']
        assert_test = AssertTest(self, 3)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data_model) 
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    #rename with explanation of the cause of the bug
    def test_creator_seine_saint_denis_with_only_one_candidate(self) :
        creator = CreatorElectionDataSecondRound(None, [])
        
        election_data_model = creator.factory_method("['93' 'Seine-Saint-Denis' 4 '4ème circonscription' 7 'Le Blanc-Mesnil' 'Complet' 26143 19415 '74.26' 6728 '25.74' 1475 '5.64' '21.92' 185 '0.71' '2.75' 5068 '19.39' '75.33' 4 'F' 'BOUROUAHA' 'Soumya' 'NUP' 5068 '19.39' '100.0' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        election_data_check = [93, 'Seine-Saint-Denis', 4, '4ème circonscription', 'Complet', 2, 26143, 19415, 74.26, 6728, 25.74, 1475, 5.64, 21.92, 185, 0.71, 2.75, 5068, 19.39, 75.33, 4, 'F', 'BOUROUAHA', 'Soumya', 'NUP', 5068, 19.39, 100.0, 'nan', 'nan']
        assert_test = AssertTest(self, 1)
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data_model)
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    def test_creator_result_city_with_last_election_data_created_same_district(self) : 
        helper = HelperTest()
        last_election_data_created = helper.get_first_department_first_district_last_election_data_model()
        creator = CreatorElectionDataSecondRound(None, last_election_data_created)
        
        election_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 38 'Bény' 'Complet' 604 317 '52.48' 287 '47.52' 6 '0.99' '2.09' 6 '0.99' '2.09' 275 '45.53' '95.82' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 108 '17.88' '39.27' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '167.0' '27.65' '60.73' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        assert_test = AssertTest(self, 2)                                                                                                                                                                                                                               
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 931, 489, 52.54, 442, 47.46, 10, 1.105, 2.335, 11, 1.26, 2.66, 421, 45.09, 95.005, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 151, 15.515, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 270, 29.575, 65.64, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data)
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 604, 317, 52.48, 287, 47.52, 6, 0.99, 2.09, 6, 0.99, 2.09, 275, 45.53, 95.82, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 108, 17.88, 39.27, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 167, 27.65, 60.73, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    def test_creator_result_with_two_last_election_data_created_second_round_data(self) :  
        helper = HelperTest()
        last_election_data_created = helper.get_two_cities_data_first_department_first_district_last_election_data_model()
        creator = CreatorElectionDataSecondRound(None, last_election_data_created)
        
        election_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 29 'Beaupont' 'Complet' 446 239 '53.59' 207 '46.41' 10 '2.24' '4.83' 2 '0.45' '0.97' 195 '43.72' '94.2' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 67 '15.02' '34.36' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '128.0' '28.7' '65.64' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        assert_test = AssertTest(self, 2)
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 1377, 728, 52.89, 649, 47.11, 20, 1.483, 3.167, 13, 0.99, 2.097, 616, 44.633, 94.737, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 218, 15.35, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 398, 29.283, 65.64, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data)
        
        election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 2, 446, 239, 53.59, 207, 46.41, 10, 2.24, 4.83, 2, 0.45, 0.97, 195, 43.72, 94.2, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 67, 15.02, 34.36, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 128, 28.7, 65.64, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
    
    def test_creator_result_with_two_last_election_data_created_second_round_data_with_different_district_in_same_department(self) :  
        helper = HelperTest()
        last_election_data_created = helper.get_two_cities_data_first_department_first_district_last_election_data_model()
        creator = CreatorElectionDataSecondRound(None, last_election_data_created)
        
        election_data = creator.factory_method("['01' 'Ain' 2 '2ème circonscription' 8 'Ambutrix' 'Complet' 553 253 '45.75' 300 '54.25' 13 '2.35' '4.33' 23 '4.16' '7.67' 264 '47.74' '88.0' 1 'F' 'LAPRAY' 'Lumir' 'NUP' 116 '20.98' '43.94' '2.0' 'M' 'DAUBIÉ' 'Romain' 'ENS' '148.0' '26.76' '56.06' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        assert_test = AssertTest(self, 2)
        election_data_check = [1, 'Ain', 2, '2ème circonscription', 'Complet', 2, 553, 253, 45.75, 300, 54.25, 13, 2.35, 4.33, 23, 4.16, 7.67, 264, 47.74, 88 , 1, 'F', 'LAPRAY', 'Lumir', 'NUP', 116, 20.98, 43.94, 'nan', '2.0', 'M', 'DAUBIÉ', 'Romain', 'ENS', 148, 26.76, 56.06, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data)
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)
        
        
    def test_creator_result_with_two_last_election_data_created_second_round_data_with_same_district_name_in_different_department(self) :  
        helper = HelperTest()
        last_election_data_created = helper.get_two_cities_data_first_department_first_district_last_election_data_model()
        creator = CreatorElectionDataSecondRound(None, last_election_data_created)
        
        election_data = creator.factory_method("['02' 'Aisne' 1 '1ère circonscription' 2 'Achery' 'Complet' 444 247 '55.63' 197 '44.37' 12 '2.7' '6.09' 2 '0.45' '1.02' 183 '41.22' '92.89' 1 'F' 'BONO-VANDORME' 'Aude' 'ENS' 63 '14.19' '34.43' '7.0' 'M' 'DRAGON' 'Nicolas' 'RN' '120.0' '27.03' '65.57' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        last_candidate_model_created = creator.last_element_created
        
        assert_test = AssertTest(self, 2)
        election_data_check = [2, 'Aisne', 1, '1ère circonscription', 'Complet', 2, 444, 247, 55.63, 197, 44.37, 12, 2.7, 6.09, 2, 0.45, 1.02, 183, 41.22, 92.89, 1, 'F', 'BONO-VANDORME', 'Aude', 'ENS', 63, 14.19, 34.43,  'nan', '2.0', 'M', 'DRAGON', 'Nicolas', 'RN', 120, 27.03, 65.57, 'nan', 'nan']
        assert_test.assert_election_data_model_second_round_result(election_data_check, election_data)
        assert_test.assert_election_data_model_second_round_result(election_data_check, last_candidate_model_created)