import unittest

from src.Factory.CreatorFirstRoundData import CreatorFirstRoundData

#TODO complete unit test
#TODO factorize
class CreatorFirstRoundDataTest(unittest.TestCase) : 
    def test_creator_first_round_data_first_line(self):
        creator = CreatorFirstRoundData()
            
        first_round_data = creator.factory_method("['01' 'Ain' 1 '1ère circonscription' 'Complet' 86187 43652 '50.65' 42535 '49.35' 490 '0.57' '1.15' 234 '0.27' '0.55' 41811 '48.51' '98.3' 2 'M' 'LAHY' 'Éric' 'DXG' 391 '0.45' '0.94' 'nan' 8 'M' 'GUÉRAUD' 'Sébastien' 'NUP' 9982 '11.58' '23.87' 'nan' 7 'F' 'ARMENJON' 'Eliane' 'ECO' 1161 '1.35' '2.78' 'nan' 1 'M' 'GUILLERMIN' 'Vincent' 'ENS' 8071 '9.36' '19.3' 'nan' '3.0' 'M' 'BRETON' 'Xavier' 'LR' '10599.0' '12.3' '25.35' 'nan' '5.0' 'M' 'MENDES' 'Michael' 'DSV' '641.0' '0.74' '1.53' 'nan' '6.0' 'M' 'BELLON' 'Julien' 'REC' '1995.0' '2.31' '4.77' 'nan' '4.0' 'F' 'PIROUX GIANNOTTI' 'Brigitte' 'RN' '8971.0' '10.41' '21.46' 'nan' 'nan']")
            
        self.assertTrue(first_round_data.department != None)
        self.assertEqual(1, first_round_data.department.number)
        self.assertEqual('Ain', first_round_data.department.name)
        self.assertTrue(first_round_data.district != None)
        self.assertEqual(1, first_round_data.district.number)
        self.assertEqual('1ère circonscription', first_round_data.district.name)
        self.assertEqual('Complet', first_round_data.election.state_compute)
        self.assertEqual(86187, first_round_data.election.registered)
        self.assertEqual(43652, first_round_data.election.abstaining)
        self.assertEqual(50.65, first_round_data.election.rate_abstaining)
        self.assertEqual(42535, first_round_data.election.voting)
        self.assertEqual(49.35, first_round_data.election.rate_voting)  
        self.assertEqual(490, first_round_data.election.blank_balot)    
        self.assertEqual(0.57, first_round_data.election.rate_blank_registered)   
        self.assertEqual(1.15, first_round_data.election.rate_blank_voting)       
        self.assertEqual(234, first_round_data.election.null_ballot)  
        self.assertEqual(0.27, first_round_data.election.rate_null_registered)  
        self.assertEqual(0.55, first_round_data.election.rate_null_voting)  
        self.assertEqual(41811, first_round_data.election.expressed)  
        self.assertEqual(48.51, first_round_data.election.rate_express_registered)  
        self.assertEqual(98.3, first_round_data.election.rate_express_voting)  
        
        
    def test_creator_first_round_data_one_hundred_and_first_line(self):
        creator = CreatorFirstRoundData()
            
        first_round_data = creator.factory_method("['25' 'Doubs' 2 '2ème circonscription' 'Complet' 79162 37688 '47.61' 41474 '52.39' 821 '1.04' '1.98' 326 '0.41' '0.79' 40327 '50.94' '97.23' 8 'F' 'VUITTON' 'Brigitte' 'DXG' 779 '0.98' '1.93' 'nan' 2 'M' 'RAVACLEY' 'Stéphane' 'NUP' 13112 '16.56' '32.51' 'nan' 6 'M' 'THOMASSIN' 'Geoffrey' 'DIV' 216 '0.27' '0.54' 'nan' 4 'F' 'MEYER' 'Claudine' 'REG' 0 '0.0' '0.0' 'nan' '3.0' 'M' 'ALAUZET' 'Eric' 'ENS' '12647.0' '15.98' '31.36' 'nan' '1.0' 'F' 'KAOULAL' 'Chafia' 'LR' '4354.0' '5.5' '10.8' 'nan' '7.0' 'M' 'PRENEL' 'Jim' 'DSV' '692.0' '0.87' '1.72' 'nan' '5.0' 'F' 'CARRAU' 'Barbara' 'REC' '1472.0' '1.86' '3.65' 'nan' '9.0' 'M' 'FUSIS' 'Eric' 'RN' '7055.0' '8.91' '17.49' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")
            
        self.assertTrue(first_round_data.department != None)
        self.assertEqual(25, first_round_data.department.number)
        self.assertEqual('Doubs', first_round_data.department.name)
        self.assertTrue(first_round_data.district != None)
        self.assertEqual(2, first_round_data.district.number)
        self.assertEqual('2ème circonscription', first_round_data.district.name)
        self.assertEqual('Complet', first_round_data.election.state_compute)
        self.assertEqual(79162, first_round_data.election.registered)
        self.assertEqual(37688, first_round_data.election.abstaining)
        self.assertEqual(47.61, first_round_data.election.rate_abstaining)
        self.assertEqual(41474, first_round_data.election.voting)
        self.assertEqual(52.39, first_round_data.election.rate_voting)  
        self.assertEqual(821, first_round_data.election.blank_balot)    
        self.assertEqual(1.04, first_round_data.election.rate_blank_registered)   
        self.assertEqual(1.98, first_round_data.election.rate_blank_voting)       
        self.assertEqual(326, first_round_data.election.null_ballot)  
        self.assertEqual(0.41, first_round_data.election.rate_null_registered)  
        self.assertEqual(0.79, first_round_data.election.rate_null_voting)  
        self.assertEqual(40327, first_round_data.election.expressed)  
        self.assertEqual(50.94, first_round_data.election.rate_express_registered)  
        self.assertEqual(97.23, first_round_data.election.rate_express_voting)  