from src.Factory.CreatorCandidate import CreatorCandidate
from src.Models.CandidateModel import CandidateModel

class CreatorCandidateSecondRound(CreatorCandidate) :
    def __init__(self, parties, datas_second_round_same_district) :
        super().__init__(parties)
        self.datas_second_round_same_district = datas_second_round_same_district
        self.candidate = CandidateModel()
        self.last_element_created = None
        
        
    def factory_method(self, election_data):
        self.data = election_data
        self.candidate  = self._init_candidate_model(self.data)
        if self.datas_second_round_same_district == None or len(self.datas_second_round_same_district) == 0 :
            self.__calculate_vote_without_last_election_data_created()
        else :
            self.__calculate_vote_with_last_election_data_created()
        self.__get_last_result_model_created()
        return self.candidate
    
    
    def __calculate_vote_without_last_election_data_created(self) : 
        if isinstance(self.data[5], str) :
            vote_to_convert = 0
            vote_to_convert = self.data[5].replace('.0','')
            self.candidate.vote_second_round = int(vote_to_convert)
        else : 
            self.candidate .vote_second_round = int(self.data[5])
        self.candidate.rate_vote_registered_second_round = float(self.data[6])
        self.candidate.rate_vote_expressed_second_round = float(self.data[7])
        
    
    def __calculate_vote_with_last_election_data_created(self) : 
        candidates = self.__get_good_candidate()
        last_vote = self.__get_vote_second_round_from_all_datas_same_districts(candidates)
        if isinstance(self.data[5], str) :
            vote_to_convert = 0
            vote_to_convert = self.data[5].replace('.0','')
            self.candidate.vote_second_round = int(vote_to_convert) + last_vote
        else : 
            self.candidate .vote_second_round = int(self.data[5]) + last_vote
        self.candidate.rate_vote_registered_second_round = round(self.__get_rate_vote_registered_second_round_from_all_datas_same_districts(candidates, (float(self.data[6]))),3)
        self.candidate.rate_vote_expressed_second_round = round(self.__get_rate_vote_expressed_second_round_from_all_datas_same_districts(candidates, (float(self.data[7]))),3)
        
    
    def __get_vote_second_round_from_all_datas_same_districts(self, candidates) : 
        vote_second_round = 0
        for data in candidates :
            vote_second_round += data.vote_second_round
        return vote_second_round
    
    
    def __get_rate_vote_registered_second_round_from_all_datas_same_districts(self, candidates, new_rate_vote_registered) : 
        rate_vote_registered = 0
        last_rate_vote_registered = 0
        for data in candidates :
            last_rate_vote_registered += data.rate_vote_registered_second_round
        rate_vote_registered = (last_rate_vote_registered + new_rate_vote_registered) / (len(self.datas_second_round_same_district) + 1 )
        return rate_vote_registered
    
    
    def __get_rate_vote_expressed_second_round_from_all_datas_same_districts(self, candidates, new_rate_vote_expressed) : 
        rate_vote_expressed = 0
        last_rate_vote_expressed = 0
        for data in candidates :
            last_rate_vote_expressed += data.rate_vote_expressed_second_round
        rate_vote_expressed = (last_rate_vote_expressed + new_rate_vote_expressed) / (len(self.datas_second_round_same_district) + 1)
        return rate_vote_expressed
    
        
    def __get_good_candidate(self) : 
        candidates = []
        for data in self.datas_second_round_same_district  :
            for c in data.candidates : 
                if c.first_name == self.candidate.first_name and c.last_name == self.candidate.last_name :
                    candidates.append(c) 
        return candidates
    
    
    def __get_last_result_model_created(self):
        self.last_element_created = self._init_candidate_model(self.data)
        if isinstance(self.data[5], str) :
            vote_to_convert = 0
            vote_to_convert = self.data[5].replace('.0','')
            self.last_element_created.vote_second_round = int(vote_to_convert)
        else : 
            self.last_element_created.vote_second_round = int(self.data[5])
        self.last_element_created.rate_vote_registered_second_round = float(self.data[6])
        self.last_element_created.rate_vote_expressed_second_round = float(self.data[7])