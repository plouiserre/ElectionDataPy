import datetime

from src.Models.DeputyModel import DeputyModel

class CandidateModel : 
    def __init__(self) : 
        self.last_name = ''
        self.first_name = ''
        self.sexe = ''
        self.birth_date = datetime.date
        self.party_id = 0
        self.job = ''
        self.is_sorting = False
        self.deputy = DeputyModel()