from src.Factory.CreatorCandidate import CreatorCandidate

class CreatorCandidateFirstRound(CreatorCandidate) : 
    def __init__(self, parties) :
        super().__init__(parties)
        
        
    def factory_method(self, election_data):
        candidate = self._init_candidate_model(election_data)
        if isinstance(election_data[5], str) :
            vote_to_convert = 0
            vote_to_convert = election_data[5].replace('.0','')
            candidate.vote_first_round = int(vote_to_convert)
        else : 
            candidate.vote_first_round = int(election_data[5])
        candidate.rate_vote_registered_first_round = float(election_data[6])
        candidate.rate_vote_expressed_first_round = float(election_data[7])
        return candidate