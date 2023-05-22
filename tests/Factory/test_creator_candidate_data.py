import unittest
import datetime

from src.Factory.CreatorCandidateData import CreatorCandidateData
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorCandidateDataTest(unittest.TestCase):
#TODO refaire cette classe    
    def test_creator_candidate_data_factory_first_line(self) :        
        creator = self.__get_creator()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' '1962-06-03 00:00:00' 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' '1963-05-26 00:00:00' 'Non']")
        
        candidate_data_check = [1, "Ain", 5, "5ème circonscription", 1, "Ain", "CROZET", "Sylvie", "F", 1, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1962,6,3), False, 'M', 'BOUVET', 'Didier', datetime.datetime(1963, 5, 26, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
     
        
    def test_creator_candidate_data_factory_second_line(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric' '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non' 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_new_line_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_tabulation_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\t '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\t 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
       
        
    def test_creator_candidate_data_factory_department_many_world(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
        candidate_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_department_with_apostrophe(self) : 
        creator = self.__get_creator()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

        candidate_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(candidate_data_check, model)
                        
        
    def __get_creator(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidateData(parties)
        return creator
        
        
    def test_creator_candidate_data_district_first_round_first_line(self):
        creator = CreatorCandidateData(None)
            
        candidate_data = creator.factory_method_first_round("['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']")
       
        candidate_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3, 2, 'M', 'LAHY', 'Éric', 'DXG', 391, 0.45, 0.94, 'nan', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 9982, 11.58, 23.87, 'nan', 7, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, 1.35, 2.78, 'nan', 1, 'M', 'GUILLERMIN', 'Vincent', 'ENS', 8071, 9.36, 19.3, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 10599, 12.3, 25.35, 'nan', '5.0', 'M', 'MENDES', 'Michael', 'DSV', 641, 0.74, 1.53, 'nan', '6.0', 'M', 'BELLON', 'Julien', 'REC', 1995, 2.31, 4.77, 'nan', '4.0', 'F', 'PIROUX GIANNOTTI', 'Brigitte', 'RN', 8971, 10.41, 21.46, 'nan', 'nan']
        assert_test = AssertTest(self, 8)        
        assert_test.assert_candidate_data_model_from_first_round_result(candidate_data_check, candidate_data)
        
        
    def test_creator_result_district_first_round_one_hundred_and_first_line(self):
        creator = CreatorCandidateData(None)
            
        candidate_data = creator.factory_method_first_round("['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
        candidate_data_check = [25, 'Doubs', 2, '2ème circonscription', 'Complet', 79162, 37688, 47.61, 41474, 52.39, 821, 1.04, 1.98, 326, 0.41, 0.79, 40327, 50.94, 97.23, 8, 'F', 'VUITTON', 'Brigitte', 'DXG', 779, 0.98, 1.93, 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, 16.56, 32.51, 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, 0.27, 0.54, 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, 0, 0, 'nan', 3, 'M', 'ALAUZET', 'Eric', 'ENS', 12647, 15.98, 31.36, 'nan', 1, 'F', 'KAOULAL', 'Chafia', 'LR', 4354, 5.5, 10.8, 'nan', 7, 'M', 'PRENEL', 'Jim', 'DSV', 692, 0.87, 1.72, 'nan', 5, 'F', 'CARRAU', 'Barbara', 'REC', 1472, 1.86, 3.65, 'nan', 9, 'M', 'FUSIS', 'Eric', 'RN', 7055, 8.91, 17.49, 'nan', 'nan']
        assert_test = AssertTest(self, 9)
        assert_test.assert_candidate_data_model_from_first_round_result(candidate_data_check, candidate_data) 


    if __name__ == "__main__":
        unittest.main()