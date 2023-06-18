from src.Factory.CreatorResult import CreatorResult

class CreatorResultSecondRound(CreatorResult) :
    def __init__(self, last_election_data_created):
        super().__init__()
        self.last_election_data_created = last_election_data_created
        
        
    def factory_method(self, second_round_data):
        self.data = second_round_data
        self.result.round_number = 2
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
        self.result.rate_abstaining = round((self.__get_rate_abstaining_from_all_last_election_datas() + float(self.data[6])) / (len(self.last_election_data_created) + 1), 3)
        self.result.voting = int(self.data[7]) + self.__get_voting_from_all_last_election_datas()
        self.result.rate_voting = round((self.__get_rate_voting_from_all_last_election_datas() + float(self.data[8])) / (len(self.last_election_data_created) + 1), 3)
        self.result.blank_balot = int(self.data[9]) + self.__get_blank_ballot_from_all_last_election_datas()
        self.result.rate_blank_registered = round((self.__get_rate_blank_registered_from_all_last_election_datas() + float(self.data[10])) / (len(self.last_election_data_created) + 1), 3)
        self.result.rate_blank_voting = round((self.__get_rate_blank_voting_from_all_last_election_datas() + float(self.data[11])) / (len(self.last_election_data_created) + 1), 3)
        self.result.null_ballot = int(self.data[12]) + self.__get_rate_null_ballot_from_all_last_election_datas()
        self.result.rate_null_registered = round((self.__get_rate_null_registered_from_all_last_election_datas() + float(self.data[13])) / (len(self.last_election_data_created) + 1) , 3)
        self.result.rate_null_voting = round((self.__get_rate_null_voting_from_all_last_election_datas() + float(self.data[14])) / (len(self.last_election_data_created) + 1), 3)  
        self.result.expressed = int(self.data[15]) + self.__get_expressed_from_all_last_election_datas()
        self.result.rate_express_registered = round((self.__get_rate_express_registered_from_all_last_election_datas() + float(self.data[16])) / (len(self.last_election_data_created) + 1), 3)  
        self.result.rate_express_voting = round((self.__get_rate_express_voting_from_all_last_election_datas() + float(self.data[17])) / (len(self.last_election_data_created) + 1), 3)  
        
        
    #TODO factorize with first round result
    def __get_results_numbers_global_with_last_election_data_created(self, datas) :
        datas_split = datas.split(" ")
        self.result.registered = int(datas_split[0]) + self.__get_registered_from_all_last_election_datas()
        self.result.abstaining = int(datas_split[1]) + self.__get_abstaining_from_all_last_election_datas()
        
           
    def __get_registered_from_all_last_election_datas(self) :
        registered = 0
        for data in self.last_election_data_created :
            registered += data.registered
        return registered
    
    
    def __get_abstaining_from_all_last_election_datas(self) :
        abstaining = 0
        for data in self.last_election_data_created :
            abstaining += data.abstaining
        return abstaining
        
    
    def __get_rate_abstaining_from_all_last_election_datas(self) :
        rate_abstaining = 0
        for data in self.last_election_data_created :
            rate_abstaining += data.rate_abstaining
        return rate_abstaining
    
    
    def __get_voting_from_all_last_election_datas(self) :
        voting = 0
        for data in self.last_election_data_created :
            voting += data.voting
        return voting
    
    
    def __get_rate_voting_from_all_last_election_datas(self) :
        rate_voting = 0
        for data in self.last_election_data_created :
            rate_voting += data.rate_voting
        return rate_voting
    
    
    def __get_blank_ballot_from_all_last_election_datas(self) :
        blank_balot = 0
        for data in self.last_election_data_created :
            blank_balot += data.blank_balot
        return blank_balot
    
    
    def __get_rate_blank_registered_from_all_last_election_datas(self) :
        rate_blank_registered = 0
        for data in self.last_election_data_created :
            rate_blank_registered += data.rate_blank_registered
        return rate_blank_registered
    
    
    def __get_rate_blank_voting_from_all_last_election_datas(self) :
        rate_blank_voting = 0
        for data in self.last_election_data_created :
            rate_blank_voting += data.rate_blank_voting
        return rate_blank_voting
    
    
    def __get_rate_null_ballot_from_all_last_election_datas(self) :
        null_ballot = 0
        for data in self.last_election_data_created :
            null_ballot += data.null_ballot
        return null_ballot
    
    
    def __get_rate_null_registered_from_all_last_election_datas(self) :
        rate_null_registered = 0
        for data in self.last_election_data_created :
            rate_null_registered += data.rate_null_registered
        return rate_null_registered
    
    def __get_rate_null_voting_from_all_last_election_datas(self) :
        rate_null_voting = 0
        for data in self.last_election_data_created :
            rate_null_voting += data.rate_null_voting
        return rate_null_voting
    
    def __get_expressed_from_all_last_election_datas(self) :
        expressed = 0
        for data in self.last_election_data_created :
            expressed += data.expressed
        return expressed
    
    
    def __get_rate_express_registered_from_all_last_election_datas(self) :
        rate_express_registered = 0
        for data in self.last_election_data_created :
            rate_express_registered += data.rate_express_registered
        return rate_express_registered
    
    
    def __get_rate_express_voting_from_all_last_election_datas(self) :
        rate_express_voting = 0
        for data in self.last_election_data_created :
            rate_express_voting += data.rate_express_voting
        return rate_express_voting