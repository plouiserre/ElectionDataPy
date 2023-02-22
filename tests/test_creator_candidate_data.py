import unittest
from src.Factory.CreatorCandidateData import CreatorCandidateData

class CreatorCandidateDataTest(unittest.TestCase):
    def test_creator_candidate_data_factory_first_line(self) :
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']")
     
        self.assertEqual(1, model.department.number)
        self.assertEqual("Ain", model.department.name)
        self.assertEqual(5, model.district_number)
        self.assertEqual("5ème circonscription", model.district_name)
        self.assertEqual("CROZET", model.candidate_last_name)
        self.assertEqual("Sylvie", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("DXG",model.candidate_party)
        self.assertEqual("Profession intermédiaire de la santé et du travail social", model.candidate_job)
        self.assertEqual("6/3/1962",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_second_line(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n datetime.datetime(1971, 11, 5, 0, 0) 'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' datetime.datetime(1980, 3, 15, 0, 0) 'Non']")
        
        self.assertEqual(2, model.department.number)
        self.assertEqual("Aisne", model.department.name)
        self.assertEqual(2, model.district_number)
        self.assertEqual("2ème circonscription", model.district_name)
        self.assertEqual("LEPEUPLE", model.candidate_last_name)
        self.assertEqual("Eric", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DIV",model.candidate_party)
        self.assertEqual("Commerçant et assimilé", model.candidate_job)
        self.assertEqual("11/5/1971",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_territoires_de_belfort(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' datetime.datetime(1993, 4, 16, 0, 0) 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' datetime.datetime(1986, 11, 14, 0, 0)\n 'Non']")
        
        self.assertEqual(90, model.department.number)
        self.assertEqual("Territoire de Belfort", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("GRUDLER", model.candidate_last_name)
        self.assertEqual("Thiebaud", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("ENS",model.candidate_party)
        self.assertEqual("Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", model.candidate_job)
        self.assertEqual("4/16/1993",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_cotes_d_or(self) : 
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n datetime.datetime(1956, 8, 20, 0, 0) 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' datetime.datetime(1972, 9, 29, 0, 0) 'Non']")

        self.assertEqual(21, model.department.number)        
        self.assertEqual("Côte-d'Or", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("MARTIN", model.candidate_last_name)
        self.assertEqual("Didier", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("ENS",model.candidate_party)
        self.assertEqual("Profession intermédiaire de la santé et du travail social", model.candidate_job)
        self.assertEqual("8/20/1956",model.candidate_birth_date)
        self.assertEqual(True, model.candidate_is_sorting)
        
    #TODO début import   
    def test_creator_candidate_data_factory_corsica(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['2A' 'Corse-du-Sud'	1 '1ère circonscription'	2	15	'M'	'LIPPLER'	'Walter'	datetime.datetime(1961, 02, 5, 0, 0) 'DSV'	'Cadre de la fonction publique'	'Non'	'M'	'GOUILLON'	'Sylvain'	datetime.datetime(1960,8 ,8, 0, 0)	'Non'")
        
        self.assertEqual(20, model.department.number)
        self.assertEqual("Corse", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("LIPPLER", model.candidate_last_name)
        self.assertEqual("Walter", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DSV",model.candidate_party)
        self.assertEqual("Cadre de la fonction publique", model.candidate_job)
        self.assertEqual("02/5/1961",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_guadeloupe(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZA' 'Guadeloupe' 1 '1ère circonscription'	4	37	'M'	'NABAJOTH'	'Alix'	datetime.datetime(1973, 11, 11, 0, 0) 'DVG'	'Cadre de la fonction publique'	'Non'	'F'	'BARTEBIN-SOURHOU'	'Huguette'	datetime.datetime(1971, 12, 3, 0, 0)	'Non'")
        
        self.assertEqual(971, model.department.number)
        self.assertEqual("Guadeloupe", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("NABAJOTH", model.candidate_last_name)
        self.assertEqual("Alix", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVG",model.candidate_party)
        self.assertEqual("Cadre de la fonction publique", model.candidate_job)
        self.assertEqual("11/11/1973",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_martinique(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZB' 'Martinique' 1 '1ère circonscription' 1	2	'M'	'TABAR'	'Jonathan'	datetime.datetime(1987,10, 11, 0, 0) 'DVD'	'Employé civil et agent de service de la fonction publique'	'Non'	'F'	'JOSEPH'	'Joannifer' datetime.datetime(1996,12,11) 'Non'")
        
        self.assertEqual(972, model.department.number)
        self.assertEqual("Martinique", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("TABAR", model.candidate_last_name)
        self.assertEqual("Jonathan", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVD",model.candidate_party)
        self.assertEqual("Employé civil et agent de service de la fonction publique", model.candidate_job)
        self.assertEqual("10/11/1987",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_guyane(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZC' 'Guyane' 1	'1ère circonscription'	11	7 'M' 'MADÈRE' 'Christophe' datetime.datetime(1971,07,18) 'DVG'	'Professeur, profession scientifique'	'Non'	'F'	'BRIQUET'	'Ruth'	datetime.datetime(1993,05,06) 'Non'")
        
        self.assertEqual(973, model.department.number)
        self.assertEqual("Guyane", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("MADÈRE", model.candidate_last_name)
        self.assertEqual("Christophe", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVG",model.candidate_party)
        self.assertEqual("Professeur, profession scientifique", model.candidate_job)
        self.assertEqual("07/18/1971",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
 

    def test_creator_candidate_data_factory_reunion(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZD' 'La Réunion' 1 '1ère circonscription' 2	9 'F' 'SISTERON' 'Murielle'	datetime.datetime(1987,02,16) 'LR'	'Profession libérale' 'Non'	'M'	'SERVIABLE'	'Mario'	datetime.datetime(1949,05,23) 'Non'")
        
        self.assertEqual(974, model.department.number)
        self.assertEqual("La Réunion", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("SISTERON", model.candidate_last_name)
        self.assertEqual("Murielle", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("LR",model.candidate_party)
        self.assertEqual("Profession libérale", model.candidate_job)
        self.assertEqual("02/16/1987",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_mayotte(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZM' 'Mayotte'	1 '1ère circonscription'	2	21	'F'	'AOUNY'	'Yasmina'	datetime.datetime(1986,03,31) 'DVG'	'Professeur, profession scientifique'	'Non'	'M'	'BACAR'	'Assoumani'	datetime.datetime(1971,04,01) 'Non'")
        
        self.assertEqual(976, model.department.number)
        self.assertEqual("Mayotte", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("AOUNY", model.candidate_last_name)
        self.assertEqual("Yasmina", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("DVG",model.candidate_party)
        self.assertEqual("Professeur, profession scientifique", model.candidate_job)
        self.assertEqual("03/31/1986",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_nouvelle_caledonie(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZN' 'Nouvelle-Calédonie'	1 '1ère circonscription'	1	2	'M'	'GIL' 'Antoine'	datetime.datetime(1956,05,26) 'DVD'	'Policier et militaire'	'Non'	'M'	'QUINET' 'Stéphane'	datetime.datetime(1965,25,12) 'Non'")
        
        self.assertEqual(988, model.department.number)
        self.assertEqual("Nouvelle-Calédonie", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("GIL", model.candidate_last_name)
        self.assertEqual("Antoine", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVD",model.candidate_party)
        self.assertEqual("Policier et militaire", model.candidate_job)
        self.assertEqual("05/26/1956",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_polynesie_francaise(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZP' 'Polynésie française'	1 '1ère circonscription'	1	15	'F'	'HAITI'	'Pascale' datetime.datetime(1972,04,03) 'DVD' 'Profession libérale'	'Non' 'F'	'NOUVEAU' 'Lydia'	datetime.datetime(1959,27,02) 'Non'")
        
        self.assertEqual(987, model.department.number)
        self.assertEqual("Polynésie française", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("HAITI", model.candidate_last_name)
        self.assertEqual("Pascale", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("DVD",model.candidate_party)
        self.assertEqual("Profession libérale", model.candidate_job)
        self.assertEqual("04/03/1972",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_saint_pierre_et_miquelon(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZS' 'Saint-Pierre-et-Miquelon'	1 '1ère circonscription'	3	3 'M'	'GASTON' 'Olivier'	datetime.datetime(1981,06,30) 'DVG'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'HELENE' 'Catherine'	datetime.datetime(1970,03,27) 'Non'")
        
        self.assertEqual(975, model.department.number)
        self.assertEqual("Saint-Pierre-et-Miquelon", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("GASTON", model.candidate_last_name)
        self.assertEqual("Olivier", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVG",model.candidate_party)
        self.assertEqual("Cadre administratif et commercial d'entreprise", model.candidate_job)
        self.assertEqual("06/30/1981",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_wallis_et_futuna(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZW' 'Wallis et Futuna'	1	'1ère circonscription'	3	7	'F'	'UGATAI' 'Sandrine' 'Aimée'	datetime.datetime(1976,06,23) 'DVC' 'Cadre administratif et commercial d'entreprise'	'Non' 'F' 'TAUVALE ÉPOUSE HANISI' 'Akata'	datetime.datetime(1976,03,27) 'Non'")
        
        self.assertEqual(986, model.department.number)
        self.assertEqual("Wallis et Futuna", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("UGATAI", model.candidate_last_name)
        self.assertEqual("Sandrine Aimée", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("DVC",model.candidate_party)
        self.assertEqual("Cadre administratif et commercial d'entreprise", model.candidate_job)
        self.assertEqual("06/23/1976",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_saint_martin_saint_barthelemy(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZX' 'Saint-Martin/Saint-Barthélemy' 1 '1ère circonscription'	2	3	'M'	'GIBBS'	'Daniel'	datetime.datetime(1968,08,01)	'DVD'	'Profession libérale'	'Non'	'M'	'GREAUX'	'Thomas'	datetime.datetime(1991,27,08)	'Non'")
        
        self.assertEqual(978, model.department.number)
        self.assertEqual("Saint-Martin/Saint-Barthélemy", model.department.name)
        self.assertEqual(1, model.district_number)
        self.assertEqual("1ère circonscription", model.district_name)
        self.assertEqual("GIBBS", model.candidate_last_name)
        self.assertEqual("Daniel", model.candidate_first_name)
        self.assertEqual("M", model.candidate_sexe)
        self.assertEqual("DVD",model.candidate_party)
        self.assertEqual("Profession libérale", model.candidate_job)
        self.assertEqual("08/01/1968",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
        
    def test_creator_candidate_data_factory_french_strangers(self):
        creator = CreatorCandidateData()
        
        model = creator.factory_method("['ZZ' 'Français établis hors de France' 4	'4ème circonscription'	5	64	'F'	'GONDARD' 'Cécilia'	datetime.datetime(1980,06,04) 'NUP'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'LIBEAUT'	'Catherine'	datetime.datetime(1963,09,26) 'Non'")
        
        self.assertEqual(99, model.department.number)
        self.assertEqual("Français établis hors de France", model.department.name)
        self.assertEqual(4, model.district_number)
        self.assertEqual("4ème circonscription", model.district_name)
        self.assertEqual("GONDARD", model.candidate_last_name)
        self.assertEqual("Cécilia", model.candidate_first_name)
        self.assertEqual("F", model.candidate_sexe)
        self.assertEqual("NUP",model.candidate_party)
        self.assertEqual("Cadre administratif et commercial d'entreprise", model.candidate_job)
        self.assertEqual("06/04/1980",model.candidate_birth_date)
        self.assertEqual(False, model.candidate_is_sorting)
        
    #fin import


    if __name__ == "__main__":
        unittest.main()