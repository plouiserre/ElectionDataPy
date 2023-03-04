class CandidateRepository : 
    def __init__(self, mydb) :
        self.mydb = mydb

    def save_candidates(self, candidates) :    
        mydb = self.mydb.get_my_db()
        
        mycursor = mydb.cursor()
        for candidate in candidates : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.CANDIDATE(CandidateLastName, CandidateFirstName, CandidateSexe, CandidateBirthDate, PartyId, Job, OldCandidate) VALUES (%s, %s,%s, %s,%s, %s,%s)"
            val = (candidate.last_name, candidate.first_name, candidate.sexe, candidate.birth_date, candidate.party_id, candidate.job, candidate.is_sorting)
            mycursor.execute(sql, val)
            
        mydb.commit()