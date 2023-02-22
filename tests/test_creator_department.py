import unittest
from src.Factory.CreatorDepartment import CreatorDepartment
         
class CreatorDepartmentTest(unittest.TestCase):
    def test_creator_department_gironde(self) : 
        creator = CreatorDepartment()
        candidate_data = ['33','Gironde','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(33, department.number)
        self.assertEqual("Gironde", department.name)
        
    def test_creator_department_corsica(self) : 
        creator = CreatorDepartment()
        candidate_data =['2A','Corse-du-Sud','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(20, department.number)
        self.assertEqual("Corse", department.name)
        
    def test_creator_department_guadeloupe(self) : 
        creator = CreatorDepartment()        
        candidate_data = ['ZA','Guadeloupe','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(971, department.number)
        self.assertEqual("Guadeloupe", department.name)
        
    def test_creator_department_martinique(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZB','Martinique','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(972, department.number)
        self.assertEqual("Martinique", department.name)
        
    def test_creator_department_guyane(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZC','Guyane','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(973, department.number)
        self.assertEqual("Guyane", department.name)
        
    def test_creator_department_la_reunion(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZD','La Réunion','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(974, department.number)
        self.assertEqual("La Réunion", department.name)
        
    def test_creator_department_mayotte(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZM','Mayotte','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(976, department.number)
        self.assertEqual("Mayotte", department.name)
        
    def test_creator_department_nouvelle_caledonie(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZN','Nouvelle-Calédonie','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(988, department.number)
        self.assertEqual("Nouvelle-Calédonie", department.name)
        
    def test_creator_department_polynesie_francaise(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZP','Polynésie française','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(987, department.number)
        self.assertEqual("Polynésie française", department.name)

    def test_creator_department_saint_pierre_et_miquelon(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZS','Saint-Pierre-et-Miquelon','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(975, department.number)
        self.assertEqual("Saint-Pierre-et-Miquelon", department.name)
        
    def test_creator_department_wallis_et_futuna(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZW','Wallis et Futuna','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(986, department.number)
        self.assertEqual("Wallis et Futuna", department.name)
        
    def test_creator_department_saint_martin_saint_barthelemy(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZX','Saint-Martin/Saint-Barthélemy','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(978, department.number)
        self.assertEqual("Saint-Martin/Saint-Barthélemy", department.name)
        
    def test_creator_department_hors_de_france(self) : 
        creator = CreatorDepartment()
        candidate_data = ['ZZ','Français établis hors de France','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX']
        
        department = creator.factory_method(candidate_data)
        
        self.assertEqual(99, department.number)
        self.assertEqual("Français établis hors de France", department.name)

        
    if __name__ == "__main__":
        unittest.main()