import datetime
import unittest

from src.Factory.CreatorElectionDataCandidatesList import CreatorElectionDataCandidatesList
from src.Models.CandidateModel import CandidateModel
from src.Models.DepartmentModel import DepartmentModel
from src.Models.DeputyModel import DeputyModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionDataModel import ElectionDataModel
from tests.assert_test import AssertTest
from tests.helper_test import HelperTest


class CreatorElectionDataCandidatesListTest(unittest.TestCase) :
    def test_creator_election_data_factory_first_line(self) :        
        creator = self.__get_creator()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' '1962-06-03 00:00:00' 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' '1963-05-26 00:00:00' 'Non']")
        
        election_data_check = [1, "Ain", 5, "5ème circonscription", 1, "Ain", "CROZET", "Sylvie", "F", 1, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1962,6,3), False, 'M', 'BOUVET', 'Didier', datetime.datetime(1963, 5, 26, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    def test_creator_election_data_factory_second_line_with_last_election_data_saved_same_district(self) : 
        creator = self.__get_creator()               
        creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
        elections_data_check= [[creator.last_election_data_created.department.number, creator.last_election_data_created.department.name, 
                                creator.last_election_data_created.district.number, creator.last_election_data_created.district.name,  
                                [['CROZET', 'Sylvie', 'F', 1, 'Profession intermédiaire de la santé et du travail social', datetime.datetime(1962,6,3), False ],
                                ['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
                                [['BOUVET', 'Didier', 'M', datetime.datetime(1963,5,26), False ], ['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
        assert_test = AssertTest(self, 2)
        elections_data_model = [model]
        assert_test.assert_elections_model(elections_data_check, elections_data_model)
        self.assertFalse(creator.is_new_election_data_model_created)
        
        assert_test.assert_last_election_data_created(creator.last_election_data_created, model)
        
        
    def test_creator_election_data_factory_third_line_with_last_election_data_saved_other_district(self) : 
        creator = self.__get_creator()               
        creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
        model = creator.factory_method("['01' 'Ain' 6 '6ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
        
        elections_data_check= [[creator.last_election_data_created.department.number, creator.last_election_data_created.department.name, 
                                6, '6ème circonscription',  
                                [['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
                                [['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
        assert_test = AssertTest(self, 1)
        elections_data_model = [model]
        assert_test.assert_elections_model(elections_data_check, elections_data_model)
        self.assertTrue(creator.is_new_election_data_model_created)
        
        assert_test.assert_last_election_data_created(creator.last_election_data_created, model)
        
        
    def test_creator_election_data_factory_third_line_with_last_election_data_saved_other_department_same_district_number(self) : 
        creator = self.__get_creator()               
        creator.last_election_data_created = self.__get_last_election_data_model_saved()
        
        model = creator.factory_method("['02' 'Aisne' 5 '5ème circonscription' 3 27 'M' 'YILMAZ' 'Celil' '1975-10-30 00:00:00' 'DIV' 'Profession intermédiaire administrative et commerciale des entreprises' 'Oui' 'M' 'ORAN' 'Mahmut' '1980-06-09 00:00:00' 'Non']")
        
        elections_data_check= [[2, 'Aisne', creator.last_election_data_created.district.number, creator.last_election_data_created.district.name,  
                                [['YILMAZ', 'Celil', 'M', 9, 'Profession intermédiaire administrative et commerciale des entreprises', datetime.datetime(1975,10,30), True]], 
                                [['ORAN', 'Mahmut', 'M', datetime.datetime(1980,6,9),  False]]]]
        assert_test = AssertTest(self, 1)
        elections_data_model = [model]
        assert_test.assert_elections_model(elections_data_check, elections_data_model)
        self.assertTrue(creator.is_new_election_data_model_created)
        assert_test.assert_last_election_data_created(creator.last_election_data_created, model)  
     
     
    def __get_last_election_data_model_saved(self) :
        elec = ElectionDataModel()
        department = DepartmentModel()
        department.name = 'Ain'
        department.number = 1
        district = DistrictModel()
        district.name = '5ème circonscription'
        district.number = 5
        candidate = CandidateModel()
        candidate.last_name = 'CROZET'
        candidate.first_name = 'Sylvie'
        candidate.birthdate = datetime.datetime(1962,6,3)
        candidate.party_id = 1
        candidate.job = 'Profession intermédiaire de la santé et du travail social'
        candidate.sexe = 'F'
        deputy = DeputyModel()
        deputy.last_name = 'BOUVET'
        deputy.sexe = 'M'
        deputy.first_name = 'Didier' 
        deputy.birthdate = datetime.datetime(1963,5,26)
        elec.department = department
        elec.district = district
        elec.district.department = department
        elec.candidates.append(candidate)
        elec.deputies.append(deputy)        
        return elec
    
        
    def test_creator_election_data_factory_second_line(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric' '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non' 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    def test_creator_election_data_factory_new_line_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    def test_creator_election_data_factory_tabulation_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\t '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\t 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        election_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
       
        
    def test_creator_election_data_factory_department_many_world(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
        election_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
        
        
    def test_creator_election_data_factory_department_with_apostrophe(self) : 
        creator = self.__get_creator()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

        election_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
        assert_test = AssertTest(self, 0)
        assert_test.assert_all_candidates_infos_with_deputy(election_data_check, model)
                        
        
    def __get_creator(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorElectionDataCandidatesList(parties)
        return creator