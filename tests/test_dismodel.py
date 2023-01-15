import unittest

from src.Models.DistrictModel import DistrictModel

class DistrictModelTest(unittest.TestCase):
    
    def test_to_district_model_first_line(self) :
        model = DistrictModel()
        
        model.to_district_model("['01' 'Ain' '05' '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']", 66)
        
        self.assertEqual(5, model.number)
        self.assertEqual("5ème circonscription", model.name)
        self.assertEqual(66, model.department_id)
        
        
    def test_to_district_model_second_line(self):
        model = DistrictModel()
        
        model.to_district_model("['02' 'Aisne' '02' '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n datetime.datetime(1971, 11, 5, 0, 0) 'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' datetime.datetime(1980, 3, 15, 0, 0) 'Non']", 67)
        
        self.assertEqual(2, model.number)
        self.assertEqual("2ème circonscription", model.name)
        self.assertEqual(67, model.department_id)
        
        
    def test_to_district_with_department_name_space(self) : 
        model = DistrictModel()
        
        model.to_district_model("['90' 'Territoire de Belfort' '01' '1ère circonscription' 1 12 'M'\n 'GRUDLER' 'Thiebaud' datetime.datetime(1993, 4, 16, 0, 0) 'ENS'\n 'Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)'\n 'Non' 'F' 'GROSDIDIER' 'Maggy' datetime.datetime(1986, 11, 14, 0, 0)\n 'Non']", 90)
        
        self.assertEqual(1, model.number)
        self.assertEqual("1ère circonscription", model.name)
        self.assertEqual(90, model.department_id)
        
        
    def test_to_district_with_department_name_apostrophe(self) : 
        model = DistrictModel()
        
        model.to_district_model('[\'21\' "Côte-d\'Or" \'01\' \'1ère circonscription\' 1 34 \'M\' \'MARTIN\' \'Didier\'\n datetime.datetime(1956, 8, 20, 0, 0) \'ENS\'\n \'Profession intermédiaire de la santé et du travail social\' \'Oui\' \'F\'\n \'REFAIT-ALEXANDRE\' \'Catherine\' datetime.datetime(1972, 9, 29, 0, 0) \'Non\']', 21)
        
        self.assertEqual(1, model.number)
        self.assertEqual("1ère circonscription", model.name)
        self.assertEqual(21, model.department_id)