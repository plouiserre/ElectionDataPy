from src.Models.ElectionModel import ElectionModel

class CreatorElection() : 
    def __init__(self) -> None:
        self.election = ElectionModel()
    
    def factory_method(self, first_round_data) : 
        self.election.state_compute = first_round_data[4]
        self.__get_elections_numbers_global(first_round_data[5])
        self.election.rate_abstaining = float(first_round_data[6])
        self.election.voting = int(first_round_data[7])
        self.election.rate_voting = float(first_round_data[8])
        self.election.blank_balot = int(first_round_data[9])
        self.election.rate_blank_registered = float(first_round_data[10])
        self.election.rate_blank_voting = float(first_round_data[11])
        self.election.null_ballot = int(first_round_data[12])
        self.election.rate_null_registered = float(first_round_data[13])
        self.election.rate_null_voting = float(first_round_data[14])
        self.election.expressed = int(first_round_data[15])
        self.election.rate_express_registered = float(first_round_data[16])
        self.election.rate_express_voting = float(first_round_data[17])
        
        return self.election
    
    def __get_elections_numbers_global(self, datas) :
        datas_split = datas.split(" ")
        self.election.registered = int(datas_split[0])
        self.election.abstaining = int(datas_split[1])