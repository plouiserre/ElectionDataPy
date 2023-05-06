import datetime

class CandidateModel : 
    def __init__(self) : 
        self.id = 0
        self.last_name = ''
        self.first_name = ''
        self.sexe = ''
        self.birthdate = datetime.date
        self.party_id = 0
        self.district_id = 0
        self.job = ''
        self.is_sorting = False
        self.vote = 0
        self.rate_vote_registered = 0.0
        self.rate_vote_expressed = 0.0