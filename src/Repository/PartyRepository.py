from src.Factory.CreatorParty import CreatorParty

class PartyRepository : 
    def __init__(self, mydb):
        self.mydb = mydb
        
    def get_all_parties(self):
        mydb = self.mydb.get_my_db()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.PARTY")
        
        parties_bdd = mycursor.fetchall()
        parties = []
        
        for party_bdd in parties_bdd : 
            creator_party = CreatorParty()
            party = creator_party.factory_method(party_bdd)
            parties.append(party)
        
        return parties
        