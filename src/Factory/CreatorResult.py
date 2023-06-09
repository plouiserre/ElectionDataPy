from src.Models.ResultModel import ResultModel

class CreatorResult() : 
    def __init__(self) -> None:
        self.result = ResultModel()
    
    def factory_method(self, first_round_data) : 
        self.result.state_compute = first_round_data[4]
        self.__get_results_numbers_global(first_round_data[5])
        self.result.rate_abstaining = float(first_round_data[6])
        self.result.voting = int(first_round_data[7])
        self.result.rate_voting = float(first_round_data[8])
        self.result.blank_balot = int(first_round_data[9])
        self.result.rate_blank_registered = float(first_round_data[10])
        self.result.rate_blank_voting = float(first_round_data[11])
        self.result.null_ballot = int(first_round_data[12])
        self.result.rate_null_registered = float(first_round_data[13])
        self.result.rate_null_voting = float(first_round_data[14])
        self.result.expressed = int(first_round_data[15])
        self.result.rate_express_registered = float(first_round_data[16])
        self.result.rate_express_voting = float(first_round_data[17])
        
        return self.result
    
    def __get_results_numbers_global(self, datas) :
        datas_split = datas.split(" ")
        self.result.registered = int(datas_split[0])
        self.result.abstaining = int(datas_split[1])