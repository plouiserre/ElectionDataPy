import unittest

from src.Factory.CreatorCandidates import CreatorCandidates

class CreatorCandidatesTest(unittest.TestCase) : 
    
    #TODO factorize this assertpart
    def test_creator_candidates_from_first_round_data_excel_first_line(self) : 
        creator = CreatorCandidates()
        candidates_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX',4,'M', 'LAHY', 'Éric', 'DXG', 391, '0.45', '0.94', 'nan', 8, 'F', 'ARMENJON', 'Eliane', 'ECO', 1161, '1.35', '2.78', 'nan', 'nan', 'nan']
        
        candidates = creator.factory_method(candidates_data)
        
        self.assertEqual(2, len(candidates))
        self.assertEqual('M', candidates[0].sexe)
        self.assertEqual('LAHY', candidates[0].last_name)        
        self.assertEqual('Éric', candidates[0].first_name)
        self.assertEqual(391, candidates[0].vote)
        self.assertEqual(0.45, candidates[0].rate_vote_registered)
        self.assertEqual(0.94, candidates[0].rate_vote_expressed)
        self.assertEqual('F', candidates[1].sexe)
        self.assertEqual('ARMENJON', candidates[1].last_name)        
        self.assertEqual('Eliane', candidates[1].first_name)
        self.assertEqual(1161, candidates[1].vote)
        self.assertEqual(1.35, candidates[1].rate_vote_registered)
        self.assertEqual(2.78, candidates[1].rate_vote_expressed)
        
  
    def test_creator_candidates_from_first_round_data_excel_second_line(self) : 
        creator = CreatorCandidates()
        candidates_data = ['XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX','XXXXX',3,'F', 'VUITTON', 'Brigitte', 'DXG', 779, '0.98', '1.93', 'nan', 2, 'M', 'RAVACLEY', 'Stéphane', 'NUP', 13112, '16.56', '32.51', 'nan', 6, 'M', 'THOMASSIN', 'Geoffrey', 'DIV', 216, '0.27', '0.54', 'nan', 4, 'F', 'MEYER', 'Claudine', 'REG', 0, '0.0', '0.0', 'nan', 'nan']
         
        candidates = creator.factory_method(candidates_data)
        
        self.assertEqual(4, len(candidates))
        self.assertEqual('F', candidates[0].sexe)
        self.assertEqual('VUITTON', candidates[0].last_name)        
        self.assertEqual('Brigitte', candidates[0].first_name)
        self.assertEqual(779, candidates[0].vote)
        self.assertEqual(0.98, candidates[0].rate_vote_registered)
        self.assertEqual(1.93, candidates[0].rate_vote_expressed)
        self.assertEqual('M', candidates[1].sexe)
        self.assertEqual('RAVACLEY', candidates[1].last_name)        
        self.assertEqual('Stéphane', candidates[1].first_name)
        self.assertEqual(13112, candidates[1].vote)
        self.assertEqual(16.56, candidates[1].rate_vote_registered)
        self.assertEqual(32.51, candidates[1].rate_vote_expressed)
        self.assertEqual('M', candidates[2].sexe)
        self.assertEqual('THOMASSIN', candidates[2].last_name)        
        self.assertEqual('Geoffrey', candidates[2].first_name)
        self.assertEqual(216, candidates[2].vote)
        self.assertEqual(0.27, candidates[2].rate_vote_registered)
        self.assertEqual(0.54, candidates[2].rate_vote_expressed)
        self.assertEqual('F', candidates[3].sexe)
        self.assertEqual('MEYER', candidates[3].last_name)        
        self.assertEqual('Claudine', candidates[3].first_name)
        self.assertEqual(0, candidates[3].vote)
        self.assertEqual(0.0, candidates[3].rate_vote_registered)
        self.assertEqual(0.0, candidates[3].rate_vote_expressed)
        