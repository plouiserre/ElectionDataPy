import unittest
from src.Models.department_model import DepartmentModel

class DepartmentModelTest(unittest.TestCase):

    def test_to_department_model_first_line(self) :
        model = DepartmentModel()
        
        model.to_department_model("['01' 'Ain' '05' '5ème circonscription' 8 11 'F' 'CROZET' 'Sylvie' datetime.datetime(1962, 6, 3, 0, 0) 'DXG' 'Profession intermédiaire de la santé et du travail social' 'Non' 'M' 'BOUVET' 'Didier' datetime.datetime(1963, 5, 26, 0, 0) 'Non']")
        
        self.assertEqual(1, model.id)
        self.assertEqual("Ain", model.name)
        
        
    def test_to_department_model_second_line(self):
        model = DepartmentModel()
        
        model.to_department_model("['02' 'Aisne' '02' '2ème circonscription' 6 24 'M' 'LEPEUPLE' 'Eric'\n datetime.datetime(1971, 11, 5, 0, 0) 'DIV' 'Commerçant et assimilé' 'Non'\n 'F' 'MAZOUR' 'Vanessa' datetime.datetime(1980, 3, 15, 0, 0) 'Non']")
        
        self.assertEqual(2, model.id)
        self.assertEqual("Aisne", model.name)

    if __name__ == "__main__":
        unittest.main()