import unittest
from mock import Mock

from src.Factory.CreatorParty import CreatorParty

class CreatorPartyTest(unittest.TestCase) : 
    def test_creator_divers_party(self) : 
        creator = CreatorParty()
        
        rows = [6, "Divers", "DIV"]
        
        party = creator.factory_method(rows)
        
        self.assertEqual(6, party.id)
        self.assertEqual("Divers", party.name)
        self.assertEqual("DIV", party.short_name)