from src.Models.PartyModel import PartyModel
from src.Factory.Creator import Creator

class CreatorParty(Creator) : 
    def factory_method(self, candidate_data):
        party = PartyModel()
        party.id = candidate_data[0]
        party.name = candidate_data[1]
        party.short_name = candidate_data[2]
        return party