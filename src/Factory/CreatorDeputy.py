from src.Models.DeputyModel import DeputyModel
from src.Factory.Creator import Creator

class CreatorDeputy(Creator):
    def factory_method(self, candidate_data):
        deputy = DeputyModel()
        deputy.sexe = candidate_data.deputy.sexe
        deputy.first_name = candidate_data.deputy.first_name
        deputy.last_name= candidate_data.deputy.last_name
        deputy.birth_date = candidate_data.deputy.birth_date
        return deputy
    
    
    