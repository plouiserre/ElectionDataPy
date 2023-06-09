import unittest
import pandas as pd
from mock import Mock
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager

class ExcelManagerTest(unittest.TestCase) :
    
    def getSimpleCandidatesDataFrame(*args) : 
        frame = pd.DataFrame({'Code département':['01', '02', '03'],'Libellé du département':['Ain', 'Aisne','Allier'],'Code circonscription':[1,2,3],'Nom Candidat':['MAISONNETTE','BEAURAIN','GUILLAUMIN'],'Prénom Candidat':['Cécile','Eric','Jean-Marie']})
        return frame
    
    @patch.object(pd,'read_excel', side_effect=getSimpleCandidatesDataFrame)
    def test_import_candidates_datas_simple_datas(self, mock_panda):
        excel_manager = ExcelManager()
        
        candidates = excel_manager.import_elections_datas(pd)
        
        self.assertEqual(3,len(candidates))
        self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        self.assertEqual(candidates[2],"['03' 'Allier' 3 'GUILLAUMIN' 'Jean-Marie']")
        

    def getComplexesCandidatesDataFrame(*args) : 
        frame = pd.DataFrame({'Code département':['01', '02', '21'],'Libellé du département':['Ain', 'Aisne','Côte d\'Or'],'Code circonscription':[1,2,3],'Nom Candidat':['MAISONNETTE','BEAURAIN','GUILLAUMIN'],'Prénom Candidat':['Cécile','Eric','Jean-Marie']})
        return frame    
        
    @patch.object(pd,'read_excel', side_effect=getComplexesCandidatesDataFrame)
    def test_import_candidates_datas_complexe_datas(self, mock_panda):
        excel_manager = ExcelManager()
        
        candidates = excel_manager.import_elections_datas(pd)
        
        self.assertEqual(3,len(candidates))
        self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        self.assertEqual(candidates[2],"['21' 'Côte d\'Or' 3 'GUILLAUMIN' 'Jean-Marie']") 


    def getSimpleFirstRoundDataFrame(*args) : 
        frame = pd.DataFrame({'Libellé du département':['Ain', 'Aisne','Allier'],'Code circonscription':[1,2,3],'Etat saisie':['Complet','Complet','Complet'],'Inscrits':[86187,99953,82204],'Abstentions':[43652,50270,45946],'% Abs/Ins':[50.65,50.29,55.89],'Votants':[42535,49683,36258]})
        return frame    
    
    @patch.object(pd,'read_excel', side_effect=getSimpleFirstRoundDataFrame)
    def test_import_first_round_results_datas(self, mock_panda):       
        excel_manager = ExcelManager()
        
        results = excel_manager.import_first_round_results_datas(pd)
        
        self.assertTrue(pd.read_excel.called)    
        self.assertEqual(3,len(results))
        self.assertEqual(results[0],"['Ain' 1 'Complet' 86187 43652 '50.65' 42535]")
        self.assertEqual(results[1],"['Aisne' 2 'Complet' 99953 50270 '50.29' 49683]")
        self.assertEqual(results[2],"['Allier' 3 'Complet' 82204 45946 '55.89' 36258]") 
        
        
    if __name__ == "__main__":
        unittest.main()