from Models.ElectionModel import ElectionModel

class CreatorElection() : 
    def factory_method(self, first_round_data) : 
        election = ElectionModel()
        election.state_compute = first_round_data[4]
        election.registered = first_round_data[5]
        election.abstaining = first_round_data[6]
        election.rate_abstaining = float(first_round_data[7])
        election.voting = first_round_data[8]
        election.rate_voting = float(first_round_data[9])
        election.blank_balot = first_round_data[10]
        election.rate_blank_registered = float(first_round_data[11])
        election.rate_blank_voting = float(first_round_data[12])
        election.null_ballot = first_round_data[13]
        election.rate_null_registered = float(first_round_data[14])
        election.rate_null_voting = float(first_round_data[15])
        election.expressed = first_round_data[16]
        election.rate_express_registered = float(first_round_data[17])
        election.rate_express_voting = float(first_round_data[18])
        
        return election