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
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n '1971-11-05 00:00:00'  'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' '1980-03-15 00:00:00' 'Non']")
         
        candidate_data_check = [2, "Aisne", 2, "2ème circonscription", 2, "Aisne", "LEPEUPLE", "Eric", "M", 9, "Commerçant et assimilé",  datetime.datetime(1971,11,5), False, 'F', 'MAZOUR', 'Vanessa', datetime.datetime(1980, 3, 15, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
       
        
    def test_creator_candidate_data_factory_territoires_de_belfort(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' '1993-04-16 00:00:00' 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' '1986-11-14 00:00:00' 'Non']")
        
        candidate_data_check = [90, "Territoire de Belfort", 1, "1ère circonscription", 90, "Territoire de Belfort", "GRUDLER", "Thiebaud", "M", 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  datetime.datetime(1993,4,16), False, 'F', 'GROSDIDIER', 'Maggy', datetime.datetime(1986, 11, 14, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_cotes_d_or(self) : 
        creator = self.get_creator()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n '1956-08-20 00:00:00' 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' '1972-09-29 00:00:00' 'Non']")

        candidate_data_check = [21, "Côte-d'Or", 1, "1ère circonscription", 21, "Côte-d'Or", "MARTIN", "Didier", "M", 7, "Profession intermédiaire de la santé et du travail social",  datetime.datetime(1956,8,20), True,'F', 'REFAIT-ALEXANDRE', 'Catherine', datetime.datetime(1972, 9, 29, 0, 0), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_corsica(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['2A' 'Corse-du-Sud'	1 '1ère circonscription'	2	15	'M'	'LIPPLER'	'Walter' '1961-06-02 00:00:00' 'DSV'	'Cadre de la fonction publique'	'Non'	'M'	'GOUILLON'	'Sylvain' '1960-08-08 00:00:00' 'Non'")
        
        candidate_data_check = [20, "Corse", 1, "1ère circonscription", 20, "Corse", "LIPPLER", "Walter", "M", 13, "Cadre de la fonction publique",  datetime.datetime(1961,6,2), False, 'M',	'GOUILLON',	'Sylvain',	datetime.datetime(1960,8 ,8, 0, 0),	False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_guadeloupe(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZA' 'Guadeloupe' 1 '1ère circonscription'	4	37	'M'	'NABAJOTH'	'Alix'	 '1973-11-11 00:00:00' 'DVG'	'Cadre de la fonction publique'	'Non'	'F'	'BARTEBIN-SOURHOU'	'Huguette' '1971-12-03 00:00:00' 'Non'")
        
        candidate_data_check = [971, "Guadeloupe", 1, "1ère circonscription", 971, "Guadeloupe", "NABAJOTH", "Alix", "M", 4, "Cadre de la fonction publique",  datetime.datetime(1973,11,11), False, 'F', 'BARTEBIN-SOURHOU', 'Huguette', datetime.datetime(1971, 12, 3, 0, 0),	False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_martinique(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZB' 'Martinique' 1 '1ère circonscription' 1	2	'M'	'TABAR'	'Jonathan'	 '1987-10-11 00:00:00' 'DVD'	'Employé civil et agent de service de la fonction publique'	'Non'	'F'	'JOSEPH'	'Joannifer' '1996-12-11 00:00:00' 'Non'")
        
        candidate_data_check = [972, "Martinique", 1, "1ère circonscription", 972, "Martinique", "TABAR", "Jonathan", "M", 12, "Employé civil et agent de service de la fonction publique",  datetime.datetime(1987,10,11), False, 'F',	'JOSEPH', 'Joannifer', datetime.datetime(1996,12,11), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_guyane(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZC' 'Guyane' 1	'1ère circonscription'	11	7 'M' 'MADÈRE' 'Christophe'  '1971-07-18 00:00:00' 'DVG'	'Professeur, profession scientifique'	'Non'	'F'	'BRIQUET'	'Ruth' '1993-05-06 00:00:00' 'Non'")
        
        candidate_data_check = [973, "Guyane", 1, "1ère circonscription", 973, "Guyane", "MADÈRE", "Christophe", "M", 4, "Professeur, profession scientifique",  datetime.datetime(1971,7,18), False, 'F',	'BRIQUET',	'Ruth',	datetime.datetime(1993,5,6), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_reunion(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZD' 'La Réunion' 1 '1ère circonscription' 2	9 'F' 'SISTERON' 'Murielle'	 '1987-02-16 00:00:00' 'LR'	'Profession libérale' 'Non'	'M'	'SERVIABLE'	'Mario' 'Luigi' '1949-05-23 00:00:00' 'Non'")
        
        candidate_data_check = [974, "La Réunion", 1, "1ère circonscription", 974, "La Réunion", "SISTERON", "Murielle", "F", 11, "Profession libérale",  datetime.datetime(1987,2,16), False, 'M',	'SERVIABLE', 'Mario Luigi', datetime.datetime(1949,5,23), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_mayotte(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZM' 'Mayotte'	1 '1ère circonscription'	2	21	'F'	'AOUNY'	'Yasmina' 'Myriam' '1986-03-31 00:00:00' 'DVG'	'Professeur, profession scientifique'	'Non'	'M'	'BACAR'	'Assoumani' 'Toufik' '1971-04-01 00:00:00' 'Non'")
        
        candidate_data_check = [976, "Mayotte", 1, "1ère circonscription", 976, "Mayotte", "AOUNY", "Yasmina Myriam", "F", 4, "Professeur, profession scientifique",  datetime.datetime(1986,3,31), False, 'M', 'BACAR', 'Assoumani Toufik',	datetime.datetime(1971,4,1), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_nouvelle_caledonie(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZN' 'Nouvelle-Calédonie'	1 '1ère circonscription'	1	2	'M'	'GIL' 'Antoine'	 '1956-05-26 00:00:00' 'DVD'	'Policier et militaire'	'Non'	'M'	'QUINET' 'Stéphane' '1965-12-25 00:00:00' 'Oui'")
        
        candidate_data_check = [988, "Nouvelle-Calédonie", 1, "1ère circonscription", 988, "Nouvelle-Calédonie", "GIL", "Antoine", "M", 12, "Policier et militaire",  datetime.datetime(1956,5,26), False, 'M',	'QUINET', 'Stéphane', datetime.datetime(1965,12,25), True]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_polynesie_francaise(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZP' 'Polynésie française'	1 '1ère circonscription'	1	15	'F'	'HAITI'	'Pascale'  '1972-04-03 00:00:00' 'DVD' 'Profession libérale'	'Non' 'F'	'NOUVEAU' 'Lydia' '1959-02-27 00:00:00' 'Non'")
        
        candidate_data_check = [987, "Polynésie française", 1, "1ère circonscription", 987, "Polynésie française", "HAITI", "Pascale", "F", 12, "Profession libérale",  datetime.datetime(1972,4,3), False, 'F', 'NOUVEAU', 'Lydia', datetime.datetime(1959,2,27), False]     
        self.assert_candidate_model(candidate_data_check, model)
        
        
    def test_creator_candidate_data_factory_saint_pierre_et_miquelon(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZS' 'Saint-Pierre-et-Miquelon'	1 '1ère circonscription'	3	3 'M'	'GASTON' 'Olivier'	 '1981-06-30 00:00:00' 'DVG'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'HELENE' 'Catherine' '1970-03-27 00:00:00' 'Non'")
        
        candidate_data_check = [975, "Saint-Pierre-et-Miquelon", 1, "1ère circonscription", 975, "Saint-Pierre-et-Miquelon", "GASTON", "Olivier", "M", 4, "Cadre administratif et commercial d'entreprise",  datetime.datetime(1981,6,30), False, 'F', 'HELENE', 'Catherine', datetime.datetime(1970,3,27), False]     
        self.assert_candidate_model(candidate_data_check, model)        
        
        
    def test_creator_candidate_data_factory_wallis_et_futuna(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZW' 'Wallis et Futuna'	1	'1ère circonscription'	3	7	'F'	'UGATAI' 'Sandrine' 'Aimée'	 '1973-06-23 00:00:00' 'DVC' 'Cadre administratif et commercial d'entreprise'	'Non' 'F' 'TAUVALE ÉPOUSE HANISI' 'Akata' '1976-03-27 00:00:00' 'Non'")
        
        candidate_data_check = [986, "Wallis et Futuna", 1, "1ère circonscription", 986, "Wallis et Futuna", "UGATAI", "Sandrine Aimée", "F", 8, "Cadre administratif et commercial d'entreprise",  datetime.datetime(1973,6,23), False, 'F', 'TAUVALE ÉPOUSE HANISI', 'Akata',	datetime.datetime(1976,3,27), False]     
        self.assert_candidate_model(candidate_data_check, model)        
        
        
    def test_creator_candidate_data_factory_saint_martin_saint_barthelemy(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZX' 'Saint-Martin/Saint-Barthélemy' 1 '1ère circonscription'	2	3	'M'	'GIBBS'	'Daniel'  '1968-08-01 00:00:00' 'DVD'	'Profession libérale'	'Non'	'M'	'GREAUX'	'Thomas' '1991-08-27 00:00:00' 'Non'")
        
        candidate_data_check = [978, "Saint-Martin/Saint-Barthélemy", 1, "1ère circonscription", 978, "Saint-Martin/Saint-Barthélemy", "GIBBS", "Daniel", "M", 12, "Profession libérale",  datetime.datetime(1968,8,1), False, 'M',	'GREAUX', 'Thomas',	datetime.datetime(1991,8,27), False]     
        self.assert_candidate_model(candidate_data_check, model)        
        
        
    def test_creator_candidate_data_factory_french_strangers(self):
        creator = self.get_creator()
        
        model = creator.factory_method("['ZZ' 'Français établis hors de France' 4	'4ème circonscription'	5	64	'F'	'GONDARD' 'Cécilia'	 '1980-06-04 00:00:00' 'NUP'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'LIBEAUT'	'Catherine' '1963-09-26 00:00:00' 'Non'")
        
        candidate_data_check = [99, "Français établis hors de France", 4, "4ème circonscription", 99, "Français établis hors de France", "GONDARD", "Cécilia", "F", 3, "Cadre administratif et commercial d'entreprise",  datetime.datetime(1980,6,4), False, 'F', 'LIBEAUT', 'Catherine', datetime.datetime(1963,9,26), False]     
        self.assert_candidate_model(candidate_data_check, model)        
        
        
    def get_creator(self) : 
        helper = HelperTest()
        parties = helper.get_parties()
        creator = CreatorCandidateData(parties)
        return creator


    if __name__ == "__main__":
        unittest.main()