import unittest
import datetime

from tests.helper_test import HelperTest
from src.Factory.CreatorCandidateData import CreatorCandidateData
from tests.base_unit_test import BaseUnitTest

class CreatorCandidateDataTest(BaseUnitTest):
#TODO refaire cette classe    
    def test_creator_candidate_data_factory_first_line(self) :        
        creator = self.get_creator()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' '1962-06-03 00:00:00' 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' '1963-05-26 00:00:00' 'Non']")
        
        candidate_data_check = [1, "Ain", 5, "5ème circonscription", 1, "Ain", "CROZET", "Sylvie", "F", 1, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1962,6,3), False, 'M', 'BOUVET', 'Didier', datetime.datetime(1963, 5, 26, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
     
        
    def test_creator_candidate_data_factory_second_line(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric' '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non' 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_new_line_caracter(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_tabulation_caracter(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\t '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\t 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
       
        
    def test_creator_candidate_data_factory_department_many_world(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
        candidate_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_department_with_apostrophe(self) : 
        creator = self.get_creator()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

        candidate_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
                
        
    def get_creator(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidateData(parties)
        return creator


    if __name__ == "__main__":
        unittest.main()