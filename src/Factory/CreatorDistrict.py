from src.Models.DistrictModel import DistrictModel

class CreatorDistrict() : 
    def factory_method(self, candidate_data):
        district = DistrictModel()
        district_number = candidate_data[2]
        district.number = int(district_number)
        district.name = candidate_data[3]
        return district