import unittest
from src.Factory.CreatorDistrict import CreatorDistrict

class CreatorDistrictTest(unittest.TestCase):
    def test_creator_district_factory_first_line(self) :
        creator = CreatorDistrict()
        
        model = creator.factory_method("['01' 'Ain' 5 '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']")
                                
        self.assertEqual(5, model.number)
        self.assertEqual("5ème circonscription", model.name)
        
        
    def test_creator_district_factory_second_line(self):
        creator = CreatorDistrict()
        
        model = creator.factory_method("['02' 'Aisne' 2 '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n datetime.datetime(1971, 11, 5, 0, 0) 'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' datetime.datetime(1980, 3, 15, 0, 0) 'Non']")
        
        self.assertEqual(2, model.number)
        self.assertEqual("2ème circonscription", model.name)
        
        
    def test_creator_district_factory_with_department_name_space(self) : 
        creator = CreatorDistrict()
        
        model = creator.factory_method("['90' 'Territoire de Belfort' 1 '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' datetime.datetime(1993, 4, 16, 0, 0) 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' datetime.datetime(1986, 11, 14, 0, 0)\n 'Non']")
        
        self.assertEqual(1, model.number)
        self.assertEqual("1ère circonscription", model.name)
        
        
    def test_creator_district_factory_with_department_name_apostrophe(self) : 
        creator = CreatorDistrict()
        
        model = creator.factory_method("['21' 'Côte-d\'Or' 1 '1ère circonscription' 1 34 'M' 'MARTIN' 'Didier'\n datetime.datetime(1956, 8, 20, 0, 0) 'ENS'\n 'Profession intermédiaire de la santé et du travail social' 'Oui' 'F'\n 'REFAIT-ALEXANDRE' 'Catherine' datetime.datetime(1972, 9, 29, 0, 0) 'Non']")
        
        self.assertEqual(1, model.number)
        self.assertEqual("1ère circonscription", model.name)        