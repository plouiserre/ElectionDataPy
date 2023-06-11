import unittest
import datetime

from src.Factory.CreatorElectionData import CreatorElectionData
from src.Models.CandidateModel import CandidateModel
from src.Models.DepartmentModel import DepartmentModel
from src.Models.DeputyModel import DeputyModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionDataModel import ElectionDataModel
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest

class CreatorElectionDataTest(unittest.TestCase):    
    #TODO tester aussi le last_election_data_created
    # def test_creator_election_data_factory_first_line(self) :        
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' '1962-06-03 00:00:00' 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' '1963-05-26 00:00:00' 'Non']")
        
    #     election_data_check = [1, "Ain", 5, "5ème circonscription", 1, "Ain", "CROZET", "Sylvie", "F", 1, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1962,6,3), False, 'M', 'BOUVET', 'Didier', datetime.datetime(1963, 5, 26, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    # def test_creator_election_data_factory_second_line_with_last_election_data_saved_same_district(self) : 
    #     creator = self.__get_creator()               
    #     creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
    #     model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
    #     elections_data_check= [[creator.last_election_data_created.department.number, creator.last_election_data_created.department.name, 
    #                             creator.last_election_data_created.district.number, creator.last_election_data_created.district.name,  
    #                             [['CROZET', 'Sylvie', 'F', 1, 'Profession intermédiaire de la santé et du travail social', datetime.datetime(1962,6,3), False ],
    #                             ['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
    #                             [['BOUVET', 'Didier', 'M', datetime.datetime(1963,5,26), False ], ['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
    #     assert_test = AssertTest(self, 2)
    #     elections_data_model = [model]
    #     assert_test.assert_elections_model(elections_data_check, elections_data_model)
    #     self.assertFalse(creator.is_new_election_data_model_created)
        
    #     assert_test.assert_last_election_data_created(creator.last_election_data_created, model)
        
        
    # def test_creator_election_data_factory_third_line_with_last_election_data_saved_other_district(self) : 
    #     creator = self.__get_creator()               
    #     creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
    #     model = creator.factory_method("['01' 'Ain' 6 '6ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
        
    #     elections_data_check= [[creator.last_election_data_created.department.number, creator.last_election_data_created.department.name, 
    #                             6, '6ème circonscription',  
    #                             [['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
    #                             [['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
    #     assert_test = AssertTest(self, 1)
    #     elections_data_model = [model]
    #     assert_test.assert_elections_model(elections_data_check, elections_data_model)
    #     self.assertTrue(creator.is_new_election_data_model_created)
        
    #     assert_test.assert_last_election_data_created(creator.last_election_data_created, model)
        
        
    # def test_creator_election_data_factory_third_line_with_last_election_data_saved_other_department_same_district_number(self) : 
    #     creator = self.__get_creator()               
    #     creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
    #     model = creator.factory_method("['02' 'Aisne' 5 '5ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
    #     elections_data_check= [[2, 'Aisne', creator.last_election_data_created.district.number, creator.last_election_data_created.district.name,  
    #                             [['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
    #                             [['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
    #     assert_test = AssertTest(self, 1)
    #     elections_data_model = [model]
    #     assert_test.assert_elections_model(elections_data_check, elections_data_model)
    #     self.assertTrue(creator.is_new_election_data_model_created)
    #     assert_test.assert_last_election_data_created(creator.last_election_data_created, model)  
     
     
    # def __get_last_election_data_model_saved(self) :
    #     elec = ElectionDataModel()
    #     department = DepartmentModel()
    #     department.name = 'Ain'
    #     department.number = 1
    #     district = DistrictModel()
    #     district.name = '5ème circonscription'
    #     district.number = 5
    #     candidate = CandidateModel()
    #     candidate.last_name = 'CROZET'
    #     candidate.first_name = 'Sylvie'
    #     candidate.birthdate = datetime.datetime(1962,6,3)
    #     candidate.party_id = 1
    #     candidate.job = 'Profession intermédiaire de la santé et du travail social'
    #     candidate.sexe = 'F'
    #     deputy = DeputyModel()
    #     deputy.last_name = 'BOUVET'
    #     deputy.sexe = 'M'
    #     deputy.first_name = 'Didier' 
    #     deputy.birthdate = datetime.datetime(1963,5,26)
    #     elec.department = department
    #     elec.district = district
    #     elec.district.department = department
    #     elec.candidates.append(candidate)
    #     elec.deputies.append(deputy)        
    #     return elec
    
        
    # def test_creator_election_data_factory_second_line(self):
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric' '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non' 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
    #     election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    # def test_creator_election_data_factory_new_line_caracter(self):
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
    #     election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    # def test_creator_election_data_factory_tabulation_caracter(self):
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\t '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\t 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
    #     election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
       
        
    # def test_creator_election_data_factory_department_many_world(self):
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
    #     election_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    # def test_creator_election_data_factory_department_with_apostrophe(self) : 
    #     creator = self.__get_creator()
        
    #     model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

    #     election_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
    #     assert_test = AssertTest(self, 0)
    #     assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
                        
        
    # def __get_creator(self) : 
    #     helper = HelperTest()
    #     parties = helper.get_parties()
    #     creator = CreatorElectionData(parties)
    #     return creator
        
        
    # def test_creator_election_data_district_first_round_first_line(self):
    #     creator = CreatorElectionData(None)
            
    #     election_data = creator.factory_method_first_round("['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']")
       
    #     election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3, 2, 'M', 'LAHY', 'Éric', 'DXG', 391, 0.45, 0.94, 'nan', 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 9982, 11.58, 23.87, 'nan', 7, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, 1.35, 2.78, 'nan', 1, 'M', 'GUILLERMIN', 'Vincent', 'ENS', 8071, 9.36, 19.3, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 10599, 12.3, 25.35, 'nan', '5.0', 'M', 'MENDES', 'Michael', 'DSV', 641, 0.74, 1.53, 'nan', '6.0', 'M', 'BELLON', 'Julien', 'REC', 1995, 2.31, 4.77, 'nan', '4.0', 'F', 'PIROUX GIANNOTTI', 'Brigitte', 'RN', 8971, 10.41, 21.46, 'nan', 'nan']
    #     assert_test = AssertTest(self, 8)        
    #     assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data)
        
        
    # def test_creator_result_district_first_round_one_hundred_and_first_line(self):
    #     creator = CreatorElectionData(None)
            
    #     election_data = creator.factory_method_first_round("['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
    #     election_data_check = [25, 'Doubs', 2, '2ème circonscription', 'Complet', 79162, 37688, 47.61, 41474, 52.39, 821, 1.04, 1.98, 326, 0.41, 0.79, 40327, 50.94, 97.23, 8, 'F', 'VUITTON', 'Brigitte', 'DXG', 779, 0.98, 1.93, 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, 16.56, 32.51, 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, 0.27, 0.54, 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, 0, 0, 'nan', 3, 'M', 'ALAUZET', 'Eric', 'ENS', 12647, 15.98, 31.36, 'nan', 1, 'F', 'KAOULAL', 'Chafia', 'LR', 4354, 5.5, 10.8, 'nan', 7, 'M', 'PRENEL', 'Jim', 'DSV', 692, 0.87, 1.72, 'nan', 5, 'F', 'CARRAU', 'Barbara', 'REC', 1472, 1.86, 3.65, 'nan', 9, 'M', 'FUSIS', 'Eric', 'RN', 7055, 8.91, 17.49, 'nan', 'nan']
    #     assert_test = AssertTest(self, 9)
    #     assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data) 
        
        
    # def test_creator_result_city_second_round_first_line(self) : 
    #     creator = CreatorElectionData(None)
        
    #     election_data = creator.factory_method_second_round("['01' 'Ain' 1 '1ère circonscription' 16 'Arbigny' 'Complet' 327 172 '52.6' 155 '47.4' 4 '1.22' '2.58' 5 '1.53' '3.23' 146 '44.65' '94.19' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 43 '13.15' '29.45' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '103.0' '31.5' '70.55' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
    #     election_data_check = [1, 'Ain', 1, '1ère circonscription', 'Complet', 327, 172, 52.6, 155, 47.4, 4, 1.22, 2.58, 5, 1.53, 3.23, 146, 44.65, 94.19, 8, 'M', 'GUÉRAUD', 'Sébastien', 'NUP', 43, 13.15, 29.45, 'nan', '3.0', 'M', 'BRETON', 'Xavier', 'LR', 103, 31.5, 70.55, 'nan', 'nan']
    #     assert_test = AssertTest(self, 1)
    #     assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data) 
        
        
    # def test_creator_result_city_second_round_cantal_district_line(self) : 
    #     creator = CreatorElectionData(None)
        
    #     election_data = creator.factory_method_second_round("['15' 'Cantal' 2 '2ème circonscription' 69 'Ferrières-Saint-Mary' 'Complet' 242 107 '44.21' 135 '55.79' 11 '4.55' '8.15' 2 '0.83' '1.48' 122 '50.41' '90.37' 2 'F' 'GUIBERT' 'Martine' 'ENS' 39 '16.12' '31.97' '1.0' 'M' 'BONY' 'Jean-Yves' 'LR' '83.0' '34.3' '68.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
        
    #     election_data_check = [15, 'Cantal', 2, '2ème circonscription', 'Complet', 242, 107, 44.21, 135, 55.79, 11, 4.55, 8.15, 2, 0.83, 1.48, 122, 50.41, 90.37, 2, 'F', 'GUIBERT', 'Martine', 'ENS', 39, 16.12, 31.97, 'nan', '1.0', 'M', 'BONY', 'Jean-Yves', 'LR', 83, 34.3, 68.03, 'nan', 'nan']
    #     assert_test = AssertTest(self, 1)
    #     assert_test.assert_election_data_model_from_rounds_result(election_data_check, election_data) 


    if __name__ == "__main__":
        unittest.main()