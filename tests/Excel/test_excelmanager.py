import unittest
import pandas as pd
from unittest.mock import patch

from src.Excel.ExcelManager import ExcelManager

class ExcelManagerTest(unittest.TestCase) :
    
    def getSimpleCandidatesDataFrame(*args) : 
        frame = pd.DataFrame({'Code département':['01', '02', '03'],'Libellé du département':['Ain', 'Aisne','Allier'],'Code circonscription':[1,2,3],'Nom Candidat':['MAISONNETTE','BEAURAIN','GUILLAUMIN'],'Prénom Candidat':['Cécile','Eric','Jean-Marie']})
        return frame
    
    @patch.object(pd,'read_excel', side_effect=getSimpleCandidatesDataFrame)
    def test_import_candidates_datas_simple_datas(self, mock_panda):
        excel_manager = ExcelManager()
        
        candidates = excel_manager.import_candidates_datas(pd)
        
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
        
        candidates = excel_manager.import_candidates_datas(pd)
        
        self.assertEqual(3,len(candidates))
        self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        self.assertEqual(candidates[2],"['21' 'Côte d\'Or' 3 'GUILLAUMIN' 'Jean-Marie']")
 

        
    
    def getSimpleResultFrame(*args) : 
        frame = pd.DataFrame({'Sexe':['M', 'M', 'F'],'Prénom':['Éric', 'Vincent','Cécile'],'Nuance':['DXG','DXG','DXG'],'Voix':[391,415,281],'% Voix/Ins':[0.45,0.42,0.34],'% Voix/Exp':[0.94,0.85,0.79],'% Sièges':['','',''],'':[8,1,6],'':['M','F','M'],'':['GUÉRAUD','LAPRAY','JOLIE'],'':['Sébastien','Lumir','Christian'],'':['NUP','NUP','NUP'],'':[9982,12428,7990],'':[11.58,12.43,9.72],'':[23.87,25.42,22.36]})
        return frame
        
    # @patch.object(pd,'read_excel', side_effect=getSimpleResultFrame)
    # def test_import_candidates_datas_complexe_datas(self, mock_panda):
    #     excel_manager = ExcelManager()
        
    #     results = excel_manager.extracts_datas_from_files(pd)
        
    #     self.assertEqual(3,len(results))
        # self.assertEqual(candidates[0],"['01' 'Ain' 1 'MAISONNETTE' 'Cécile']")
        # self.assertEqual(candidates[1],"['02' 'Aisne' 2 'BEAURAIN' 'Eric']")
        # self.assertEqual(candidates[2],"['21' 'Côte d\'Or' 3 'GUILLAUMIN' 'Jean-Marie']")   
    
        
        
    if __name__ == "__main__":
        unittest.main()