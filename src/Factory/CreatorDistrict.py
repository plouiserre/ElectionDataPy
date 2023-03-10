from src.Models.DistrictModel import DistrictModel
from src.Factory.Creator import Creator

class CreatorDistrict(Creator) : 
    def factory_method(self, candidate_data):
        district = DistrictModel()
        district_number = candidate_data[2]
        district.number = int(district_number)
        district.name = candidate_data[3]
        return district