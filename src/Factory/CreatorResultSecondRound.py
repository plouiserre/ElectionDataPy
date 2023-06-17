from src.Factory.CreatorResult import CreatorResult

class CreatorResultSecondRound(CreatorResult) :
    def __init__(self, last_election_data_created):
        super().__init__()
        self.last_election_data_created = last_election_data_created
        
        
    def factory_method(self, second_round_data):
        self.data = second_round_data
        if self.last_election_data_created == None :
            self.__get_result_without_last_election_data_created()
        else :
            self.__get_result_with_last_election_data_created()
        return self.result
    
    
    def __get_result_without_last_election_data_created(self) :
        self.result.state_compute = self.data[4]
        self.__get_results_numbers_global_without_last_election_data_created(self.data[5])
        self.result.rate_abstaining = float(self.data[6])
        self.result.voting = int(self.data[7])
        self.result.rate_voting = float(self.data[8])
        self.result.blank_balot = int(self.data[9])
        self.result.rate_blank_registered = float(self.data[10])
        self.result.rate_blank_voting = float(self.data[11])
        self.result.null_ballot = int(self.data[12])
        self.result.rate_null_registered = float(self.data[13])
        self.result.rate_null_voting = float(self.data[14])
        self.result.expressed = int(self.data[15])
        self.result.rate_express_registered = float(self.data[16])
        self.result.rate_express_voting = float(self.data[17])
        
        return self.result
    
    
    #TODO factorize with first round result
    def __get_results_numbers_global_without_last_election_data_created(self, datas) :
        datas_split = datas.split(" ")
        self.result.registered = int(datas_split[0])
        self.result.abstaining = int(datas_split[1])
    
    
    def __get_result_with_last_election_data_created(self) :
        self.result.state_compute = self.data[4]
        self.__get_results_numbers_global_with_last_election_data_created(self.data[5])
        self.result.rate_abstaining = (float(self.data[6])+ self.last_election_data_created.rate_abstaining ) / 2
        self.result.voting = int(self.data[7]) + self.last_election_data_created.voting
        self.result.rate_voting = (float(self.data[8]) + self.last_election_data_created.rate_voting ) / 2
        self.result.blank_balot = int(self.data[9]) + self.last_election_data_created.blank_balot
        self.result.rate_blank_registered = (float(self.data[10]) + self.last_election_data_created.rate_blank_registered) / 2
        self.result.rate_blank_voting = (float(self.data[11]) + self.last_election_data_created.rate_blank_voting) / 2
        self.result.null_ballot = int(self.data[12]) + self.last_election_data_created.null_ballot
        self.result.rate_null_registered = (float(self.data[13]) + self.last_election_data_created.rate_null_registered) / 2
        self.result.rate_null_voting = (float(self.data[14]) + self.last_election_data_created.rate_null_voting) / 2
        self.result.expressed = int(self.data[15]) + self.last_election_data_created.expressed
        self.result.rate_express_registered = (float(self.data[16]) + self.last_election_data_created.rate_express_registered) / 2
        self.result.rate_express_voting = (float(self.data[17]) + self.last_election_data_created.rate_express_voting ) / 2
        
        
    #TODO factorize with first round result
    def __get_results_numbers_global_with_last_election_data_created(self, datas) :
        datas_split = datas.split(" ")
        self.result.registered = int(datas_split[0]) + self.last_election_data_created.registered
        self.result.abstaining = int(datas_split[1]) + self.last_election_data_created.abstaining