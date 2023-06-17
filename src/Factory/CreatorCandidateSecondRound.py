from src.Factory.CreatorCandidate import CreatorCandidate
from src.Models.CandidateModel import CandidateModel

class CreatorCandidateSecondRound(CreatorCandidate) :
    def __init__(self, parties, last_election_data_created) :
        super().__init__(parties)
        self.last_election_data_created = last_election_data_created
        self.candidate = CandidateModel()
        
        
    def factory_method(self, election_data):
        self.candidate  = self._init_candidate_model(election_data)
        if self.last_election_data_created == None :
            self.__calculate_vote_without_last_election_data_created(election_data)
        else :
            self.__calculate_vote_with_last_election_data_created(election_data)
        return self.candidate
    
    
    def __calculate_vote_without_last_election_data_created(self, election_data) : 
        if isinstance(election_data[5], str) :
            vote_to_convert = 0
            vote_to_convert = election_data[5].replace('.0','')
            self.candidate.vote_second_round = int(vote_to_convert)
        else : 
            self.candidate .vote_second_round = int(election_data[5])
        self.candidate.rate_vote_registered_second_round = float(election_data[6])
        self.candidate.rate_vote_expressed_second_round = float(election_data[7])
        
    
    def __calculate_vote_with_last_election_data_created(self, election_data) : 
        candidate = self.__get_good_candidate()
        if isinstance(election_data[5], str) :
            vote_to_convert = 0
            vote_to_convert = election_data[5].replace('.0','')
            self.candidate.vote_second_round = int(vote_to_convert) + candidate.vote_second_round
        else : 
            self.candidate .vote_second_round = int(election_data[5]) + candidate.vote_second_round
        self.candidate.rate_vote_registered_second_round = (float(election_data[6]) + candidate.rate_vote_registered_second_round ) / 2
        self.candidate.rate_vote_expressed_second_round = (float(election_data[7]) + candidate.rate_vote_expressed_second_round ) / 2
        
        
    def __get_good_candidate(self) : 
        candidate = CandidateModel()
        for c in self.last_election_data_created.candidates :
            if c.first_name == self.candidate.first_name and c.last_name == self.candidate.last_name :
                candidate = c 
                break
        return candidate