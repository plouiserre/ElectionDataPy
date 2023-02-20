import unittest
import pandas as pd
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager

class ExcelManagerTest(unittest.TestCase) :
    
    def getSimpleDataFrame(*args) : 
        frame = pd.DataFrame({'Code département':['01', '02', '03'],'Libellé du département':['Ain', 'Aisne','Allier'],'Code circonscription':[1,2,3],'Nom Candidat':['MAISONNETTE','BEAURAIN','GUILLAUMIN'],'Prénom Candidat':['Cécile','Eric','Jean-Marie']})
        return frame
    
    @patch.object(pd,'read_excel', side_effect=getSimpleDataFrame)
    def test_import_candidates_datas_simple_datas(self, mock_panda):
        excel_manager = ExcelManager()
        
        candidates = excel_manager.import_candidates_datas(pd)
        
        self.assertEqual(3,len(candidates))
        self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        self.assertEqual(candidates[2],"['03' 'Allier' 3 'GUILLAUMIN' 'Jean-Marie']")
        

    def getComplexesDataFrame(*args) : 
        frame = pd.DataFrame({'Code département':['01', '02', '21'],'Libellé du département':['Ain', 'Aisne','Côte d\'Or'],'Code circonscription':[1,2,3],'Nom Candidat':['MAISONNETTE','BEAURAIN','GUILLAUMIN'],'Prénom Candidat':['Cécile','Eric','Jean-Marie']})
        return frame
        
    @patch.object(pd,'read_excel', side_effect=getComplexesDataFrame)
    def test_import_candidates_datas_complexe_datas(self, mock_panda):
        excel_manager = ExcelManager()
        
        candidates = excel_manager.import_candidates_datas(pd)
        
        self.assertEqual(3,len(candidates))
        self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        self.assertEqual(candidates[2],"['21' 'Côte d\'Or' 3 'GUILLAUMIN' 'Jean-Marie']")
        
        #'[\'21\' "Côte-d\'Or" 4 \'4ème circonscription\' 9 15 \'M\' \'GUINOT\' \'Stéphane\'\n Timestamp(\'1981-05-02 00:00:00\') \'NUP\'\n \'Professeur des écoles, instituteur et assimilé\' \'Non\' \'F\' \'JACQ\'\n \'Valérie\' Timestamp(\'1972-10-30 00:00:00\') \'Non\']'
        
        
    if __name__ == "__main__":
        unittest.main()