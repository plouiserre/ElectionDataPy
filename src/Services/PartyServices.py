#TODO quand ca fonctonnera faire un test de partyservices

class PartyServices : 
    def __init__(self ):
        pass
    
    def load_parties(self,PartyRepository) : 
        self.party_repository = PartyRepository
        parties = self.party_repository.get_all_parties()
        return parties