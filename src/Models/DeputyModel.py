import datetime

from src.Models.CandidateModel import CandidateModel

class DeputyModel : 
    def __init__(self) :
        self.sexe = ''
        self.last_name = ''
        self.first_name = ''
        self.birthdate = datetime.date
        self.is_sorting = False
        self.candidate = CandidateModel()