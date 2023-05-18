import unittest
import datetime

from tests.helper_test import HelperTest
from src.Factory.CreatorCandidateData import CreatorCandidateData
from tests.base_unit_test import BaseUnitTest

class CreatorCandidateDataTest(BaseUnitTest):
#TODO refaire cette classe    
    def test_creator_candidate_data_factory_first_line(self) :        
        creator = self.__get_creator()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' '1962-06-03 00:00:00' 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' '1963-05-26 00:00:00' 'Non']")
        
        candidate_data_check = [1, "Ain", 5, "5ème circonscription", 1, "Ain", "CROZET", "Sylvie", "F", 1, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1962,6,3), False, 'M', 'BOUVET', 'Didier', datetime.datetime(1963, 5, 26, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
     
        
    def test_creator_candidate_data_factory_second_line(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric' '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non' 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_new_line_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_tabulation_caracter(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\t '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\t 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
       
        
    def test_creator_candidate_data_factory_department_many_world(self):
        creator = self.__get_creator()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
        candidate_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_department_with_apostrophe(self) : 
        creator = self.__get_creator()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

        candidate_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
                        
        
    def __get_creator(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidateData(parties)
        return creator
        
        
    #TODO factoriser les assert des deux prochaines méthodes
    def test_creator_candidate_data_district_first_round_first_line(self):
        creator = CreatorCandidateData(None)
            
        candidate_data = creator.factory_method_first_round("['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']")
            
        self.assertTrue(candidate_data.department != None)
        self.assertEqual(1, candidate_data.department.number)
        self.assertEqual('Ain', candidate_data.department.name)
        self.assertTrue(candidate_data.district != None)
        self.assertEqual(1, candidate_data.district.number)
        self.assertEqual('1ère circonscription', candidate_data.district.name)
        self.assertEqual('Complet', candidate_data.election.state_compute)
        self.assertEqual(86187, candidate_data.election.registered)
        self.assertEqual(43652, candidate_data.election.abstaining)
        self.assertEqual(50.65, candidate_data.election.rate_abstaining)
        self.assertEqual(42535, candidate_data.election.voting)
        self.assertEqual(49.35, candidate_data.election.rate_voting)  
        self.assertEqual(490, candidate_data.election.blank_balot)    
        self.assertEqual(0.57, candidate_data.election.rate_blank_registered)   
        self.assertEqual(1.15, candidate_data.election.rate_blank_voting)       
        self.assertEqual(234, candidate_data.election.null_ballot)  
        self.assertEqual(0.27, candidate_data.election.rate_null_registered)  
        self.assertEqual(0.55, candidate_data.election.rate_null_voting)  
        self.assertEqual(41811, candidate_data.election.expressed)  
        self.assertEqual(48.51, candidate_data.election.rate_express_registered)  
        self.assertEqual(98.3, candidate_data.election.rate_express_voting)  
        self.assertEqual(8, len(candidate_data.candidates))
        self.assertEqual('M', candidate_data.candidates[0].sexe)
        self.assertEqual('LAHY', candidate_data.candidates[0].last_name)
        self.assertEqual('Éric', candidate_data.candidates[0].first_name)
        self.assertEqual(391, candidate_data.candidates[0].vote)
        self.assertEqual(0.45, candidate_data.candidates[0].rate_vote_registered)
        self.assertEqual(0.94, candidate_data.candidates[0].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[1].sexe)
        self.assertEqual('GUÉRAUD', candidate_data.candidates[1].last_name)
        self.assertEqual('Sébastien', candidate_data.candidates[1].first_name)
        self.assertEqual(9982, candidate_data.candidates[1].vote)
        self.assertEqual(11.58, candidate_data.candidates[1].rate_vote_registered)
        self.assertEqual(23.87, candidate_data.candidates[1].rate_vote_expressed)
        self.assertEqual('F', candidate_data.candidates[2].sexe)
        self.assertEqual('ARMENJON', candidate_data.candidates[2].last_name)
        self.assertEqual('Eliane', candidate_data.candidates[2].first_name)
        self.assertEqual(1161, candidate_data.candidates[2].vote)
        self.assertEqual(1.35, candidate_data.candidates[2].rate_vote_registered)
        self.assertEqual(2.78, candidate_data.candidates[2].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[3].sexe)
        self.assertEqual('GUILLERMIN', candidate_data.candidates[3].last_name)
        self.assertEqual('Vincent', candidate_data.candidates[3].first_name)
        self.assertEqual(8071, candidate_data.candidates[3].vote)
        self.assertEqual(9.36, candidate_data.candidates[3].rate_vote_registered)
        self.assertEqual(19.3, candidate_data.candidates[3].rate_vote_expressed)        
        self.assertEqual('M', candidate_data.candidates[4].sexe)
        self.assertEqual('BRETON', candidate_data.candidates[4].last_name)
        self.assertEqual('Xavier', candidate_data.candidates[4].first_name)
        self.assertEqual(10599, candidate_data.candidates[4].vote)
        self.assertEqual(12.3, candidate_data.candidates[4].rate_vote_registered)
        self.assertEqual(25.35, candidate_data.candidates[4].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[5].sexe)
        self.assertEqual('MENDES', candidate_data.candidates[5].last_name)
        self.assertEqual('Michael', candidate_data.candidates[5].first_name)
        self.assertEqual(641, candidate_data.candidates[5].vote)
        self.assertEqual(0.74, candidate_data.candidates[5].rate_vote_registered)
        self.assertEqual(1.53, candidate_data.candidates[5].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[6].sexe)
        self.assertEqual('BELLON', candidate_data.candidates[6].last_name)
        self.assertEqual('Julien', candidate_data.candidates[6].first_name)
        self.assertEqual(1995, candidate_data.candidates[6].vote)
        self.assertEqual(2.31, candidate_data.candidates[6].rate_vote_registered)
        self.assertEqual(4.77, candidate_data.candidates[6].rate_vote_expressed)
        self.assertEqual('F', candidate_data.candidates[7].sexe)
        self.assertEqual('PIROUX GIANNOTTI', candidate_data.candidates[7].last_name)
        self.assertEqual('Brigitte', candidate_data.candidates[7].first_name)
        self.assertEqual(8971, candidate_data.candidates[7].vote)
        self.assertEqual(10.41, candidate_data.candidates[7].rate_vote_registered)
        self.assertEqual(21.46, candidate_data.candidates[7].rate_vote_expressed)
        
        
    def test_creator_election_district_first_round_one_hundred_and_first_line(self):
        creator = CreatorCandidateData(None)
            
        candidate_data = creator.factory_method_first_round("['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
            
        self.assertTrue(candidate_data.department != None)
        self.assertEqual(25, candidate_data.department.number)
        self.assertEqual('Doubs', candidate_data.department.name)
        self.assertTrue(candidate_data.district != None)
        self.assertEqual(2, candidate_data.district.number)
        self.assertEqual('2ème circonscription', candidate_data.district.name)
        self.assertEqual('Complet', candidate_data.election.state_compute)
        self.assertEqual(79162, candidate_data.election.registered)
        self.assertEqual(37688, candidate_data.election.abstaining)
        self.assertEqual(47.61, candidate_data.election.rate_abstaining)
        self.assertEqual(41474, candidate_data.election.voting)
        self.assertEqual(52.39, candidate_data.election.rate_voting)  
        self.assertEqual(821, candidate_data.election.blank_balot)    
        self.assertEqual(1.04, candidate_data.election.rate_blank_registered)   
        self.assertEqual(1.98, candidate_data.election.rate_blank_voting)       
        self.assertEqual(326, candidate_data.election.null_ballot)  
        self.assertEqual(0.41, candidate_data.election.rate_null_registered)  
        self.assertEqual(0.79, candidate_data.election.rate_null_voting)  
        self.assertEqual(40327, candidate_data.election.expressed)  
        self.assertEqual(50.94, candidate_data.election.rate_express_registered)  
        self.assertEqual(97.23, candidate_data.election.rate_express_voting)  
        self.assertEqual(9, len(candidate_data.candidates))
        self.assertEqual('F', candidate_data.candidates[0].sexe)
        self.assertEqual('VUITTON', candidate_data.candidates[0].last_name)
        self.assertEqual('Brigitte', candidate_data.candidates[0].first_name)
        self.assertEqual(779, candidate_data.candidates[0].vote)
        self.assertEqual(0.98, candidate_data.candidates[0].rate_vote_registered)
        self.assertEqual(1.93, candidate_data.candidates[0].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[1].sexe)
        self.assertEqual('RAVACLEY', candidate_data.candidates[1].last_name)
        self.assertEqual('Stéphane', candidate_data.candidates[1].first_name)
        self.assertEqual(13112, candidate_data.candidates[1].vote)
        self.assertEqual(16.56, candidate_data.candidates[1].rate_vote_registered)
        self.assertEqual(32.51, candidate_data.candidates[1].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[2].sexe)
        self.assertEqual('THOMASSIN', candidate_data.candidates[2].last_name)
        self.assertEqual('Geoffrey', candidate_data.candidates[2].first_name)
        self.assertEqual(216, candidate_data.candidates[2].vote)
        self.assertEqual(0.27, candidate_data.candidates[2].rate_vote_registered)
        self.assertEqual(0.54, candidate_data.candidates[2].rate_vote_expressed)
        self.assertEqual('F', candidate_data.candidates[3].sexe)
        self.assertEqual('MEYER', candidate_data.candidates[3].last_name)
        self.assertEqual('Claudine', candidate_data.candidates[3].first_name)
        self.assertEqual(0, candidate_data.candidates[3].vote)
        self.assertEqual(0.0, candidate_data.candidates[3].rate_vote_registered)
        self.assertEqual(0.0, candidate_data.candidates[3].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[4].sexe)
        self.assertEqual('ALAUZET', candidate_data.candidates[4].last_name)
        self.assertEqual('Eric', candidate_data.candidates[4].first_name)
        self.assertEqual(12647, candidate_data.candidates[4].vote)
        self.assertEqual(15.98, candidate_data.candidates[4].rate_vote_registered)
        self.assertEqual(31.36, candidate_data.candidates[4].rate_vote_expressed)
        self.assertEqual('F', candidate_data.candidates[5].sexe)
        self.assertEqual('KAOULAL', candidate_data.candidates[5].last_name)
        self.assertEqual('Chafia', candidate_data.candidates[5].first_name)
        self.assertEqual(4354, candidate_data.candidates[5].vote)
        self.assertEqual(5.5, candidate_data.candidates[5].rate_vote_registered)
        self.assertEqual(10.8, candidate_data.candidates[5].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[6].sexe)
        self.assertEqual('PRENEL', candidate_data.candidates[6].last_name)
        self.assertEqual('Jim', candidate_data.candidates[6].first_name)
        self.assertEqual(692, candidate_data.candidates[6].vote)
        self.assertEqual(0.87, candidate_data.candidates[6].rate_vote_registered)
        self.assertEqual(1.72, candidate_data.candidates[6].rate_vote_expressed)
        self.assertEqual('F', candidate_data.candidates[7].sexe)
        self.assertEqual('CARRAU', candidate_data.candidates[7].last_name)
        self.assertEqual('Barbara', candidate_data.candidates[7].first_name)
        self.assertEqual(1472, candidate_data.candidates[7].vote)
        self.assertEqual(1.86, candidate_data.candidates[7].rate_vote_registered)
        self.assertEqual(3.65, candidate_data.candidates[7].rate_vote_expressed)
        self.assertEqual('M', candidate_data.candidates[8].sexe)
        self.assertEqual('FUSIS', candidate_data.candidates[8].last_name)
        self.assertEqual('Eric', candidate_data.candidates[8].first_name)
        self.assertEqual(7055, candidate_data.candidates[8].vote)
        self.assertEqual(8.91, candidate_data.candidates[8].rate_vote_registered)
        self.assertEqual(17.49, candidate_data.candidates[8].rate_vote_expressed)


    if __name__ == "__main__":
        unittest.main()