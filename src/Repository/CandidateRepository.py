class CandidateRepository : 
    def __init__(self, mydb) :
        self.mydb = mydb

    def save_candidates(self, candidates) :    
        mydb = self.mydb.get_my_db()
        
        mycursor = mydb.cursor()
        for candidate in candidates : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.CANDIDATE(CandidateLastName, CandidateFirstName, CandidateSexe, CandidateBirthDate, PartyId, DistrictId, Job, OldCandidate, VoteFirstRound, RateVoteExpressedFirstRound, RateVoteRegisteredFirstRound) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (candidate.last_name, candidate.first_name, candidate.sexe, candidate.birthdate, candidate.party_id, candidate.district_id, candidate.job, candidate.is_sorting, candidate.vote_first_round, candidate.rate_vote_registered_first_round, candidate.rate_vote_expressed_first_round)
            mycursor.execute(sql, val)
            candidate.id = mycursor.lastrowid
            
        mydb.commit()