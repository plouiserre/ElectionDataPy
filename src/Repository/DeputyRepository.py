class DeputyRepository :
    def __init__(self, mydb) :
        self.mydb = mydb
        
    def save_deputies(self, deputies) : 
        mydb = self.mydb.get_my_db()
        
        mycursor = mydb.cursor()
        for deputy in deputies : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.Deputy(DeputyLastName, DeputyFirstName, DeputySexe, DeputyBirthDate, CandidateId, OldCandidate) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (deputy.last_name, deputy.first_name, deputy.sexe, deputy.birthdate, deputy.candidate.id, deputy.is_sorting)
            mycursor.execute(sql, val)
            
        mydb.commit()