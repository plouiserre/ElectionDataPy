from src.Models.CandidateModel import CandidateModel
from src.Factory.Creator import Creator

class CreatorCandidate(Creator) : 
    def factory_method(self, candidate_data) :         
        can = CandidateModel()
        can.last_name = candidate_data.candidate_last_name
        can.first_name = candidate_data.candidate_first_name 
        can.sexe =  candidate_data.candidate_sexe
        can.birth_date = candidate_data.candidate_birth_date 
        can.party = candidate_data.candidate_party 
        can.job = candidate_data.candidate_job 
        
        return can