class ResultRepository : 
    def __init__(self, mydb) :
        self.mydb = mydb
    
    def save_results(self, results) :
        mydb = self.mydb.get_my_db()
        
        mycursor = mydb.cursor()
        
        for result in results : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.RESULT(StateCompute, Registered, Abstaining, RateAbstaining, Voting, RateVoting, BlankBalot, RateBlankRegistered, RateBlankVoting, NullBallot, RateNullRegistered, RateNullVoting, Expressed, RateExpressRegistered, RateExpressVoting, DistrictId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (result.state_compute, result.registered, result.abstaining, result.rate_abstaining, result.voting, result.rate_voting, result.blank_balot, result.rate_blank_registered, result.rate_blank_voting, result.null_ballot, result.rate_null_registered, result.rate_null_voting, result.expressed, result.rate_express_registered, result.rate_express_voting, result.district_id)
            mycursor.execute(sql, val)
            
        mydb.commit()
        