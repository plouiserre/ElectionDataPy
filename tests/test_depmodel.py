import unittest
from src.Models.DepartmentModel import DepartmentModel

class DepartmentModelTest(unittest.TestCase):

    def test_to_department_model_first_line(self) :
        model = DepartmentModel()
        
        model.to_department_model("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']")
     
        self.assertEqual(1, model.number)
        self.assertEqual("Ain", model.name)
        
        
    def test_to_department_model_second_line(self):
        model = DepartmentModel()
        
        model.to_department_model("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n datetime.datetime(1971, 11, 5, 0, 0) 'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' datetime.datetime(1980, 3, 15, 0, 0) 'Non']")
        
        self.assertEqual(2, model.number)
        self.assertEqual("Aisne", model.name)
        
        
    def test_to_deparment_model_territoires_de_belfort(self):
        model = DepartmentModel()
        model.to_department_model("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' datetime.datetime(1993, 4, 16, 0, 0) 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' datetime.datetime(1986, 11, 14, 0, 0)\n 'Non']")
        
        self.assertEqual(90, model.number)
        self.assertEqual("Territoire de Belfort", model.name)
        
        
    def test_to_department_model_cotes_d_or(self) : 
        model = DepartmentModel()
        model.to_department_model("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n datetime.datetime(1956, 8, 20, 0, 0) 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' datetime.datetime(1972, 9, 29, 0, 0) 'Non']")

        self.assertEqual(21, model.number)        
        self.assertEqual("Côte-d'Or", model.name)
        
        
    def test_to_department_model_corsica(self):
        model = DepartmentModel()
        
        model.to_department_model("['2A' 'Corse-du-Sud'	1 '1ère circonscription'	2	15	'M'	'LIPPLER'	'Walter'	datetime.datetime(1961, 02, 5, 0, 0) 'DSV'	'Cadre de la fonction publique'	'Non'	'M'	'GOUILLON'	'Sylvain'	datetime.datetime(1960,8 ,8, 0, 0)	'Non'")
        
        self.assertEqual(20, model.number)
        self.assertEqual("Corse", model.name)
        
        
    def test_to_department_model_guadeloupe(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZA' 'Guadeloupe' 1 '1ère circonscription'	4	37	'M'	'NABAJOTH'	'Alix'	datetime.datetime(1973, 11, 11, 0, 0) 'DVG'	'Cadre de la fonction publique'	'Non'	'F'	'BARTEBIN-SOURHOU'	'Huguette'	datetime.datetime(1971, 12, 3, 0, 0)	'Non'")
        
        self.assertEqual(971, model.number)
        self.assertEqual("Guadeloupe", model.name)
        
        
    def test_to_department_model_martinique(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZB' 'Martinique' 1 '1ère circonscription' 1	2	'M'	'TABAR'	'Jonathan'	datetime.datetime(1987,10, 11, 0, 0) 'DVD'	'Employé civil et agent de service de la fonction publique'	'Non'	'F'	'JOSEPH'	'Joannifer' datetime.datetime(1996,12,11) 'Non'")
        
        self.assertEqual(972, model.number)
        self.assertEqual("Martinique", model.name)
        
        
    def test_to_department_model_guyane(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZC' 'Guyane' 1	'1ère circonscription'	11	7 'M' 'MADÈRE' 'Christophe' datetime.datetime(1971,07,18) 'DVG'	'Professeur, profession scientifique'	'Non'	'F'	'BRIQUET'	'Ruth'	datetime.datetime(1993,05,06) 'Non'")
        
        self.assertEqual(973, model.number)
        self.assertEqual("Guyane", model.name)
 

    def test_to_department_model_reunion(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZD' 'La Réunion' 1 '1ère circonscription' 2	9 'F' 'SISTERON' 'Murielle'	datetime.datetime(1987,02,16) 'LR'	'Profession libérale' 'Non'	'M'	'SERVIABLE'	'Mario'	datetime.datetime(1949,05,23) 'Non'")
        
        self.assertEqual(974, model.number)
        self.assertEqual("La Réunion", model.name)
        
        
    def test_to_department_model_mayotte(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZM' 'Mayotte'	1 '1ère circonscription'	2	21	'F'	'AOUNY'	'Yasmina'	datetime.datetime(1986,03,31) 'DVG'	'Professeur, profession scientifique'	'Non'	'M'	'BACAR'	'Assoumani'	datetime.datetime(1971,04,01) 'Non'")
        
        self.assertEqual(976, model.number)
        self.assertEqual("Mayotte", model.name)
        
        
    def test_to_department_model_nouvelle_caledonie(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZN' 'Nouvelle-Calédonie'	1 '1ère circonscription'	1	2	'M'	'GIL' 'Antoine'	datetime.datetime(1956,26,05) 'DVD'	'Policier et militaire'	'Non'	'M'	'QUINET' 'Stéphane'	datetime.datetime(1965,25,12) 'Non'")
        
        self.assertEqual(988, model.number)
        self.assertEqual("Nouvelle-Calédonie", model.name)
        
        
    def test_to_department_model_polynesie_francaise(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZP' 'Polynésie française'	1 '1ère circonscription'	1	15	'F'	'HAITI'	'Pascale' datetime.datetime(1972,04,03) 'DVD' 'Profession libérale'	'Non' 'F'	'NOUVEAU' 'Lydia'	datetime.datetime(1959,27,02) 'Non'")
        
        self.assertEqual(987, model.number)
        self.assertEqual("Polynésie française", model.name)
        
        
    def test_to_department_model_saint_pierre_et_miquelon(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZS' 'Saint-Pierre-et-Miquelon'	1 'Saint-Pierre-et-Miquelon'	3	3 'M'	'GASTON' 'Olivier'	datetime.datetime(1981,06,30) 'DVG'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'HELENE' 'Catherine'	datetime.datetime(1970,03,27) 'Non'")
        
        self.assertEqual(975, model.number)
        self.assertEqual("Saint-Pierre-et-Miquelon", model.name)
        
        
    def test_to_department_model_wallis_et_futuna(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZW' 'Wallis et Futuna'	1	'1ère circonscription'	3	7	'F'	'UGATAI' 'Sandrine' 'Aimée'	datetime.datetime(1976,06,23) 'DVC' 'Cadre administratif et commercial d'entreprise'	'Non' 'F' 'TAUVALE ÉPOUSE HANISI' 'Akata'	datetime.datetime(1976,03,27) 'Non'")
        
        self.assertEqual(986, model.number)
        self.assertEqual("Wallis et Futuna", model.name)
        
        
    def test_to_department_model_saint_martin_saint_barthelemy(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZX' 'Saint-Martin/Saint-Barthélemy' 1 '1ère circonscription'	2	3	'M'	'GIBBS'	'Daniel'	datetime.datetime(1968,08,01)	'DVD'	'Profession libérale'	'Non'	'M'	'GREAUX'	'Thomas'	datetime.datetime(1991,27,08)	'Non'")
        
        self.assertEqual(978, model.number)
        self.assertEqual("Saint-Martin/Saint-Barthélemy", model.name)
        
        
    def test_to_department_model_french_strangers(self):
        model = DepartmentModel()
        
        model.to_department_model("['ZZ' 'Français établis hors de France' 4	'4ème circonscription'	5	64	'F'	'GONDARD' 'Cécilia'	datetime.datetime(1980,06,04) 'NUP'	'Cadre administratif et commercial d'entreprise' 'Non'	'F'	'LIBEAUT'	'Catherine'	datetime.datetime(1963,09,26) 'Non'")
        
        self.assertEqual(99, model.number)
        self.assertEqual("Français établis hors de France", model.name)


    if __name__ == "__main__":
        unittest.main()