from src.Models.PartyModel import PartyModel

class CreatorParty() : 
    def factory_method(self, election_data):
        party = PartyModel()
        party.id = election_data[0]
        party.name = election_data[1]
        party.short_name = election_data[2]
        return party