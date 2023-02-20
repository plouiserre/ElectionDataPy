from src.Models.DistrictModel import DistrictModel
from src.Factory.Creator import Creator

class CreatorDistrict(Creator) : 
    def factory_method(self, candidate_data):
        district = DistrictModel()
        district.number = candidate_data.district_number
        district.name = candidate_data.district_name
        return district